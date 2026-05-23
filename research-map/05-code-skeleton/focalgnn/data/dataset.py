"""
PyTorch Geometric Dataset for FocalGNN.
Constructs per-event graphs with station nodes and physics-informed edges.
"""

import numpy as np
import h5py
import torch
from torch.utils.data import Dataset
from torch_geometric.data import Data, Batch
from .graph_builder import build_physics_graph


class FocalMechanismDataset(Dataset):
    """
    Dataset for earthquake focal mechanism estimation.
    
    Each sample is one earthquake event represented as a graph:
    - Nodes: recording stations
    - Node features: waveform (3, T) + geometry (7,)
    - Edges: fully connected with physics-informed features
    - Label: moment tensor (6,)
    """

    def __init__(
        self,
        h5_path: str,
        split: str = 'train',
        min_stations: int = 8,
        max_stations: int = 50,
        augment: bool = True,
        station_dropout_rate: tuple = (0.1, 0.5),
        noise_snr_range: tuple = (5.0, 50.0),
        time_shift_max: float = 0.5,
    ):
        """
        Args:
            h5_path: Path to preprocessed HDF5 file
            split: 'train', 'val', or 'test'
            min_stations: Minimum stations to keep after dropout
            max_stations: Maximum stations (subsample if more)
            augment: Whether to apply augmentation
            station_dropout_rate: (min, max) fraction of stations to drop
            noise_snr_range: SNR range for noise augmentation (dB)
            time_shift_max: Maximum time shift in seconds
        """
        self.h5_path = h5_path
        self.split = split
        self.min_stations = min_stations
        self.max_stations = max_stations
        self.augment = augment and (split == 'train')
        self.station_dropout_rate = station_dropout_rate
        self.noise_snr_range = noise_snr_range
        self.time_shift_max = time_shift_max

        # Load event index
        with h5py.File(h5_path, 'r') as f:
            self.event_ids = list(f[split].keys())

    def __len__(self):
        return len(self.event_ids)

    def __getitem__(self, idx):
        """
        Returns a PyG Data object representing one earthquake event as a graph.
        """
        event_id = self.event_ids[idx]

        with h5py.File(self.h5_path, 'r') as f:
            event_group = f[self.split][event_id]

            # Waveforms: (N_stations, 3, T)
            waveforms = event_group['waveforms'][:]

            # Geometry: (N_stations, 7) - [az, to, dist, cos_az, sin_az, cos_to, sin_to]
            geometry = event_group['geometry'][:]

            # Labels: moment tensor (6,)
            moment_tensor = event_group['moment_tensor'][:]

            # Polarities: (N_stations,) - first motion polarity (+1/-1/0=unknown)
            polarities = event_group.get('polarities', None)
            if polarities is not None:
                polarities = polarities[:]

        N_stations = waveforms.shape[0]

        # Station subsampling (if too many)
        if N_stations > self.max_stations:
            indices = np.random.choice(N_stations, self.max_stations, replace=False)
            waveforms = waveforms[indices]
            geometry = geometry[indices]
            if polarities is not None:
                polarities = polarities[indices]
            N_stations = self.max_stations

        # Augmentation
        if self.augment:
            waveforms, geometry, polarities, N_stations = self._augment(
                waveforms, geometry, polarities, N_stations
            )

        # Build physics-informed graph
        edge_index, edge_attr = build_physics_graph(geometry)

        # Convert to tensors
        data = Data(
            waveform=torch.tensor(waveforms, dtype=torch.float32),
            geometry=torch.tensor(geometry, dtype=torch.float32),
            edge_index=torch.tensor(edge_index, dtype=torch.long),
            edge_attr=torch.tensor(edge_attr, dtype=torch.float32),
            y=torch.tensor(moment_tensor, dtype=torch.float32),
            num_nodes=N_stations,
        )

        if polarities is not None:
            data.polarities = torch.tensor(polarities, dtype=torch.float32)

        return data

    def _augment(self, waveforms, geometry, polarities, N):
        """Apply data augmentation."""

        # 1. Station dropout
        if N > self.min_stations:
            drop_rate = np.random.uniform(*self.station_dropout_rate)
            keep_n = max(self.min_stations, int(N * (1 - drop_rate)))
            if keep_n < N:
                indices = np.random.choice(N, keep_n, replace=False)
                waveforms = waveforms[indices]
                geometry = geometry[indices]
                if polarities is not None:
                    polarities = polarities[indices]
                N = keep_n

        # 2. Noise addition
        snr_db = np.random.uniform(*self.noise_snr_range)
        snr_linear = 10 ** (snr_db / 20)
        noise = np.random.randn(*waveforms.shape)
        signal_power = np.sqrt(np.mean(waveforms ** 2, axis=-1, keepdims=True))
        noise_scaled = noise * signal_power / snr_linear
        waveforms = waveforms + noise_scaled

        # 3. Time shift (circular shift)
        max_samples = int(self.time_shift_max * 100)  # 100 Hz
        shift = np.random.randint(-max_samples, max_samples + 1)
        if shift != 0:
            waveforms = np.roll(waveforms, shift, axis=-1)

        return waveforms, geometry, polarities, N


def collate_fn(data_list):
    """Custom collate using PyG Batch for variable-size graphs."""
    return Batch.from_data_list(data_list)
