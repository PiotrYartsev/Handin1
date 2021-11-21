#plot some data
import matplotlib.pyplot as plt
from numpy.core.function_base import linspace

Q_real=[]
a_list=[0,0.5,0.571,1]
for a in a_list:
    
    x=[0,1,2,3]

    y=[0,2,6,12]

    weight = [1,1,1,1]

    C=x[0]**2+x[1]**2+x[2]**2+x[3]**2
    

    B=(y[0]-a*x[0]**2)*x[0]+ (y[1]-a*x[1]**2)*x[1]+(y[2]-a*x[2]**2)*x[2]+(y[3]-a*x[3]**2)*x[3]  

    b=B/C
    print("The value of b is:")
    print(b)
    f=lambda x: a*x**2+b*x

    f_1=[]

    #make a list of numbers between 0 and 3 in 1000 steps
    i=linspace(0,3,1000)
      
    Q_sq=0
    for integer in range(len(x)):
        Q_sq=Q_sq+((y[integer]-f(x[integer]))**2)/weight[integer] 
    #print(Q_sq)
    Q_real.append(Q_sq)
    #for k in i:
    #    f_1.append(f(k))
    #make a dot plot
    #plt.plot(x,y,'o')
    #plt.plot(i,f_1)
    #plt.show()
print("The value for C is:")
print(C)
print(Q_real)
plt.plot(a_list,Q_real,'o')
plt.show()