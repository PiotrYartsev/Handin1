import numpy as np
import math 
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace
#using the least squares method make a linear fit to the data

x= [0,1,2,3]

y= [0, 1, 4 , 9]

weight = [1,1,1,1]

f=lambda x: a*x+b

f_a= lambda x: x
f_b= lambda x: 1



def calcB(x, y, weight):
    B_1=0
    B_2=0
    for i in range(len(x)):
        B_1 += weight[i]*y[i]*f_a(x[i])
        B_2 += weight[i]*y[i]*f_b(x[i])
    #print(B_1)
    #print(B_2)

    return(B_1, B_2)

B_values=calcB(x, y, weight)

def linearfit(x, y, weight):
    C_11=0
    C_12=0
    C_21=0
    C_22=0
    for i in range(len(x)):
        C_11 += weight[i]*f_a(x[i])**2
        C_12 += weight[i]*f_a(x[i])*f_b(x[i])
        C_21 += weight[i]*f_a(x[i])*f_b(x[i])
        C_22 += weight[i]*f_b(x[i])**2

    #print(C_11)

    #print(C_12)

    #print(C_21)

    #print(C_22)

    return(C_11, C_12, C_21, C_22)

C_values=linearfit(x, y, weight)



#make a matrix with the values of the data for the C matrix

C=[[C_values[0], C_values[1]], [C_values[2], C_values[3]]]

print("The C matrix is:")
print(C[0])
print(C[1], "\n")
#make a matrix with the values of the data for the B matrix

B=[[B_values[0] ], [B_values[1]]]

print("The B matrix is:")
print(B[0])
print(B[1], "\n")

#invert C matrix

C_inverted = np.linalg.inv(C)

print("The inverted C matrix is:")
print(C_inverted, "\n")

#multiply C_inverted and B

P=np.matmul(C_inverted, B)

print("The P matrix is:")
print(P, "\n")

#test if the fit is correct
a=P[0][0]
b=P[1][0]

print("The measurment vs the calculated values are:")
print(y[0], f(x[0]))
print(y[1], f(x[1]))
print(y[2], f(x[2]))
print(y[3], f(x[3]), "\n")

#the error in a and b is
print("The error in a is:")
print(math.sqrt(C_inverted[0][0]), "\n")

print("The error in b is:")
print(math.sqrt(C_inverted[1][1]), "\n")
#error of the fit





Q_sq=0
for i in range(len(x)):
    Q_sq += ((y[i]-f(x[i]))**2)/(weight[i])

print("The Q^2 error in the fit is:")
print((Q_sq), "\n")

degrees_of_freedom=len(x)-2

xsi_sq=Q_sq/degrees_of_freedom

print("The xsi^2 error is:")
print(xsi_sq, "\n")

stops=linspace(0,3,1000)

f_list=[]

for i in stops:
    f_list.append(f(i))

plt.plot(x, y,'o')
plt.plot(stops, f_list)
plt.show()