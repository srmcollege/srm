
# matrix vector multiplication in terms of dot combination
vector_length = int(input("Enter the length of the vector: "))
vector = []

print("Enter vector elements:")
for j in range(vector_length):
    element = int(input(f"Element at position ({j}): "))
    vector.append(element)

print()

# Get matrix dimensions and elements
c = int(input("Enter number of rows for the matrix: "))
d = int(input("Enter number of columns for the matrix: "))
matrix = []

print("Enter matrix elements row-wise:")
for i in range(c):
    row = [int(input(f"Element at position ({i},{j}): ")) for j in range(d)]
    matrix.append(row)
print()

# Perform vector-matrix multiplication
if vector_length != c:
    print("Dimension mismatch: Vector length must be equal to the number of rows in the matrix.")
else:
    result = [sum(vector[j] * matrix[j][i] for j in range(vector_length)) for i in range(d)]

    print("\nVector:")
    print(vector)
   
    print("\nMatrix:")
    for row in matrix:
        print(row)
   
    print("\nResulting vector after multiplication:")
    print(result)

-------------------------------------------------------------------------------------

#vector-matrix multiplication in terms of dot product
vector_length = int(input("Enter the length of the vector: "))
vector = []

print("Enter vector elements:")
for j in range(vector_length):
    element = int(input(f"Element at position ({j}): "))
    vector.append(element)
print()

# Get matrix dimensions and elements
c = int(input("Enter number of rows for the matrix: "))
d = int(input("Enter number of columns for the matrix: "))
matrix = []

print("Enter matrix elements row-wise:")
for i in range(c):
    row = [int(input(f"Element at position ({i},{j}): ")) for j in range(d)]
    matrix.append(row)
print()

# Perform vector-matrix multiplication
if vector_length != c:
    print("Dimension mismatch: Vector length must be equal to the number of rows in the matrix.")
else:
    result = [sum(vector[j] * matrix[j][i] for j in range(vector_length)) for i in range(d)]

    # Print vector
    print("\nVector:")
    print(vector)
   
    # Print matrix
    print("\nMatrix:")
    for row in matrix:
        print(row)

    print("\nResulting vector after multiplication:")
    print(result)


