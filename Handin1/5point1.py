#Problem a)
N=4

n=1

y_a=[1.20,1.15,2.0,1.17]

y_best_a=1.2258585858585858

sigma_k_a=0.7453559924999299

sigma_k_aa=[0.20,0.10,0.8,0.7]
Chi_sq_a=0

for i in range(len(y_a)):
    Chi_sq_a=Chi_sq_a+((y_a[i]-y_best_a)**2)/sigma_k_aa[i]**2

print("The value for Q^2 for problem a is:")
print(Chi_sq_a)
Chi_sq_a=Chi_sq_a*1/(N-n)
print("The value for Chi^2 for problem a is")

print(Chi_sq_a)

#problem b)
y_b=[20,25,18,16]

y_best_b=21.6

Chi_sq_b=0

sigma_k_b=0.29
sigma_k_bb=[2,1,2,7]
s_sq_b=0
for s in range(len(y_b)):
    Chi_sq_b=Chi_sq_b+1/(N-n)*((y_b[s]-y_best_b)**2)/sigma_k_bb[s]**2

print("The value for Q^2 for problem b is:")
print(Chi_sq_b)
Chi_sq_b=Chi_sq_b*1/(N-n)
print("The value for Chi^2 for problem b is")
print(Chi_sq_b)
