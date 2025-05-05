import numpy as np

def get_matrices(dt):
    F = np.eye(6)
    # Position-velocity coupling
    F[0, 2] = dt
    F[1, 3] = dt
    # Position-acceleration coupling (½·dt²)
    F[0, 4] = 0.5 * dt**2
    F[1, 5] = 0.5 * dt**2
    # Velocity-acceleration coupling
    F[2, 4] = dt
    F[3, 5] = dt

    H_pos = np.zeros((2, 6))
    H_pos[0, 0] = 1
    H_pos[1, 1] = 1

    H_posacc = np.zeros((4, 6))
    # x, y rows
    H_posacc[0, 0] = 1
    H_posacc[1, 1] = 1
    # ax, ay rows
    H_posacc[2, 4] = 1
    H_posacc[3, 5] = 1

    return F, H_pos, H_posacc

