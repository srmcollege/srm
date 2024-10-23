"""
#row reduction (echelon form)
import numpy as np
def reduce(arr):
    for i in range(len((arr))):
        res=(arr[i][i]*arr[i-1])-(arr[i+1][i]*arr[i])
        arr[i+1]=res
        break
    print("Row Echolon form is \n",arr)
    count=len(arr)
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j] == 0 and arr[i][j+1]==0):
                count -= 1
                break
    print("Rank of the matrix is ",count)
    
matrix=np.array([[3,2],[6,4]])
print(matrix)
print()
reduce(matrix)              
"""


#without numpy
matrix = [[2, 8], [3, 5]]
print("The given matrix is: ")
for row in matrix:
    print(row)
print()
for i in range(2):
    if matrix[i][i] == 0:
        matrix[i], matrix[i + 1] = matrix[i + 1], matrix[i]
    for j in range(i + 1, 2):
        if matrix[j][i] != 0:
            factor = matrix[j][i] / matrix[i][i]
            matrix[j] = [matrix[j][k] - factor * matrix[i][k] for k in range(2)]
print("Row Echelon Form is:")
for row in matrix:
    print(row)
print()
rank = sum(any(x != 0 for x in row) for row in matrix)
print("Rank of the matrix is", rank)
