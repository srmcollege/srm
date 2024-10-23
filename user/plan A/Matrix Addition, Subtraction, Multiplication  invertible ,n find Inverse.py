import numpy as np

def matrix_operations(matrix_a, matrix_b):
    # Ensure inputs are NumPy arrays
    matrix_a = np.array(matrix_a)
    matrix_b = np.array(matrix_b)

    # Matrix Addition
    addition = matrix_a + matrix_b
    print("Matrix Addition:\n", addition)

    # Matrix Subtraction
    subtraction = matrix_a - matrix_b
    print("Matrix Subtraction:\n", subtraction)

    # Matrix Multiplication
    multiplication = np.dot(matrix_a, matrix_b)
    print("Matrix Multiplication:\n", multiplication)

    # Check if matrix A is invertible and find inverse
    if np.linalg.det(matrix_a) != 0:
        inverse_a = np.linalg.inv(matrix_a)
        print("Inverse of Matrix A:\n", inverse_a)
    else:
        print("Matrix A is not invertible.")

# Example matrices
matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]

matrix_operations(matrix_a, matrix_b)
