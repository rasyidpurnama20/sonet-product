"""
Baseline models for comparison with FocalGNN.

B2: Single-CNN - per-station prediction, then average
B3: Multi-CNN-Concat - concatenate all station waveforms
B4: Transformer-style - attention over stations (TEAM-like)
B5: GNN-Distance - GNN with distance-only edges (no physics-informed features)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import global_mean_pool

from .encoder import ResNet1DEncoder, GeometryEncoder
from .gat_layers import FocalGATStack
from .readout import MomentTensorHead, AttentionPooling


class SingleCNNBaseline(nn.Module):
    """
    B2: Per-station CNN prediction, then average across stations.
    No inter-station interaction.
    """

    def __init__(self, encoder_channels=[32, 64, 128, 256], pred_hidden=[256, 128]):
        super().__init__()
        self.encoder = ResNet1DEncoder(input_channels=3, channels=encoder_channels)
        self.predictor = MomentTensorHead(
            in_channels=encoder_channels[-1],
            hidden_dims=pred_hidden,
        )

    def forward(self, data):
        """Each station predicts independently, then average."""
        h = self.encoder(data.waveform)  # (N, 256)
        mt_mean, mt_logvar = self.predictor(h)  # (N, 6), (N, 6)

        # Average per graph
        batch = data.batch
        num_graphs = batch.max().item() + 1

        mt_mean_avg = torch.zeros(num_graphs, 6, device=h.device)
        mt_logvar_avg = torch.zeros(num_graphs, 6, device=h.device)
        counts = torch.zeros(num_graphs, 1, device=h.device)

        mt_mean_avg.scatter_add_(0, batch.unsqueeze(1).expand_as(mt_mean), mt_mean)
        mt_logvar_avg.scatter_add_(0, batch.unsqueeze(1).expand_as(mt_logvar), mt_logvar)
        counts.scatter_add_(0, batch.unsqueeze(1), torch.ones_like(batch.unsqueeze(1).float()))

        mt_mean_avg = mt_mean_avg / counts
        mt_logvar_avg = mt_logvar_avg / counts

        return {
            'mt_mean': mt_mean_avg,
            'mt_logvar': mt_logvar_avg,
            'gate_weights': None,
        }


class TransformerBaseline(nn.Module):
    """
    B4: Transformer-style multi-station model (similar to TEAM).
    Self-attention over stations without explicit graph structure.
    """

    def __init__(
        self,
        encoder_channels=[32, 64, 128, 256],
        geometry_dim=7,
        geometry_embed=64,
        d_model=320,
        nhead=4,
        num_layers=3,
        dropout=0.1,
    ):
        super().__init__()
        self.encoder = ResNet1DEncoder(input_channels=3, channels=encoder_channels)
        self.geo_encoder = GeometryEncoder(input_dim=geometry_dim, embed_dim=geometry_embed)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=d_model * 4,
            dropout=dropout,
            batch_first=True,
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        self.predictor = MomentTensorHead(d_model, [256, 128], dropout)

    def forward(self, data):
        """
        Process stations with self-attention.
        Note: Requires padding to handle variable-length sequences per graph.
        """
        # Encode per station
        wave_embed = self.encoder(data.waveform)  # (N_total, 256)
        geo_embed = self.geo_encoder(data.geometry)  # (N_total, 64)
        node_feat = torch.cat([wave_embed, geo_embed], dim=-1)  # (N_total, 320)

        # Reconstruct per-graph sequences (pad to max length)
        batch = data.batch
        num_graphs = batch.max().item() + 1
        max_nodes = 0
        graphs = []

        for i in range(num_graphs):
            mask = batch == i
            graphs.append(node_feat[mask])
            max_nodes = max(max_nodes, mask.sum().item())

        # Pad and stack
        padded = torch.zeros(num_graphs, max_nodes, node_feat.size(1), device=node_feat.device)
        padding_mask = torch.ones(num_graphs, max_nodes, dtype=torch.bool, device=node_feat.device)

        for i, g in enumerate(graphs):
            padded[i, :g.size(0)] = g
            padding_mask[i, :g.size(0)] = False

        # Transformer
        out = self.transformer(padded, src_key_padding_mask=padding_mask)  # (B, max_N, d_model)

        # Mean pool (excluding padding)
        mask_expanded = (~padding_mask).unsqueeze(-1).float()
        z = (out * mask_expanded).sum(dim=1) / mask_expanded.sum(dim=1).clamp(min=1)

        # Predict
        mt_mean, mt_logvar = self.predictor(z)

        return {
            'mt_mean': mt_mean,
            'mt_logvar': mt_logvar,
            'gate_weights': None,
        }


class GNNDistanceBaseline(nn.Module):
    """
    B5: GNN with distance-only edges (no physics-informed features).
    Same architecture as FocalGNN but edge features are only inter-station distance.
    Used to isolate the contribution of physics-informed edge features.
    """

    def __init__(
        self,
        encoder_channels=[32, 64, 128, 256],
        geometry_dim=7,
        geometry_embed=64,
        gat_hidden=320,
        gat_layers=3,
        gat_heads=4,
        gat_dropout=0.1,
    ):
        super().__init__()
        self.encoder = ResNet1DEncoder(input_channels=3, channels=encoder_channels)
        self.geo_encoder = GeometryEncoder(input_dim=geometry_dim, embed_dim=geometry_embed)

        # Edge encoder: only distance (1D input)
        self.edge_encoder = nn.Sequential(
            nn.Linear(1, 32),
            nn.ReLU(),
        )

        node_dim = encoder_channels[-1] + geometry_embed
        self.gat_stack = FocalGATStack(
            in_channels=node_dim,
            hidden_channels=gat_hidden,
            num_layers=gat_layers,
            edge_dim=32,
            heads=gat_heads,
            dropout=gat_dropout,
        )
        self.pooling = AttentionPooling(gat_hidden)
        self.predictor = MomentTensorHead(gat_hidden, [256, 128], gat_dropout)

    def forward(self, data):
        wave_embed = self.encoder(data.waveform)
        geo_embed = self.geo_encoder(data.geometry)
        node_feat = torch.cat([wave_embed, geo_embed], dim=-1)

        # Only use distance as edge feature
        edge_dist = data.edge_attr[:, -1:] if data.edge_attr.dim() > 1 else data.edge_attr.unsqueeze(-1)
        edge_feat = self.edge_encoder(edge_dist)

        node_feat = self.gat_stack(node_feat, data.edge_index, edge_feat)
        z, gate_weights = self.pooling(node_feat, data.batch)
        mt_mean, mt_logvar = self.predictor(z)

        return {
            'mt_mean': mt_mean,
            'mt_logvar': mt_logvar,
            'gate_weights': gate_weights,
        }
