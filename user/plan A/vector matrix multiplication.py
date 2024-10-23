#matrix vector multiplication in terms of linear combination
a=int(input("Enter no of rows:"))
b=int(input("Enter no of columns:"))
matrix=[]
for i in range(a):
    row=[]
    for j in range(b): 
        element=int(input(f"enter the elements at position ({i},{j}): "))
        row.append(element)
    print()
    matrix.append(row)
print("matrix is")
for i in range(a):
      for j in range(b):
            print(matrix[i][j],end=" ")
      print()
      print("matrix",matrix)
c=int(input("Enter no of rows:"))
d=int(input("Enter no of columns:"))
vector=[]
for i in range(c):
    row=[]
    for j in range(d):
        element=int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    print()
    vector.append(row)
print("vector is",vector)
for row in matrix:
    print(row)
print("vector")
for row in vector:
    print(vector)
# Perform matrix-vector multiplication
if (b == c):
    print("Matrix-vector multiplication not possible due to dimension mismatch.")
else:
    result = []
    for i in range(a):
        sum = 0
        for j in range(b):
            sum += matrix[i][j] * vector[0][j] 
        result.append(sum)
        print(result)
        
#vector matrix multiplication 
a=int(input("Enter no of rows:"))
b=int(input("Enter no of columns:"))
matrix=[]
for i in range(a):
    row=[]
    for j in range(b): 
        element=int(input(f"enter the elements at position ({i},{j}): "))
        row.append(element)
    print()
    matrix.append(row)
print("matrix is")
for i in range(a):
      for j in range(b):
            print(matrix[i][j],end=" ")
      print()
      print("matrix",matrix)        
c=int(input("Enter no of rows:"))
d=int(input("Enter no of columns:"))
vector=[]
for i in range(c):
    row=[]
    for j in range(d):
        element=int(input(f"Enter element at position ({i},{j}): "))
        row.append(element)
    print()
    vector.append(row)
print("vector is",vector)
for row in matrix:
    print(row)
print("vector")
for row in vector:
    print(vector)
# Validate dimensions for multiplication
if b != c:
    print("\nMatrix and vector dimensions are not compatible for multiplication.")
else:
    # Initialize result vector
    result_vector = []

    # Perform multiplication
    for i in range(a):
        row_result = 0
        for j in range(b):
            row_result += matrix[i][j] * vector[j]
        result_vector.append(row_result)

    # Print result
    print("\nResult of vector-matrix multiplication:")
    print(result_vector)

