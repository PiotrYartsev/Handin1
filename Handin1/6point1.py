import numpy as np
import matplotlib
import math


K_matrix= np.array([[1,0],[0,1],[1,-1]])
print("The K matrix is:")
print(K_matrix, "\n")


l_matrix=np.array([[15.0000],[14.9980],[0.0020]])
print("The l matrix is:")
print(l_matrix, "\n")

weights_matrix=np.array([[1/(0.001)**2, 0,0],[0,1/(0.001)**2,0],[0,0,1/(0.001)**2]])
print("The weights matrix is:")
print(weights_matrix, "\n")

#get the transpose matrix of K_matrix

K_transpose=np.transpose(K_matrix)
print("The K_transpose matrix is:")
print(K_transpose, "\n")
#multiplication of K_trasposed and weights_matrix

C_K_transposed_W=np.matmul(K_transpose,weights_matrix)
C=np.matmul(C_K_transposed_W,K_matrix)
print("The C matrix is:")
print(C, "\n")

#Calculate C inverse

C_inverse=np.linalg.inv(C)
print("The C_inverse matrix is:")
print(C_inverse, "\n")

#Calculate the unsertanti in mass a, mass b 

mass_a=C_inverse[0][0]

mass_b=C_inverse[1][1]

mass_a_minus_mass_b=C_inverse[0][1]

print("The error in mass a is:")
print(mass_a, "\n")

print("The error in mass b is:")
print(mass_b, "\n")

print("The error in mass a minus mass b is:")
print(mass_a_minus_mass_b, "\n")

#Calculating the corrected mass a, mass b

R_matrix_1=np.matmul(C_inverse,K_transpose)

R_matrix=np.matmul(R_matrix_1,weights_matrix)
print("The R matrix is:")
print(R_matrix, "\n")

R_transpose=np.transpose(R_matrix)
print("The R_transpose matrix is:")
print(R_transpose, "\n")

#make a cross multiplication of R_transpose and K_matrix

F_matrix=np.multiply(R_transpose,K_matrix)

print("The F matrix is:")
print(F_matrix, "\n")
