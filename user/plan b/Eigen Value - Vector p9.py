

#Eigen value, Eigen vector. 
import numpy as np
mat1=np.array([[2,1],[1,2]])
m,n=np.linalg.eig(mat1)
print("The Eigen value of matrix are",m); 
print("The Eigen vector of matrix are",n);

#projection
def orthogonal_projection(b, u):
    proj_u = projection_onto(u, b)
    return proj_u
b=np.array([1,2,3])
u=np.array([2,5,3])
b_perp_u = orthogonal_projection(b, u)
print(b_perp_u)

#dot
def projection_onto(u, b):
    return (np.dot(b, u) / np.dot(u, u)) * u

def orthogonal_projection(b, u):
    proj_u = projection_onto(u, b)
    return proj_u
b=np.array([1,2,3])
u=np.array([2,5,3])
b_perp_u = orthogonal_projection(b, u)
print(b_perp_u)
