
#matix vector multiplication interms of linear combination
a = int(input("Enter number of rows for the matrix: "))
b = int(input("Enter number of columns for the matrix: "))
matrix = []

print("Enter matrix elements row-wise:")
for i in range(a):
    row = [int(input(f"Element at position ({i}, {j}): "))for j in range(b)]
    matrix.append(row)
# Get vector dimensions and elements
vector_length = int(input("Enter the length of the vector: "))
if vector_length != b:
    print("Dimension mismatch: Vector length must be equal to the number of columns in the matrix.")
else:
    vector = []
    print("\nEnter vector elements:")
    for j in range(vector_length):
        element = int(input(f"Element at position ({j}): "))
        vector.append(element)
# Perform matrix-vector multiplication
    result = [sum (matrix[i][j]* vector[j] for j in range (b)) for i in range(a)]
    print("\nMatrix:")
    for row in matrix:
        print(row)
    print("\nVector: ")
    print(vector)
    print("\nResulting vector after multiplication:")
    print(result)
--------------------------------------------------------------------------------------------
#vector matix multiplication interms of linear combination
vector_length = int(input("Enter the length of the vector: "))
vector = []
print("\nEnter vector elements:")
for i in range (vector_length):
    element = int(input(f"Element at position ({i}): "))
    vector.append(element)
# Get matrix dimensions and elements
c = int(input("Enter number of rows for the matrix: "))
d = int(input("Enter number of columns for the matrix: "))
matrix = []
if vector_length != c:
    print("Dimension mismatch: Vector length must be equal to the number of rows in the matrix.")
else:
    print("\nEnter matrix elements row-wise:")
    for i in range(c):
        row = [int(input(f" Element at position ({i}, {j}): ")) for j in range(d)]
        matrix.append(row)
# Perform vector-matrix multiplication
    result = [sum(vector[i] * matrix[i][j] for i in range(c)) for j in range(d)]
    print("\nVector:")
    print(vector)
    print("\nMatrix:")
    for row in matrix:
        print(row)
    print("\nResulting vector after multiplication:")
    print(result)
---------------------------------------------------------------------------------------
