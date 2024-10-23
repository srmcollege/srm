m1_rows=int(input("Enter Number of Rows for matrix 1 :"))
m1_cols=int(input("Enter Number of Column for matrix 1 :"))
matrix1=[]
for i in range(m1_rows):
    print("Enter for ",i+1, "row of matrix 1 :")
    for j in range(m1_cols):
        a=int(input("Enter Value: "))
        matrix1.append(a)
m2_rows=int(input("Enter Number of Rows for matrix 2 :"))
m2_cols=int(input("Enter Number of Column for matrix 2 :"))
matrix2=[]
for i in range(m2_rows):
    print("Enter for ",i+1, "row of matrix 1 :")
    for j in range(m2_cols):
        a=int(input("Enter Value: "))
        matrix2.append(a)            
print("First Matrix is : ",matrix1)
print("Second Matrix is : ",matrix2)
result=[]
if(m1_rows==m2_rows):
    if(m1_cols==m2_cols):
        for i in range(len(matrix1)):
            for j in matrix2:
                a=matrix1[i]+matrix2[i]
                result.append(a)
                break
        print("The addition of matrices is : \n",result)
else:
    print("Matrix Addition is not possible as Dimenions of both matrix are not same.")

        
