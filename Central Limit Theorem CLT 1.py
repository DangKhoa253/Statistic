from math import sqrt,erf 

x=int(input())
n=int(input())
mean=float(input())
sigma=float(input())

Sn=n*mean 
sigma_sum= sqrt(n) * sigma

def cdf(x,mean,sigma):
    Z = (x-mean) /sigma
    return 0.5 * ( 1 + erf( Z/ (sqrt(2))) )

print(round(cdf(x,Sn,sigma_sum),4))