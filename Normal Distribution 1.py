from math import sqrt, erf

mean,std=map(int,input().split())

#erf (x) for cumulative proba 

cdf= lambda x: 0.5 * ( 1 + erf( (x - mean) / (std * sqrt(2)) ))

x1=float(input())
x2,x3=map(float,input().split())

#Less than 19.5 

print(round(cdf(x1),3))

#Between 20 and 22 

print(round(( cdf(x3) - cdf(x2) ),3 ))