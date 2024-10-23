def row_echelon_form(mat):
    #  1 by dividing the first row
    mat[0][0], mat[0][1] = mat[0][0] / mat[0][0], mat[0][1] / mat[0][0]

    mat[1][0], mat[1][1] = mat[1][0] - mat[1][0] * mat[0][0], mat[1][1] - mat[1][0] * mat[0][1]
    
    mat[1][1] = mat[1][1] / mat[1][1]
    
    return mat

mat = [[float(input(f"Element [{i+1}][{j+1}]: ")) for j in range(2)] for i in range(2)]

print("Original Matrix:", mat)

echelon_matrix = row_echelon_form(mat)
print("Row Echelon Form:", echelon_matrix)
