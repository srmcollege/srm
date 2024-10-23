import numpy as np
def reduce(arr):
    for i in range(len((arr))):
        res=(arr[i][i]*arr[i-1])-(arr[i+1][i]*arr[i])
        arr[i+1]=res
        break
    print("row echolon form \n",arr)
    count=len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j]==0 and arr[i][j+1]==0):
                count-=1
                break
    print(f"rank of the matrix{count}")
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
d=int(input("enter a number: "))
matrix=np.array([[a,b],[c,d]])
print(matrix)
print()
reduce(matrix)
###################################################
import numpy as np
def reduce(arr):
    for i in range(len((arr))):
        res=(arr[i][i]*arr[i-1])-(arr[i+1][i]*arr[i])
        arr[i+1]=res
        break
    print("row echolon form \n",arr)
    
    count=len(arr)
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if(arr[i][j]==0 and arr[i][j+1]==0):
                count-=1
                break
    print(f"rank of the matrix: {count}")
matrix=np.array([[3,4],[2,8]])
print(matrix)
print()
reduce(matrix)