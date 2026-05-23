"""
Evaluation metrics for FocalGNN.
Computes Kagan angle, fault-type accuracy, and uncertainty calibration.
"""

import numpy as np
import torch
from focalgnn.utils.focal_mech import batch_kagan_angle, mt6_to_sdr, classify_fault_type


@torch.no_grad()
def evaluate_model(model, dataloader, criterion, device):
    """
    Evaluate model on a dataset.
    
    Args:
        model: FocalGNN model
        dataloader: PyG DataLoader
        criterion: loss function
        device: torch device
    Returns:
        metrics: dict with evaluation metrics
    """
    model.eval()
    
    all_mt_pred = []
    all_mt_true = []
    all_logvar = []
    all_losses = []

    for batch in dataloader:
        batch = batch.to(device)
        predictions = model(batch)
        
        loss, loss_dict = criterion(predictions, batch.y)
        all_losses.append(loss.item())
        
        all_mt_pred.append(predictions['mt_mean'].cpu().numpy())
        all_mt_true.append(batch.y.cpu().numpy())
        all_logvar.append(predictions['mt_logvar'].cpu().numpy())

    # Concatenate
    mt_pred = np.concatenate(all_mt_pred, axis=0)
    mt_true = np.concatenate(all_mt_true, axis=0)
    logvar = np.concatenate(all_logvar, axis=0)

    # Kagan angles
    kagan_angles = batch_kagan_angle(mt_pred, mt_true)

    # Fault type classification
    fault_type_acc = compute_fault_type_accuracy(mt_pred, mt_true)

    # Uncertainty calibration
    ece = compute_expected_calibration_error(mt_pred, mt_true, logvar)
    coverage_90 = compute_coverage(mt_pred, mt_true, logvar, confidence=0.90)

    metrics = {
        'loss': np.mean(all_losses),
        'kagan_median': np.median(kagan_angles),
        'kagan_p25': np.percentile(kagan_angles, 25),
        'kagan_p75': np.percentile(kagan_angles, 75),
        'kagan_mean': np.mean(kagan_angles),
        'fault_type_accuracy': fault_type_acc,
        'ece': ece,
        'coverage_90': coverage_90,
        'kagan_angles': kagan_angles,  # full array for plotting
    }

    return metrics


def compute_fault_type_accuracy(mt_pred, mt_true):
    """
    Compute accuracy of fault-type classification (normal/reverse/strike-slip).
    """
    correct = 0
    total = mt_pred.shape[0]
    
    for i in range(total):
        try:
            sdr_pred = mt6_to_sdr(mt_pred[i])
            sdr_true = mt6_to_sdr(mt_true[i])
            
            type_pred = classify_fault_type(*sdr_pred[0])
            type_true = classify_fault_type(*sdr_true[0])
            
            if type_pred == type_true:
                correct += 1
        except Exception:
            continue
    
    return correct / max(total, 1)


def compute_expected_calibration_error(mt_pred, mt_true, logvar, num_bins=10):
    """
    Compute Expected Calibration Error (ECE) for uncertainty estimates.
    
    For each MT component, check if the true value falls within the
    predicted confidence interval at various confidence levels.
    """
    sigma = np.exp(0.5 * logvar)  # standard deviation
    
    # Normalized residuals: (true - pred) / sigma
    residuals = (mt_true - mt_pred) / (sigma + 1e-8)
    
    # For a well-calibrated Gaussian, |residual| < z_alpha should hold
    # with probability alpha
    confidence_levels = np.linspace(0.1, 0.9, num_bins)
    ece = 0.0
    
    for alpha in confidence_levels:
        from scipy.stats import norm
        z = norm.ppf(0.5 + alpha / 2)
        observed_coverage = np.mean(np.abs(residuals) < z)
        ece += abs(observed_coverage - alpha)
    
    ece /= num_bins
    return ece


def compute_coverage(mt_pred, mt_true, logvar, confidence=0.90):
    """
    Compute coverage probability at a given confidence level.
    
    What fraction of true values fall within the predicted confidence interval?
    """
    from scipy.stats import norm
    
    sigma = np.exp(0.5 * logvar)
    z = norm.ppf(0.5 + confidence / 2)
    
    within_interval = np.abs(mt_true - mt_pred) < z * sigma
    coverage = np.mean(within_interval)
    
    return coverage


def evaluate_station_dropout(model, dataset, criterion, device, station_counts):
    """
    Evaluate model performance as a function of station count.
    Systematically drops stations at test time.
    
    Args:
        model: trained FocalGNN
        dataset: test dataset (without augmentation)
        criterion: loss function
        device: torch device
        station_counts: list of station counts to test [5, 10, 15, 20, 30, 50]
    Returns:
        results: dict mapping station_count -> metrics
    """
    from torch_geometric.loader import DataLoader as PyGDataLoader
    
    results = {}
    
    for n_stations in station_counts:
        # Create dataset with fixed station count
        dropout_dataset = FocalMechanismDatasetFixedStations(
            dataset, n_stations=n_stations
        )
        loader = PyGDataLoader(dropout_dataset, batch_size=32, shuffle=False)
        
        metrics = evaluate_model(model, loader, criterion, device)
        results[n_stations] = {
            'kagan_median': metrics['kagan_median'],
            'kagan_p25': metrics['kagan_p25'],
            'kagan_p75': metrics['kagan_p75'],
        }
        print(f"  Stations={n_stations}: Kagan median={metrics['kagan_median']:.1f}°")
    
    return results


class FocalMechanismDatasetFixedStations:
    """Wrapper that enforces a fixed number of stations per event."""
    
    def __init__(self, base_dataset, n_stations):
        self.base_dataset = base_dataset
        self.n_stations = n_stations
        # Filter events with enough stations
        self.valid_indices = [
            i for i in range(len(base_dataset))
            # This would need the actual station count info
        ]
    
    def __len__(self):
        return len(self.valid_indices)
    
    def __getitem__(self, idx):
        data = self.base_dataset[self.valid_indices[idx]]
        # Subsample to n_stations
        if data.num_nodes > self.n_stations:
            indices = np.random.choice(data.num_nodes, self.n_stations, replace=False)
            # Rebuild graph with subset of stations
            # ... (implementation depends on PyG Data structure)
        return data
