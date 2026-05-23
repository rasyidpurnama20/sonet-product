"""
FocalGNN: Full model assembly.
Physics-Informed Graph Attention Network for Earthquake Focal Mechanism Estimation.
"""

import torch
import torch.nn as nn
from torch_geometric.data import Batch

from .encoder import ResNet1DEncoder, GeometryEncoder
from .gat_layers import FocalGATStack
from .readout import FocalMechanismReadout


class FocalGNN(nn.Module):
    """
    FocalGNN: End-to-end model for focal mechanism estimation.
    
    Pipeline:
        1. Per-station CNN encoder: waveform → embedding
        2. Geometry encoder: (az, takeoff, dist) → embedding
        3. Concatenate waveform + geometry embeddings as node features
        4. GATv2 stack with physics-informed edges: message passing
        5. Attention pooling + MT prediction head
    
    Input: PyG Batch with:
        - x_waveform: (N_total, 3, T) waveforms for all stations
        - x_geometry: (N_total, 7) geometry features
        - edge_index: (2, E_total) edge connectivity
        - edge_attr: (E_total, edge_dim) physics-informed edge features
        - batch: (N_total,) graph assignment
    
    Output:
        - mt_mean: (B, 6) moment tensor prediction
        - mt_logvar: (B, 6) uncertainty
        - gate_weights: (N_total, 1) station importance
    """

    def __init__(
        self,
        # Encoder config
        waveform_channels: int = 3,
        waveform_length: int = 1000,
        encoder_channels: list = [32, 64, 128, 256],
        geometry_input_dim: int = 7,
        geometry_embed_dim: int = 64,
        # GAT config
        gat_hidden_dim: int = 320,
        gat_num_layers: int = 3,
        gat_heads: int = 4,
        edge_feature_dim: int = 5,
        edge_embed_dim: int = 32,
        gat_dropout: float = 0.1,
        # Readout config
        pool_hidden_dim: int = 128,
        pred_hidden_dims: list = [256, 128],
        pred_dropout: float = 0.1,
    ):
        super().__init__()

        # Stage 1: Per-station encoders
        self.waveform_encoder = ResNet1DEncoder(
            input_channels=waveform_channels,
            channels=encoder_channels,
        )
        self.geometry_encoder = GeometryEncoder(
            input_dim=geometry_input_dim,
            embed_dim=geometry_embed_dim,
        )

        # Edge feature projection
        self.edge_encoder = nn.Sequential(
            nn.Linear(edge_feature_dim, edge_embed_dim),
            nn.ReLU(),
        )

        # Total node feature dim
        node_dim = encoder_channels[-1] + geometry_embed_dim  # 256 + 64 = 320

        # Stage 2: GATv2 stack
        self.gat_stack = FocalGATStack(
            in_channels=node_dim,
            hidden_channels=gat_hidden_dim,
            num_layers=gat_num_layers,
            edge_dim=edge_embed_dim,
            heads=gat_heads,
            dropout=gat_dropout,
        )

        # Stage 3: Readout
        self.readout = FocalMechanismReadout(
            in_channels=gat_hidden_dim,
            pool_hidden_dim=pool_hidden_dim,
            pred_hidden_dims=pred_hidden_dims,
            dropout=pred_dropout,
        )

    def forward(self, data):
        """
        Args:
            data: PyG Data/Batch object with attributes:
                - waveform: (N, 3, T) station waveforms
                - geometry: (N, 7) source-station geometry
                - edge_index: (2, E) edge connectivity
                - edge_attr: (E, edge_feat_dim) raw edge features
                - batch: (N,) graph assignment
        Returns:
            dict with:
                - mt_mean: (B, 6) moment tensor prediction
                - mt_logvar: (B, 6) log-variance (uncertainty)
                - gate_weights: (N, 1) station importance weights
        """
        # Stage 1: Encode per-station features
        waveform_embed = self.waveform_encoder(data.waveform)  # (N, 256)
        geometry_embed = self.geometry_encoder(data.geometry)   # (N, 64)

        # Concatenate node features
        node_features = torch.cat([waveform_embed, geometry_embed], dim=-1)  # (N, 320)

        # Encode edge features
        edge_features = self.edge_encoder(data.edge_attr)  # (E, 32)

        # Stage 2: GATv2 message passing
        node_features = self.gat_stack(
            node_features, data.edge_index, edge_features
        )  # (N, 320)

        # Stage 3: Readout and prediction
        mt_mean, mt_logvar, gate_weights = self.readout(
            node_features, data.batch
        )

        return {
            'mt_mean': mt_mean,
            'mt_logvar': mt_logvar,
            'gate_weights': gate_weights,
        }

    def predict_with_uncertainty(self, data, num_samples: int = 50):
        """
        MC Dropout inference for epistemic uncertainty estimation.
        
        Args:
            data: PyG Data/Batch object
            num_samples: number of stochastic forward passes
        Returns:
            dict with:
                - mt_mean: (B, 6) mean prediction across samples
                - mt_aleatoric: (B, 6) mean aleatoric uncertainty
                - mt_epistemic: (B, 6) epistemic uncertainty (variance of means)
                - mt_total: (B, 6) total uncertainty
        """
        self.train()  # Enable dropout
        
        means = []
        logvars = []

        with torch.no_grad():
            for _ in range(num_samples):
                output = self.forward(data)
                means.append(output['mt_mean'])
                logvars.append(output['mt_logvar'])

        means = torch.stack(means, dim=0)      # (T, B, 6)
        logvars = torch.stack(logvars, dim=0)  # (T, B, 6)

        # Predictive mean
        mt_mean = means.mean(dim=0)  # (B, 6)

        # Aleatoric uncertainty (mean of predicted variances)
        mt_aleatoric = logvars.exp().mean(dim=0)  # (B, 6)

        # Epistemic uncertainty (variance of predicted means)
        mt_epistemic = means.var(dim=0)  # (B, 6)

        # Total uncertainty
        mt_total = mt_aleatoric + mt_epistemic  # (B, 6)

        self.eval()

        return {
            'mt_mean': mt_mean,
            'mt_aleatoric': mt_aleatoric,
            'mt_epistemic': mt_epistemic,
            'mt_total': mt_total,
        }

    @property
    def num_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
