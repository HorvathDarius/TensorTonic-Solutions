def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x = x0
    x = (a * x * x) + (b * x) + c
    
    for i in range(0, steps):
        dfx = (2*a*x)+b
        x = x - lr * dfx    

    return x