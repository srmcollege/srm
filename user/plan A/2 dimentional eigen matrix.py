import numpy as np

print("Enter the elements of a 2x2 matrix (separated by spaces):")
elements = input("Matrix (e.g 'a b; c d'): ").split(';')

matrix = np.array([[float(num) for num in row.split()] for row in elements])

eigenvalues, eigenvectors = np.linalg.eig(matrix)

print("Eigen values are:\n", eigenvalues)
print("Eigen vectors are:\n", eigenvectors)
