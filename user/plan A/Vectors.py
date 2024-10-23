# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:42:45 2024

@author: INDIA
"""
def addvect(u,v):
    if(len(u)==len(v)):
        return[u[i]+v[i] for i in range(len(u))]
u=[1,2,3,-5,2]
v=[1,-2,3,1,1]
print(addvect(u,v))
u=[1,23,2] #list reprensentation
v={0:1,1:23,2:2} #dictionary based representation
print(u)

u=[1,2,3,-5,2]
v=[1,-2,3,1,1]
print(u+v)

#scalar vector multiplication
def addscvector(u,a):
    return[a*u[i] for i in range(len(u))]
u=[2,3,5,6]
print(addscvector(u,-2))

#dot product
def dotprod(u,v):
    return sum([u[i]*v[i] for i in range(len(u))])
u=[2,3,5,6]
v=[1,1,-1,1]
print(dotprod(u,v))


#column vector
import numpy as np
col_vec=np.array([[4],[3],[3]])
print("A column vector\n",col_vec)
print("Shape of vector=",col_vec.shape)

#row vector
import numpy as np
row_vec=np.array([[4,-1,2]])
print("A row vector\n",row_vec)
print("Shape of vector=",row_vec.shape)

zero_vector=np.zeros([4])
print(zero_vector)

zero_vector_3=np.zeros(4)
print(zero_vector_3)
t=np.reshape(zero_vector_3,[4,1])
print(t)

import numpy as np
vector=np.array([[4],[-1],[2]])
print("The vector",vector)

print("Element at position 1=",vector[0])
print("Element at position 3=",vector[-1])

vector=np.array([3,3])