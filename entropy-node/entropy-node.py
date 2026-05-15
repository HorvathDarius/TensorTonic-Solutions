import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    # Return 0 for no classes
    if len(y) == 0:
        return 0.0

    # Get items counts
    _, counts = np.unique(y, return_counts=True)
    # Calculate percentage of each class
    probabilities = counts / len(y)
    
    # log2(0) is undefined, but 0 * log2(0) = 0 by convention.
    # Filtering zero probabilities avoids the warning.
    probabilities = probabilities[probabilities > 0]

    # Entropy formula
    return -np.sum(probabilities * np.log2(probabilities))