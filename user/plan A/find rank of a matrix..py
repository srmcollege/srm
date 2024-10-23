def matrix_rank(mat):
    mat[0][0] = 1 if mat[0][0] != 0 else 0
    for j in range(1, len(mat[0])):
        mat[0][j] /= mat[0][0]
    
    # Step 2: Eliminate elements below the first 1
    for i in range(1, len(mat)):
        if mat[i][0] != 0:
            for j in range(len(mat[0])):
                mat[i][j] -= mat[i][0] * mat[0][j]
    
    # Count non-zero rows to determine rank
    return sum(1 for row in mat if any(val != 0 for val in row))

mat = [[float(input(f"Element [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]

print("Original Matrix:", mat)

rank = matrix_rank(mat)
print(f"The rank of the matrix is: {rank}")
