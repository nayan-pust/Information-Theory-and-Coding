import numpy as np

def create_transition_matrix(adjacency):
    """Create transition probability matrix from adjacency matrix"""
    P = np.zeros_like(adjacency, dtype=float)
    for i in range(len(adjacency)):
        row_sum = np.sum(adjacency[i])
        if row_sum > 0:
            P[i] = adjacency[i] / row_sum
    return P

def get_stationary_distribution(P):
    """Calculate stationary distribution using eigenvalue method"""
    eigenvals, eigenvecs = np.linalg.eig(P.T)
    # Find eigenvector corresponding to eigenvalue 1
    index = np.argmin(np.abs(eigenvals - 1))
    pi = np.real(eigenvecs[:, index])
    # Normalize to get probability distribution
    return pi / np.sum(pi)

def calculate_entropy_rate(P, pi):
    """Calculate entropy rate using stationary distribution and transition matrix"""
    H = 0
    for i in range(len(P)):
        for j in range(len(P)):
            if P[i,j] > 0:  # Avoid log(0)
                H -= pi[i] * P[i,j] * np.log2(P[i,j])
    return H

# Define the weighted adjacency matrix for the graph
adjacency = np.array([
    [0, 1, 1, 2],  # x₁ connections
    [1, 0, 0, 1],  # x₂ connections
    [1, 0, 0, 1],  # x₃ connections
    [2, 1, 1, 0]   # x₄ connections
])

# Calculate transition probability matrix
P = create_transition_matrix(adjacency)
print("\nTransition Probability Matrix:")
print(np.round(P, 4))

# Calculate stationary distribution
pi = get_stationary_distribution(P)
print("\nStationary Distribution:")
print(np.round(pi, 4))

# Calculate entropy rate
entropy_rate = calculate_entropy_rate(P, pi)
print(f"\nEntropy Rate: {entropy_rate:.2f} bits per step")

