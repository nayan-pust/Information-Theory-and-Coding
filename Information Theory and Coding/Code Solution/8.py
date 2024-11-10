import numpy as np
from math import log2

def calculate_entropies(matrix):
    # Convert the matrix to numpy array
    P = np.array([
        [1/8, 1/16, 1/32, 1/32],
        [1/16, 1/8, 1/32, 1/32],
        [1/16, 1/16, 1/16, 1/16],
        [1/4, 0, 0, 0]
    ])
    
    # Calculate marginal probabilities
    px = P.sum(axis=0)  # P(X)
    py = P.sum(axis=1)  # P(Y)
    
    # Joint Entropy H(X,Y)
    joint_entropy = 0
    for i in range(4):
        for j in range(4):
            if P[i,j] > 0:  # Avoid log(0)
                joint_entropy -= P[i,j] * log2(P[i,j])
    
    # Calculate H(X) and H(Y)
    hx = -sum(p * log2(p) for p in px if p > 0)
    hy = -sum(p * log2(p) for p in py if p > 0)
    
    # Calculate conditional entropies
    # H(Y|X) = H(X,Y) - H(X)
    hy_given_x = joint_entropy - hx
    # H(X|Y) = H(X,Y) - H(Y)
    hx_given_y = joint_entropy - hy
    
    # Calculate mutual information
    # I(X;Y) = H(X) + H(Y) - H(X,Y)
    mutual_info = hx + hy - joint_entropy
    
    return {
        'Joint_Entropy': joint_entropy,
        'H(X)': hx,
        'H(Y)': hy,
        'H(Y|X)': hy_given_x,
        'H(X|Y)': hx_given_y,
        'Mutual_Information': mutual_info
    }

# Calculate and print results
results = calculate_entropies(None)  # Matrix is hardcoded in the function
for metric, value in results.items():
    print(f"{metric}: {value:.3f}")