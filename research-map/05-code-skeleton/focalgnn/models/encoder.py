"""
Per-station 1D ResNet Encoder for seismic waveforms.
Shared weights across all stations in the network.
"""

import torch
import torch.nn as nn


class ResBlock1D(nn.Module):
    """1D Residual Block with optional downsampling."""

    def __init__(self, in_channels, out_channels, kernel_size=3, stride=1):
        super().__init__()
        self.conv1 = nn.Conv1d(in_channels, out_channels, kernel_size,
                               stride=stride, padding=kernel_size // 2, bias=False)
        self.bn1 = nn.BatchNorm1d(out_channels)
        self.conv2 = nn.Conv1d(out_channels, out_channels, kernel_size,
                               stride=1, padding=kernel_size // 2, bias=False)
        self.bn2 = nn.BatchNorm1d(out_channels)
        self.relu = nn.ReLU(inplace=True)

        # Shortcut connection
        self.shortcut = nn.Sequential()
        if stride != 1 or in_channels != out_channels:
            self.shortcut = nn.Sequential(
                nn.Conv1d(in_channels, out_channels, 1, stride=stride, bias=False),
                nn.BatchNorm1d(out_channels)
            )

    def forward(self, x):
        residual = self.shortcut(x)
        out = self.relu(self.bn1(self.conv1(x)))
        out = self.bn2(self.conv2(out))
        out += residual
        out = self.relu(out)
        return out


class ResNet1DEncoder(nn.Module):
    """
    1D ResNet-18 adapted for 3-component seismic waveforms.
    
    Input: (batch, 3, T) - 3-component waveform
    Output: (batch, embed_dim) - station embedding
    """

    def __init__(
        self,
        input_channels: int = 3,
        layers: list = [2, 2, 2, 2],
        channels: list = [32, 64, 128, 256],
        first_kernel_size: int = 7,
        first_stride: int = 2,
        kernel_size: int = 3,
    ):
        super().__init__()
        self.embed_dim = channels[-1]

        # Initial convolution
        self.conv1 = nn.Conv1d(input_channels, channels[0], first_kernel_size,
                               stride=first_stride, padding=first_kernel_size // 2, bias=False)
        self.bn1 = nn.BatchNorm1d(channels[0])
        self.relu = nn.ReLU(inplace=True)

        # Residual layers
        self.layer1 = self._make_layer(channels[0], channels[0], layers[0], kernel_size, stride=1)
        self.layer2 = self._make_layer(channels[0], channels[1], layers[1], kernel_size, stride=2)
        self.layer3 = self._make_layer(channels[1], channels[2], layers[2], kernel_size, stride=2)
        self.layer4 = self._make_layer(channels[2], channels[3], layers[3], kernel_size, stride=2)

        # Global average pooling
        self.global_pool = nn.AdaptiveAvgPool1d(1)

    def _make_layer(self, in_channels, out_channels, num_blocks, kernel_size, stride):
        layers = [ResBlock1D(in_channels, out_channels, kernel_size, stride)]
        for _ in range(1, num_blocks):
            layers.append(ResBlock1D(out_channels, out_channels, kernel_size, stride=1))
        return nn.Sequential(*layers)

    def forward(self, x):
        """
        Args:
            x: (batch, 3, T) waveform tensor
        Returns:
            h: (batch, embed_dim) station embedding
        """
        x = self.relu(self.bn1(self.conv1(x)))  # (B, 32, T/2)
        x = self.layer1(x)  # (B, 32, T/2)
        x = self.layer2(x)  # (B, 64, T/4)
        x = self.layer3(x)  # (B, 128, T/8)
        x = self.layer4(x)  # (B, 256, T/16)
        x = self.global_pool(x)  # (B, 256, 1)
        x = x.squeeze(-1)  # (B, 256)
        return x


class GeometryEncoder(nn.Module):
    """
    Encode source-station geometry (azimuth, take-off angle, distance)
    into a fixed-size embedding.
    """

    def __init__(self, input_dim: int = 7, embed_dim: int = 64):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.ReLU(),
            nn.Linear(32, embed_dim),
            nn.ReLU(),
        )

    def forward(self, geometry):
        """
        Args:
            geometry: (batch, 7) - [az, to, dist, cos_az, sin_az, cos_to, sin_to]
        Returns:
            geo_embed: (batch, embed_dim)
        """
        return self.mlp(geometry)
