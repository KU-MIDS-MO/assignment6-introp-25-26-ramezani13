import numpy as np

def random_unit_vectors(num_vectors, dim):

    M = np.random.randn(num_vectors, dim)

    U = np.zeros((num_vectors, dim), dtype=float)

    for i in range(num_vectors):

        total = 0.0
        for j in range(dim):
            total += M[i, j] * M[i, j]   # sum of squares
        l2_norm = np.sqrt(total)

        if l2_norm == 0:
            l2_norm = 1.0

        for j in range(dim):
            U[i, j] = M[i, j] / l2_norm

    return U

