"""
Focal mechanism utility functions.
Conversions between moment tensor, strike/dip/rake, and related computations.
"""

import numpy as np
from scipy.linalg import eigh


def mt6_to_matrix(mt6):
    """
    Convert 6-component moment tensor to 3x3 symmetric matrix.
    
    Args:
        mt6: (6,) array [Mxx, Myy, Mzz, Mxy, Mxz, Myz]
    Returns:
        M: (3, 3) symmetric moment tensor matrix
    """
    M = np.zeros((3, 3))
    M[0, 0] = mt6[0]  # Mxx
    M[1, 1] = mt6[1]  # Myy
    M[2, 2] = mt6[2]  # Mzz
    M[0, 1] = M[1, 0] = mt6[3]  # Mxy
    M[0, 2] = M[2, 0] = mt6[4]  # Mxz
    M[1, 2] = M[2, 1] = mt6[5]  # Myz
    return M


def matrix_to_mt6(M):
    """
    Convert 3x3 moment tensor matrix to 6-component vector.
    
    Args:
        M: (3, 3) symmetric matrix
    Returns:
        mt6: (6,) array [Mxx, Myy, Mzz, Mxy, Mxz, Myz]
    """
    return np.array([M[0, 0], M[1, 1], M[2, 2], M[0, 1], M[0, 2], M[1, 2]])


def sdr_to_mt6(strike, dip, rake, scalar_moment=1.0):
    """
    Convert strike/dip/rake to 6-component moment tensor.
    Uses Aki & Richards (2002) convention.
    
    Args:
        strike: strike angle (degrees, 0-360)
        dip: dip angle (degrees, 0-90)
        rake: rake angle (degrees, -180 to 180)
        scalar_moment: scalar seismic moment (default 1.0 for unit tensor)
    Returns:
        mt6: (6,) array [Mxx, Myy, Mzz, Mxy, Mxz, Myz]
    """
    s = np.radians(strike)
    d = np.radians(dip)
    r = np.radians(rake)

    # Moment tensor components (Aki & Richards, NED convention)
    Mxx = -scalar_moment * (np.sin(d) * np.cos(r) * np.sin(2*s) + 
                             np.sin(2*d) * np.sin(r) * np.sin(s)**2)
    Myy = scalar_moment * (np.sin(d) * np.cos(r) * np.sin(2*s) - 
                            np.sin(2*d) * np.sin(r) * np.cos(s)**2)
    Mzz = scalar_moment * np.sin(2*d) * np.sin(r)
    Mxy = scalar_moment * (np.sin(d) * np.cos(r) * np.cos(2*s) + 
                            0.5 * np.sin(2*d) * np.sin(r) * np.sin(2*s))
    Mxz = -scalar_moment * (np.cos(d) * np.cos(r) * np.cos(s) + 
                              np.cos(2*d) * np.sin(r) * np.sin(s))
    Myz = -scalar_moment * (np.cos(d) * np.cos(r) * np.sin(s) - 
                              np.cos(2*d) * np.sin(r) * np.cos(s))

    return np.array([Mxx, Myy, Mzz, Mxy, Mxz, Myz])


def mt6_to_sdr(mt6):
    """
    Convert 6-component moment tensor to strike/dip/rake.
    Decomposes MT into best double-couple and returns both nodal planes.
    
    Args:
        mt6: (6,) array [Mxx, Myy, Mzz, Mxy, Mxz, Myz]
    Returns:
        (strike1, dip1, rake1): first nodal plane (degrees)
        (strike2, dip2, rake2): second nodal plane (degrees)
    """
    M = mt6_to_matrix(mt6)
    
    # Eigendecomposition
    eigenvalues, eigenvectors = eigh(M)
    
    # Sort by absolute value (T, N, P axes)
    idx = np.argsort(np.abs(eigenvalues))
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    
    # P and T axes (largest positive = T, largest negative = P)
    if eigenvalues[2] > 0:
        t_axis = eigenvectors[:, 2]
        p_axis = eigenvectors[:, 0]
    else:
        t_axis = eigenvectors[:, 0]
        p_axis = eigenvectors[:, 2]
    
    # Fault normal and slip vectors
    n1 = (t_axis + p_axis) / np.sqrt(2)
    s1 = (t_axis - p_axis) / np.sqrt(2)
    
    # Ensure fault normal points up (convention)
    if n1[2] < 0:
        n1 = -n1
        s1 = -s1
    
    # Convert to strike/dip/rake
    strike1, dip1, rake1 = _normal_slip_to_sdr(n1, s1)
    
    # Second nodal plane
    n2 = s1.copy()
    s2 = n1.copy()
    if n2[2] < 0:
        n2 = -n2
        s2 = -s2
    strike2, dip2, rake2 = _normal_slip_to_sdr(n2, s2)
    
    return (strike1, dip1, rake1), (strike2, dip2, rake2)


def _normal_slip_to_sdr(normal, slip):
    """Convert fault normal and slip vectors to strike/dip/rake."""
    # Dip
    dip = np.degrees(np.arccos(abs(normal[2])))
    
    # Strike
    if abs(normal[2]) > 0.999:
        # Nearly horizontal fault
        strike = 0.0
    else:
        strike = np.degrees(np.arctan2(-normal[0], normal[1]))
    
    if strike < 0:
        strike += 360.0
    
    # Rake
    # Project slip onto fault plane
    strike_dir = np.array([np.cos(np.radians(strike)), np.sin(np.radians(strike)), 0])
    dip_dir = np.cross(normal, strike_dir)
    
    rake = np.degrees(np.arctan2(
        np.dot(slip, dip_dir),
        np.dot(slip, strike_dir)
    ))
    
    return strike, dip, rake


def kagan_angle(mt1, mt2):
    """
    Compute Kagan angle between two moment tensors.
    
    The Kagan angle is the minimum rotation angle needed to rotate
    one double-couple mechanism into another (considering both nodal planes).
    Range: [0, 120] degrees.
    
    Args:
        mt1: (6,) first moment tensor
        mt2: (6,) second moment tensor
    Returns:
        angle: Kagan angle in degrees
    """
    M1 = mt6_to_matrix(mt1)
    M2 = mt6_to_matrix(mt2)
    
    # Normalize
    M1 = M1 / np.sqrt(np.sum(M1**2) / 2)
    M2 = M2 / np.sqrt(np.sum(M2**2) / 2)
    
    # Get rotation quaternions for both tensors
    q1s = _mt_to_quaternions(M1)
    q2s = _mt_to_quaternions(M2)
    
    # Minimum angle over all equivalent orientations
    min_angle = 180.0
    for q1 in q1s:
        for q2 in q2s:
            angle = _quaternion_angle(q1, q2)
            min_angle = min(min_angle, angle)
    
    return min_angle


def _mt_to_quaternions(M):
    """
    Get equivalent quaternion representations of a moment tensor.
    A DC source has 4 equivalent representations due to nodal plane ambiguity.
    """
    eigenvalues, eigenvectors = eigh(M)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    
    # Generate 4 equivalent rotation matrices
    quaternions = []
    for signs in [(1, 1, 1), (-1, -1, 1), (-1, 1, -1), (1, -1, -1)]:
        R = eigenvectors.copy()
        for i, s in enumerate(signs):
            R[:, i] *= s
        if np.linalg.det(R) < 0:
            R = -R
        q = _rotation_to_quaternion(R)
        quaternions.append(q)
    
    return quaternions


def _rotation_to_quaternion(R):
    """Convert 3x3 rotation matrix to unit quaternion."""
    trace = R[0, 0] + R[1, 1] + R[2, 2]
    
    if trace > 0:
        s = 0.5 / np.sqrt(trace + 1.0)
        w = 0.25 / s
        x = (R[2, 1] - R[1, 2]) * s
        y = (R[0, 2] - R[2, 0]) * s
        z = (R[1, 0] - R[0, 1]) * s
    else:
        if R[0, 0] > R[1, 1] and R[0, 0] > R[2, 2]:
            s = 2.0 * np.sqrt(1.0 + R[0, 0] - R[1, 1] - R[2, 2])
            w = (R[2, 1] - R[1, 2]) / s
            x = 0.25 * s
            y = (R[0, 1] + R[1, 0]) / s
            z = (R[0, 2] + R[2, 0]) / s
        elif R[1, 1] > R[2, 2]:
            s = 2.0 * np.sqrt(1.0 + R[1, 1] - R[0, 0] - R[2, 2])
            w = (R[0, 2] - R[2, 0]) / s
            x = (R[0, 1] + R[1, 0]) / s
            y = 0.25 * s
            z = (R[1, 2] + R[2, 1]) / s
        else:
            s = 2.0 * np.sqrt(1.0 + R[2, 2] - R[0, 0] - R[1, 1])
            w = (R[1, 0] - R[0, 1]) / s
            x = (R[0, 2] + R[2, 0]) / s
            y = (R[1, 2] + R[2, 1]) / s
            z = 0.25 * s
    
    return np.array([w, x, y, z])


def _quaternion_angle(q1, q2):
    """Compute angle between two unit quaternions in degrees."""
    dot = abs(np.dot(q1, q2))
    dot = min(dot, 1.0)
    angle = 2.0 * np.degrees(np.arccos(dot))
    return angle


def classify_fault_type(strike, dip, rake):
    """
    Classify focal mechanism into fault type.
    
    Args:
        strike, dip, rake: in degrees
    Returns:
        str: 'normal', 'reverse', 'strike_slip', or 'oblique'
    """
    rake_abs = abs(rake)
    
    if rake_abs < 30 or rake_abs > 150:
        return 'strike_slip'
    elif 60 <= rake_abs <= 120:
        if rake > 0:
            return 'reverse'
        else:
            return 'normal'
    else:
        return 'oblique'


def batch_kagan_angle(mt_pred, mt_true):
    """
    Compute Kagan angles for a batch of predictions.
    
    Args:
        mt_pred: (B, 6) predicted moment tensors
        mt_true: (B, 6) true moment tensors
    Returns:
        angles: (B,) Kagan angles in degrees
    """
    B = mt_pred.shape[0]
    angles = np.zeros(B)
    for i in range(B):
        angles[i] = kagan_angle(mt_pred[i], mt_true[i])
    return angles
