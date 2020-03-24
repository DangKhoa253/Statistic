# Special case of poisson distribution: 
# E(x^2) = mean + mean ^2
# Reference from tutorial 
# Reference from https://www.coursehero.com/file/7280151/examples-for-poisson-distrubution-and-hypergeometric-distribution/ 

mean1 = float(input())
mean2 = float(input())

Dailycost1= 160 + 40*(mean1 ** 2)
Dailycost2= 128 + 40*(mean2 ** 2)

#Expected daily cost 

E1= 160 + 40*( mean1 + (mean1**2))
E2= 128 + 40*( mean2 + (mean2**2))

print(round(E1,3))
print(round(E2,3))
