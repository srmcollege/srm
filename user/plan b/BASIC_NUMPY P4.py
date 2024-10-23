# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 12:13:14 2024

@author: INDIA
"""
#creating matrix
import numpy as np
import numpy.matlib
a=np.mat('1,3,5;2,4,6;1,6,8')
print(a)

#addition
a=np.mat('1,3,5;2,4,6;1,6,8')
b=np.mat('2,5,6;4,2,9;4,1,3')
print(np.add(a,b))

#subtraction
a=np.mat('1,3,5;2,4,6;1,6,8')
b=np.mat('2,5,6;4,2,9;4,1,3')
print(np.subtract(a,b))


#dot product
a=np.mat('1,3,5;2,4,6;1,6,8')
b=np.mat('2,5,6;4,2,9;4,1,3')
print(np.dot(a,b))

#multiplying 2 matrices
a=np.mat('1,3,5;2,4,6;1,6,8')
b=np.mat('2,5,6;4,2,9;4,1,3')
print(np.multiply(a,b))

#scalar multiplication
c=np.mat('2,5,6;4,2,9;4,1,3')
print(2*c)

#TRANSPOSE using numppy
a=np.mat('1,3,5;2,4,6;1,6,8')
print(np.transpose(a))

#inverse
b=np.mat('2,5,6;4,2,9;4,1,3')
print(np.linalg.inv(c))

#identity matrix
I=np.matlib.identity(3,dtype="int")
print(I)

#Transpose
a=2
b=2
c=[[1,2],[3,4]]
for i in range(b):
    for j in range(a):
        print(c[j][i], end=" ")
    print()
    
#CREATING MATRIX    
m1_rows=int(input("Enter Number of Rows for matrix 1 :"))
m1_cols=int(input("Enter Number of Column for matrix 1 :"))
matrix1=[]
for i in range(m1_rows):
    print("Enter for ",i+1, "row of matrix 1 :")
    for j in range(m1_cols):
        a=int(input("Enter Value: "))
        matrix1.append(a)
print("Matrix is \n",matrix1)

