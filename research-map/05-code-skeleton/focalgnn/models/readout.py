"""
Graph-level readout and prediction head for FocalGNN.
Aggregates station-level embeddings into event-level prediction.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import global_mean_pool, global_max_pool


class AttentionPooling(nn.Module):
    """
    Attention-weighted global pooling.
    Learns which stations are most informative for the final prediction.
    
    gate_i = softmax(MLP(x_i))
    z = sum(gate_i * x_i)
    """

    def __init__(self, in_channels: int, hidden_dim: int = 128):
        super().__init__()
        self.gate = nn.Sequential(
            nn.Linear(in_channels, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x, batch):
        """
        Args:
            x: (N_total, in_channels) node features (all nodes in batch)
            batch: (N_total,) batch assignment vector
        Returns:
            z: (B, in_channels) graph-level embeddings
            gate_weights: (N_total, 1) attention weights (for interpretability)
        """
        # Compute gate scores
        gate_scores = self.gate(x)  # (N_total, 1)

        # Softmax within each graph
        gate_weights = self._scatter_softmax(gate_scores, batch)

        # Weighted sum
        weighted = x * gate_weights  # (N_total, in_channels)

        # Aggregate per graph
        num_graphs = batch.max().item() + 1
        z = torch.zeros(num_graphs, x.size(1), device=x.device)
        z.scatter_add_(0, batch.unsqueeze(1).expand_as(weighted), weighted)

        return z, gate_weights

    def _scatter_softmax(self, src, index):
        """Softmax over groups defined by index."""
        # Subtract max for numerical stability
        max_vals = torch.zeros(index.max() + 1, 1, device=src.device)
        max_vals.scatter_reduce_(0, index.unsqueeze(1), src, reduce='amax', include_self=False)
        src_stable = src - max_vals[index]

        # Exp and normalize
        exp_src = torch.exp(src_stable)
        sum_exp = torch.zeros(index.max() + 1, 1, device=src.device)
        sum_exp.scatter_add_(0, index.unsqueeze(1), exp_src)
        return exp_src / (sum_exp[index] + 1e-8)


class MomentTensorHead(nn.Module):
    """
    Prediction head that outputs moment tensor components with uncertainty.
    
    Output: 12 values
        - 6 moment tensor means: Mxx, Myy, Mzz, Mxy, Mxz, Myz
        - 6 moment tensor log-variances
    """

    def __init__(
        self,
        in_channels: int = 320,
        hidden_dims: list = [256, 128],
        dropout: float = 0.1,
    ):
        super().__init__()
        layers = []
        prev_dim = in_channels

        for hdim in hidden_dims:
            layers.extend([
                nn.Linear(prev_dim, hdim),
                nn.ReLU(),
                nn.Dropout(dropout),
            ])
            prev_dim = hdim

        self.features = nn.Sequential(*layers)

        # Separate heads for mean and variance (better optimization)
        self.mean_head = nn.Linear(prev_dim, 6)
        self.logvar_head = nn.Linear(prev_dim, 6)

    def forward(self, z):
        """
        Args:
            z: (B, in_channels) graph-level embedding
        Returns:
            mt_mean: (B, 6) predicted moment tensor components
            mt_logvar: (B, 6) predicted log-variance (uncertainty)
        """
        h = self.features(z)
        mt_mean = self.mean_head(h)
        mt_logvar = self.logvar_head(h)

        # Clamp log-variance to prevent numerical issues
        mt_logvar = torch.clamp(mt_logvar, min=-10.0, max=10.0)

        return mt_mean, mt_logvar


class FocalMechanismReadout(nn.Module):
    """
    Complete readout module: attention pooling + moment tensor prediction.
    """

    def __init__(
        self,
        in_channels: int = 320,
        pool_hidden_dim: int = 128,
        pred_hidden_dims: list = [256, 128],
        dropout: float = 0.1,
    ):
        super().__init__()
        self.pooling = AttentionPooling(in_channels, pool_hidden_dim)
        self.predictor = MomentTensorHead(in_channels, pred_hidden_dims, dropout)

    def forward(self, x, batch):
        """
        Args:
            x: (N_total, in_channels) node features
            batch: (N_total,) batch assignment
        Returns:
            mt_mean: (B, 6) predicted MT
            mt_logvar: (B, 6) predicted uncertainty
            gate_weights: (N_total, 1) station importance weights
        """
        z, gate_weights = self.pooling(x, batch)
        mt_mean, mt_logvar = self.predictor(z)
        return mt_mean, mt_logvar, gate_weights
