"""
GATv2 layers with edge feature incorporation for FocalGNN.
Implements physics-informed attention where edge features 
(azimuthal separation, take-off angle difference) influence attention weights.
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import MessagePassing
from torch_geometric.utils import softmax


class GATv2ConvEdge(MessagePassing):
    """
    GATv2 convolution with edge feature incorporation.
    
    Attention is computed as:
        alpha_ij = softmax_j(a^T * LeakyReLU(W_l*x_i || W_r*x_j || W_e*e_ij))
    
    This allows edge features (physics-informed: delta_azimuth, delta_takeoff)
    to directly influence which station pairs communicate most.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        edge_dim: int,
        heads: int = 4,
        dropout: float = 0.1,
        negative_slope: float = 0.2,
    ):
        super().__init__(aggr='add', node_dim=0)
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.heads = heads
        self.head_dim = out_channels // heads
        self.dropout = dropout
        self.negative_slope = negative_slope

        # Linear projections
        self.W_l = nn.Linear(in_channels, out_channels, bias=False)  # left node
        self.W_r = nn.Linear(in_channels, out_channels, bias=False)  # right node
        self.W_e = nn.Linear(edge_dim, out_channels, bias=False)     # edge features
        self.W_v = nn.Linear(in_channels, out_channels, bias=False)  # value projection

        # Attention vector (one per head)
        self.att = nn.Parameter(torch.Tensor(heads, 3 * self.head_dim))

        # Output bias
        self.bias = nn.Parameter(torch.Tensor(out_channels))

        self.reset_parameters()

    def reset_parameters(self):
        nn.init.xavier_uniform_(self.W_l.weight)
        nn.init.xavier_uniform_(self.W_r.weight)
        nn.init.xavier_uniform_(self.W_e.weight)
        nn.init.xavier_uniform_(self.W_v.weight)
        nn.init.xavier_uniform_(self.att.unsqueeze(0))
        nn.init.zeros_(self.bias)

    def forward(self, x, edge_index, edge_attr):
        """
        Args:
            x: (N, in_channels) node features
            edge_index: (2, E) edge indices
            edge_attr: (E, edge_dim) edge features
        Returns:
            out: (N, out_channels) updated node features
        """
        # Project nodes and edges
        x_l = self.W_l(x)  # (N, out_channels)
        x_r = self.W_r(x)  # (N, out_channels)
        x_v = self.W_v(x)  # (N, out_channels)
        e = self.W_e(edge_attr)  # (E, out_channels)

        # Propagate
        out = self.propagate(edge_index, x_l=x_l, x_r=x_r, x_v=x_v, edge_feat=e)
        out = out + self.bias
        return out

    def message(self, x_l_i, x_r_j, x_v_j, edge_feat, index, ptr, size_i):
        """
        Compute attention-weighted messages.
        
        x_l_i: left projection of target nodes (E, out_channels)
        x_r_j: right projection of source nodes (E, out_channels)
        x_v_j: value projection of source nodes (E, out_channels)
        edge_feat: projected edge features (E, out_channels)
        """
        # Reshape for multi-head attention
        E = x_l_i.size(0)
        x_l_i = x_l_i.view(E, self.heads, self.head_dim)
        x_r_j = x_r_j.view(E, self.heads, self.head_dim)
        edge_feat = edge_feat.view(E, self.heads, self.head_dim)
        x_v_j = x_v_j.view(E, self.heads, self.head_dim)

        # GATv2: apply nonlinearity BEFORE dot product with attention vector
        # Concatenate: [W_l*x_i || W_r*x_j || W_e*e_ij]
        cat = torch.cat([x_l_i, x_r_j, edge_feat], dim=-1)  # (E, heads, 3*head_dim)
        cat = F.leaky_relu(cat, negative_slope=self.negative_slope)

        # Dot product with attention vector
        alpha = (cat * self.att.unsqueeze(0)).sum(dim=-1)  # (E, heads)

        # Softmax over neighbors
        alpha = softmax(alpha, index, ptr, size_i)

        # Dropout on attention weights
        alpha = F.dropout(alpha, p=self.dropout, training=self.training)

        # Weighted message
        out = x_v_j * alpha.unsqueeze(-1)  # (E, heads, head_dim)
        return out.view(E, self.heads * self.head_dim)


class FocalGATBlock(nn.Module):
    """
    A single GAT block with residual connection, layer norm, and dropout.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        edge_dim: int,
        heads: int = 4,
        dropout: float = 0.1,
        residual: bool = True,
        layer_norm: bool = True,
    ):
        super().__init__()
        self.gat = GATv2ConvEdge(in_channels, out_channels, edge_dim, heads, dropout)
        self.residual = residual
        self.layer_norm = layer_norm
        self.dropout = nn.Dropout(dropout)

        if layer_norm:
            self.norm = nn.LayerNorm(out_channels)

        if residual and in_channels != out_channels:
            self.residual_proj = nn.Linear(in_channels, out_channels, bias=False)
        else:
            self.residual_proj = None

    def forward(self, x, edge_index, edge_attr):
        """
        Args:
            x: (N, in_channels) node features
            edge_index: (2, E) edge indices
            edge_attr: (E, edge_dim) edge features
        Returns:
            out: (N, out_channels) updated node features
        """
        h = self.gat(x, edge_index, edge_attr)
        h = self.dropout(h)

        # Residual connection
        if self.residual:
            if self.residual_proj is not None:
                x = self.residual_proj(x)
            h = h + x

        # Layer normalization
        if self.layer_norm:
            h = self.norm(h)

        h = F.relu(h)
        return h


class FocalGATStack(nn.Module):
    """
    Stack of GATv2 blocks for FocalGNN.
    Processes station embeddings with physics-informed edges.
    """

    def __init__(
        self,
        in_channels: int = 320,
        hidden_channels: int = 320,
        num_layers: int = 3,
        edge_dim: int = 32,
        heads: int = 4,
        dropout: float = 0.1,
        residual: bool = True,
        layer_norm: bool = True,
    ):
        super().__init__()
        self.layers = nn.ModuleList()

        # First layer
        self.layers.append(FocalGATBlock(
            in_channels, hidden_channels, edge_dim, heads, dropout, residual, layer_norm
        ))

        # Hidden layers
        for _ in range(num_layers - 1):
            self.layers.append(FocalGATBlock(
                hidden_channels, hidden_channels, edge_dim, heads, dropout, residual, layer_norm
            ))

    def forward(self, x, edge_index, edge_attr):
        """
        Args:
            x: (N, in_channels) initial node features
            edge_index: (2, E) edge indices
            edge_attr: (E, edge_dim) edge features
        Returns:
            x: (N, hidden_channels) context-enriched node features
            attention_weights: list of attention weight tensors per layer (for interpretability)
        """
        for layer in self.layers:
            x = layer(x, edge_index, edge_attr)
        return x
