"""
Physics-informed graph construction for FocalGNN.

Constructs edges between seismic stations with features that encode
the geometric relationship relevant to focal mechanism estimation:
- Azimuthal separation (most critical for FM resolution)
- Take-off angle difference
- Inter-station distance
"""

import numpy as np
from itertools import combinations


def build_physics_graph(
    geometry: np.ndarray,
    connection: str = "fully_connected",
    knn_k: int = 15,
    distance_threshold_km: float = 200.0,
):
    """
    Build a physics-informed graph from station geometry.
    
    Args:
        geometry: (N, 7) array with columns:
            [azimuth, takeoff, distance, cos_az, sin_az, cos_to, sin_to]
            - azimuth: source-to-station azimuth (degrees or radians)
            - takeoff: take-off angle from source (degrees or radians)
            - distance: epicentral distance (km, normalized)
            - cos_az, sin_az: circular encoding of azimuth
            - cos_to, sin_to: circular encoding of take-off angle
        connection: graph connectivity type
            "fully_connected": all pairs connected
            "knn": k-nearest neighbors
            "distance_threshold": connect if closer than threshold
        knn_k: k for knn connection
        distance_threshold_km: threshold for distance connection
    
    Returns:
        edge_index: (2, E) source-target pairs
        edge_attr: (E, 5) edge features:
            [delta_azimuth, cos_delta_az, sin_delta_az, delta_takeoff, inter_station_dist]
    """
    N = geometry.shape[0]
    
    if N < 2:
        # Single station: no edges
        return np.zeros((2, 0), dtype=np.int64), np.zeros((0, 5), dtype=np.float32)

    # Extract relevant columns
    azimuth = geometry[:, 0]   # source-to-station azimuth
    takeoff = geometry[:, 1]   # take-off angle
    cos_az = geometry[:, 3]
    sin_az = geometry[:, 4]

    # Build connectivity
    if connection == "fully_connected":
        edges = _fully_connected_edges(N)
    elif connection == "knn":
        edges = _knn_edges(geometry, knn_k)
    elif connection == "distance_threshold":
        edges = _distance_threshold_edges(geometry, distance_threshold_km)
    else:
        raise ValueError(f"Unknown connection type: {connection}")

    # Compute edge features
    edge_attr = _compute_edge_features(edges, azimuth, takeoff, cos_az, sin_az)

    # Convert to numpy arrays
    edge_index = np.array(edges).T  # (2, E)
    edge_attr = np.array(edge_attr, dtype=np.float32)  # (E, 5)

    return edge_index, edge_attr


def _fully_connected_edges(N):
    """Generate all pairs (bidirectional)."""
    edges = []
    for i in range(N):
        for j in range(N):
            if i != j:
                edges.append([i, j])
    return edges


def _knn_edges(geometry, k):
    """k-nearest neighbors based on inter-station distance."""
    from scipy.spatial.distance import cdist
    
    # Use lat/lon proxy (cos_az, sin_az for relative position)
    coords = geometry[:, 3:5]  # cos_az, sin_az as proxy
    dists = cdist(coords, coords)
    
    N = geometry.shape[0]
    k_actual = min(k, N - 1)
    edges = []
    
    for i in range(N):
        # Get k nearest (exclude self)
        sorted_idx = np.argsort(dists[i])
        neighbors = sorted_idx[1:k_actual + 1]
        for j in neighbors:
            edges.append([i, j])
            edges.append([j, i])  # bidirectional
    
    # Remove duplicates
    edges = list(set(tuple(e) for e in edges))
    return [list(e) for e in edges]


def _distance_threshold_edges(geometry, threshold_km):
    """Connect stations within distance threshold."""
    distance = geometry[:, 2]  # epicentral distance (normalized)
    N = geometry.shape[0]
    edges = []
    
    for i in range(N):
        for j in range(i + 1, N):
            # Approximate inter-station distance from geometry
            # This is a simplification; actual implementation should use station coordinates
            d_ij = abs(distance[i] - distance[j])  # placeholder
            if d_ij < threshold_km:
                edges.append([i, j])
                edges.append([j, i])
    
    if not edges:
        # Fallback to fully connected if threshold too strict
        return _fully_connected_edges(N)
    
    return edges


def _compute_edge_features(edges, azimuth, takeoff, cos_az, sin_az):
    """
    Compute physics-informed edge features for each edge.
    
    For focal mechanisms, the azimuthal separation between two stations
    is the most informative quantity: stations 90 degrees apart on the
    focal sphere provide maximally complementary information about nodal planes.
    
    Returns:
        edge_features: list of [delta_az, cos_delta_az, sin_delta_az, delta_to, dist_ij]
    """
    edge_features = []
    
    for src, dst in edges:
        # Azimuthal separation (circular difference)
        delta_az = _circular_difference(azimuth[src], azimuth[dst])
        
        # Take-off angle difference
        delta_to = takeoff[src] - takeoff[dst]
        
        # Inter-station "distance" on focal sphere
        # Using angular distance between two points on unit sphere
        dist_ij = _angular_distance(
            azimuth[src], takeoff[src],
            azimuth[dst], takeoff[dst]
        )
        
        edge_features.append([
            delta_az,
            np.cos(np.radians(delta_az)),
            np.sin(np.radians(delta_az)),
            delta_to,
            dist_ij,
        ])
    
    return edge_features


def _circular_difference(angle1, angle2):
    """
    Compute circular difference between two angles (in degrees).
    Returns value in [-180, 180].
    """
    diff = angle1 - angle2
    # Normalize to [-180, 180]
    diff = ((diff + 180) % 360) - 180
    return diff


def _angular_distance(az1, to1, az2, to2):
    """
    Angular distance between two points on the focal sphere.
    
    Convert (azimuth, takeoff) to Cartesian and compute angle between vectors.
    Uses degrees input.
    """
    az1_r, to1_r = np.radians(az1), np.radians(to1)
    az2_r, to2_r = np.radians(az2), np.radians(to2)
    
    # Convert to Cartesian (spherical coordinates)
    x1 = np.sin(to1_r) * np.cos(az1_r)
    y1 = np.sin(to1_r) * np.sin(az1_r)
    z1 = np.cos(to1_r)
    
    x2 = np.sin(to2_r) * np.cos(az2_r)
    y2 = np.sin(to2_r) * np.sin(az2_r)
    z2 = np.cos(to2_r)
    
    # Dot product = cos(angular distance)
    cos_dist = x1*x2 + y1*y2 + z1*z2
    cos_dist = np.clip(cos_dist, -1.0, 1.0)
    
    return np.degrees(np.arccos(cos_dist))
