"""
Main training loop for FocalGNN.
"""

import os
import yaml
import argparse
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torch_geometric.loader import DataLoader as PyGDataLoader

from focalgnn.models import FocalGNN, SingleCNNBaseline, TransformerBaseline, GNNDistanceBaseline
from focalgnn.data import FocalMechanismDataset, collate_fn
from focalgnn.losses import FocalGNNLoss
from focalgnn.training.evaluate import evaluate_model


def train(config):
    """
    Main training function.
    
    Args:
        config: dict with all hyperparameters (loaded from YAML)
    """
    # Setup
    device = torch.device(config['experiment']['device'] if torch.cuda.is_available() else 'cpu')
    torch.manual_seed(config['experiment']['seed'])
    np.random.seed(config['experiment']['seed'])

    print(f"Device: {device}")
    print(f"Experiment: {config['experiment']['name']}")

    # Data
    train_dataset = FocalMechanismDataset(
        h5_path=config['data']['h5_path'],
        split='train',
        min_stations=config['data']['min_stations'],
        augment=True,
        station_dropout_rate=tuple(config['augmentation']['station_dropout']['drop_rate']),
    )
    val_dataset = FocalMechanismDataset(
        h5_path=config['data']['h5_path'],
        split='val',
        min_stations=config['data']['min_stations'],
        augment=False,
    )

    train_loader = PyGDataLoader(
        train_dataset,
        batch_size=config['training']['batch_size'],
        shuffle=True,
        num_workers=config['experiment']['num_workers'],
    )
    val_loader = PyGDataLoader(
        val_dataset,
        batch_size=config['training']['batch_size'],
        shuffle=False,
        num_workers=config['experiment']['num_workers'],
    )

    print(f"Train: {len(train_dataset)} events")
    print(f"Val: {len(val_dataset)} events")

    # Model
    model = build_model(config).to(device)
    print(f"Model parameters: {model.num_parameters:,}")

    # Loss
    criterion = FocalGNNLoss(
        nll_weight=config['loss']['nll_weight'],
        dc_weight=config['loss']['dc_constraint_weight'],
        polarity_weight=config['loss']['polarity_weight'],
    )

    # Optimizer
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=config['training']['optimizer']['lr'],
        weight_decay=config['training']['optimizer']['weight_decay'],
    )

    # Scheduler
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
        optimizer,
        T_max=config['training']['scheduler']['T_max'],
        eta_min=config['training']['scheduler']['eta_min'],
    )

    # Training loop
    best_val_kagan = float('inf')
    patience_counter = 0
    patience = config['training']['early_stopping']['patience']

    for epoch in range(config['training']['num_epochs']):
        # Train
        model.train()
        train_losses = []

        for batch in train_loader:
            batch = batch.to(device)
            optimizer.zero_grad()

            predictions = model(batch)
            loss, loss_dict = criterion(predictions, batch.y)

            loss.backward()

            # Gradient clipping
            if config['training']['gradient_clip_norm'] > 0:
                nn.utils.clip_grad_norm_(
                    model.parameters(),
                    config['training']['gradient_clip_norm']
                )

            optimizer.step()
            train_losses.append(loss_dict)

        scheduler.step()

        # Validate
        val_metrics = evaluate_model(model, val_loader, criterion, device)

        # Logging
        train_loss_avg = np.mean([d['loss_total'].item() for d in train_losses])
        val_kagan_median = val_metrics['kagan_median']

        print(f"Epoch {epoch+1}/{config['training']['num_epochs']} | "
              f"Train Loss: {train_loss_avg:.4f} | "
              f"Val Kagan (median): {val_kagan_median:.1f}° | "
              f"LR: {scheduler.get_last_lr()[0]:.6f}")

        # Early stopping
        if val_kagan_median < best_val_kagan:
            best_val_kagan = val_kagan_median
            patience_counter = 0
            # Save best model
            save_checkpoint(model, optimizer, epoch, val_metrics, config)
            print(f"  -> New best! Saved checkpoint.")
        else:
            patience_counter += 1
            if patience_counter >= patience:
                print(f"Early stopping at epoch {epoch+1}")
                break

    print(f"\nTraining complete. Best val Kagan: {best_val_kagan:.1f}°")
    return best_val_kagan


def build_model(config):
    """Build model from config."""
    model_cfg = config['model']
    
    model = FocalGNN(
        waveform_channels=3,
        waveform_length=int(config['data']['waveform_window_sec'] * config['data']['sampling_rate']),
        encoder_channels=model_cfg['encoder']['channels'],
        geometry_input_dim=len(config['graph']['node_features']['geometry_inputs']),
        geometry_embed_dim=config['graph']['node_features']['geometry_embed_dim'],
        gat_hidden_dim=model_cfg['gat']['hidden_dim'],
        gat_num_layers=model_cfg['gat']['num_layers'],
        gat_heads=model_cfg['gat']['num_heads'],
        edge_feature_dim=len(config['graph']['edge_features']['inputs']),
        edge_embed_dim=config['graph']['edge_features']['embed_dim'],
        gat_dropout=model_cfg['gat']['dropout'],
        pool_hidden_dim=model_cfg['readout']['gate_hidden_dim'],
        pred_hidden_dims=model_cfg['prediction_head']['hidden_dims'],
        pred_dropout=model_cfg['prediction_head']['dropout'],
    )
    return model


def save_checkpoint(model, optimizer, epoch, metrics, config):
    """Save model checkpoint."""
    checkpoint_dir = f"checkpoints/{config['experiment']['name']}"
    os.makedirs(checkpoint_dir, exist_ok=True)
    
    torch.save({
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'metrics': metrics,
        'config': config,
    }, f"{checkpoint_dir}/best_model.pt")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', type=str, default='config/default.yaml')
    parser.add_argument('--data', type=str, required=True, help='Path to HDF5 data')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    config['data']['h5_path'] = args.data
    train(config)
