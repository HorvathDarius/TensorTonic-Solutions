import numpy as np

def adam_step(param, grad, m, v, t, lr=1e-3, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    One Adam optimizer update step.
    Return (param_new, m_new, v_new).
    """

    print("Initial:")
    print(param, grad, m, v, t, beta1, beta2)

    print("Vectorize inputs")
    param = np.array(param, dtype=float)
    grad  = np.array(grad, dtype=float)
    m     = np.array(m, dtype=float)
    v     = np.array(v, dtype=float)

    print("Vectorized:")
    print(param, grad, m, v, t, beta1, beta2)
    print(beta1 * m)
    
    # update first moment
    m_new = (beta1 * m) + ((1 - beta1) * grad)
    # # update second moment
    v_new = (beta2 * v) + ((1 - beta2) * grad * grad)

    print("update")
    print(m_new, v_new)
    
    # bias correction
    m_bias = m_new / (1 - pow(beta1, t))
    v_bias = v_new / (1 - pow(beta2, t))

    # Parameter update
    param_new = param - (lr * (m_bias / (np.sqrt(v_bias) + eps)))

    # Return new values
    return (param_new, m_new, v_new)
    