#calculate a weighted sum of the values in a list using least squares

import math
import random
import statistics

def weigheted_sum(values, weights):
    values_sum = 0
    weights_sum = 0
    for i in range(len(values)):
        values_sum += values[i] / weights[i]**2
        weights_sum += 1/weights[i]**2
        k=values_sum/weights_sum
    return(k)



def new_error(weights):
    sum=0

    for i in range(len(weights)):  
        sum += 1/(weights[i]**2)
    
    return(1/sum)

#problem a)

print("Problem a)")
values = [1.20, 1.15, 2.0, 1.17]

#print(statistics.mean(values))

weights = [0.20, 0.10, 0.8, 0.7]

print("For the values {} with the errors {} we have:".format(values, weights))
print("The weighted sum is: {}".format(weigheted_sum(values, weights)))
print("The error is: {}".format(new_error(weights)))


#problem b)

print( "Problem b)")
values2 = [20, 25, 18, 16]

weights2 = [2, 1, 2, 7]

print("For the values {} with the errors {} we have:".format(values2, weights2))
print("The weighted sum is: {}".format(weigheted_sum(values2, weights2)))
print("The error is: {}".format(new_error(weights2)))


