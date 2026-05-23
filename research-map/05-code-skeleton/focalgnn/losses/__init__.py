"""
Loss functions for FocalGNN training.
Combines NLL, double-couple constraint, and polarity consistency.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F


class FocalGNNLoss(nn.Module):
    """
    Combined loss for focal mechanism estimation:
    L = L_NLL + lambda_1 * L_DC + lambda_2 * L_polarity
    """

    def __init__(
        self,
        nll_weight: float = 1.0,
        dc_weight: float = 0.1,
        polarity_weight: float = 0.05,
    ):
        super().__init__()
        self.nll_weight = nll_weight
        self.dc_weight = dc_weight
        self.polarity_weight = polarity_weight

    def forward(self, predictions, targets, polarities=None, geometry=None):
        """
        Args:
            predictions: dict with 'mt_mean' (B,6) and 'mt_logvar' (B,6)
            targets: (B, 6) true moment tensor components
            polarities: optional (N_total,) observed first-motion polarities
            geometry: optional (N_total, 7) station geometry for polarity computation
        Returns:
            total_loss, loss_dict
        """
        mt_mean = predictions['mt_mean']
        mt_logvar = predictions['mt_logvar']

        # 1. NLL Loss
        loss_nll = self.nll_loss(mt_mean, mt_logvar, targets)

        # 2. Double-Couple Constraint
        loss_dc = self.dc_constraint(mt_mean)

        # Total
        total = self.nll_weight * loss_nll + self.dc_weight * loss_dc

        loss_dict = {
            'loss_total': total,
            'loss_nll': loss_nll,
            'loss_dc': loss_dc,
        }

        # 3. Polarity Consistency (optional)
        if polarities is not None and geometry is not None:
            loss_pol = self.polarity_consistency(mt_mean, polarities, geometry)
            total = total + self.polarity_weight * loss_pol
            loss_dict['loss_polarity'] = loss_pol
            loss_dict['loss_total'] = total

        return total, loss_dict

    def nll_loss(self, mt_mean, mt_logvar, mt_true):
        """
        Heteroscedastic Gaussian NLL.
        L = 0.5 * sum[ (y-mu)^2 / sigma^2 + log(sigma^2) ]
        """
        precision = torch.exp(-mt_logvar)  # 1/sigma^2
        diff_sq = (mt_true - mt_mean) ** 2
        loss = 0.5 * (precision * diff_sq + mt_logvar)
        return loss.mean()

    def dc_constraint(self, mt_mean):
        """
        Double-couple constraint: det(M) = 0 for pure DC.
        Penalize |det(M)| / ||M||_F^3
        """
        # Reconstruct 3x3 symmetric tensor from 6 components
        # Order: Mxx, Myy, Mzz, Mxy, Mxz, Myz
        B = mt_mean.size(0)
        M = torch.zeros(B, 3, 3, device=mt_mean.device)
        M[:, 0, 0] = mt_mean[:, 0]  # Mxx
        M[:, 1, 1] = mt_mean[:, 1]  # Myy
        M[:, 2, 2] = mt_mean[:, 2]  # Mzz
        M[:, 0, 1] = M[:, 1, 0] = mt_mean[:, 3]  # Mxy
        M[:, 0, 2] = M[:, 2, 0] = mt_mean[:, 4]  # Mxz
        M[:, 1, 2] = M[:, 2, 1] = mt_mean[:, 5]  # Myz

        # det(M) and Frobenius norm
        det_M = torch.det(M)  # (B,)
        frob_norm = torch.norm(M.view(B, -1), dim=1)  # (B,)

        # Normalized constraint
        loss = (det_M.abs() / (frob_norm ** 3 + 1e-8)).mean()
        return loss

    def polarity_consistency(self, mt_mean, polarities, geometry):
        """
        Ensure predicted MT radiation pattern agrees with observed polarities.
        
        For P-wave, the polarity at a station is determined by:
            p = sign(gamma^T * M * gamma)
        where gamma is the ray direction (take-off angle + azimuth).
        
        Args:
            mt_mean: (B, 6) predicted MT (need to broadcast to stations)
            polarities: (N_total,) observed polarities (+1/-1 or 1/0)
            geometry: (N_total, 7) with [az, to, dist, cos_az, sin_az, cos_to, sin_to]
        """
        # Extract azimuth and take-off angle
        cos_az = geometry[:, 3]  # cos(azimuth)
        sin_az = geometry[:, 4]  # sin(azimuth)
        cos_to = geometry[:, 5]  # cos(takeoff)
        sin_to = geometry[:, 6]  # sin(takeoff)

        # Ray direction vector in NED coordinates
        # gamma = [sin(to)*cos(az), sin(to)*sin(az), cos(to)]  (approximate)
        gamma = torch.stack([
            sin_to * cos_az,
            sin_to * sin_az,
            cos_to,
        ], dim=-1)  # (N, 3)

        # This requires knowing which graph each station belongs to
        # For simplicity, return 0 if polarities not available
        # Full implementation needs batch assignment to get per-station MT
        
        # Placeholder - full implementation needs careful batch handling
        return torch.tensor(0.0, device=mt_mean.device)
