import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    x = np.asarray(x, dtype=float)
    p = np.asarray(p, dtype=float)
    
    # Step 0. Validate all probabilities sum up to 1
    if not np.allclose(p.sum(), 1.0):
        raise ValueError("Probabilities do not add up to 1")

    # Check if array have the same size
    if not len(x) == len(p):
        raise ValueError("Not same size")

    return np.sum(x * p)