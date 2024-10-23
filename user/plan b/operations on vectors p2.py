
#addition of two vector
def addvect(u,v):
    return[u[i]+v[i]for i in range(len(u))]
u=[1,2,3,-5,2]
v=[1,-2,3,1,1]
print(addvect(u,v))

#substract of two vector
def subvect(u,v):
    return[u[i]-v[i]for i in range(len(u))]
u=[1,2,3,-5,2]
v=[1,-2,3,1,1]
print(subvect(u,v))

#list representation  
v=[1,23,2]
u={0:1,1:23,2:2}#dictionary based representation
print(u) 


#adding scalar vector
def addscvect(u,a):
    return[a*u[i]for i in range(len(u))]
u=[2,3,5,6]
print(addscvect(u,-2))


#dot product
def dotprod(u,v):
    return sum([u[i]*v[i]for i in range(len(u))])
u=[2,3,5,6]
v=[1,1,-1,1]
print(dotprod(u,v))


#creating a column vector with 2 row and 1 columns
import numpy as np
col_vec=np.array([[4],[3],[3]])
print("A column vector\n",col_vec)
#printing the shape of the vector
print("Shape of vector=",col_vec.shape)


#creating arow vector witn 1row and 3 columns
import numpy as np
row_vec=np.array([[4,-1,2]])
print("shape of vector=",row_vec)
#printing the shape of the vector
print("shape of vector=",row_vec.shape)


# zero colunm vector of dimension 3
zero_vector_3=np.zeros(4)
print(zero_vector_3)
t=np.reshape(zero_vector_3,[4,1])
print(t)


#Addressing index value
import numpy as np
vector=np.array([[4],[-1],[2]]) 
print("the vector",vector)   
print("\n Elements at position 1",vector[0]) 
  
#use numpy lib
import numpy as np
v=np.array([1,2,40,7])   
print(v)
print(type(v))
print(v.shape)
print(v[3])
print(v[0],v[1],v[2],v[3])
u=np.array([[1,2,3]])
print(u.shape)
print(u)

#vector addition
import numpy as np
p=np.array([0,2,1])
q=np.array([-1,2])
if(len(p)==len(q)):
    add=np.add(p,q)
    print(add)
else:
    print("the dimension of array are not same")

import numpy as np
p=np.array([0,2,1])
q=np.array([-1,0,2])
if(len(p)==len(q)):
    add=np.add(p,q)
    print(add)
else:
    print("the dimension of array are not same")


#using numpy scalar vector multiplication.
import numpy as np
a=np.array([0,-2,6])
b=np.multiply(4,a)
print(b)

#using numpy dot product
import numpy as np
e=np.array([0,2,1])
f=np.array([-1,0,2])
r=np.dot(e,f)
print(r)

#using numpy combination of scalar multiplication and vector
import numpy as np
e=np.array([0,2,1])
f=np.array([-1,0,2])
add1=np.multiply(2,e)
add2=np.multiply(5,f)
add=np.add(add1,add2)
print(add)










