m1_rows=int(input("Enter Number of Rows for matrix 1 :"))
m1_cols=int(input("Enter Number of Column for matrix 1 :"))
matrix1=[]
for i in range(m1_rows):
    c1=[]
    print("Enter for ",i+1, "row of matrix 1 :")
    for j in range(m1_cols):
        a=int(input("Enter Value: "))
        c1.append(a)
    matrix1.append(c1)
print("Matrix is \n",matrix1)
for i in range(m1_cols):
    for j in range(m1_rows):
        print(matrix1[j][i], end=" ")
    print()
