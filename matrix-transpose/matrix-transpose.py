import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    print(A)
    rows = len(A)
    cols = len(A[0])
    
    print("A rows: ", rows)
    print("A cols: ", cols)

    t = np.zeros((cols, rows))
    print(t)

    col = 0
    for row in range(0, len(A)):
        print(A[row])
        for i in range(0, len(A[row])):
            t[i][col] = A[row][i]
        col += 1
    print(t)
    
    return t
