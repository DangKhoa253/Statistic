from math import sqrt, erf

mean,std=map(int,input().split())

#erf (x) for cumulative proba 

cdf= lambda x: 0.5 * ( 1 + erf( (x - mean) / (std * sqrt(2)) ))

x1=float(input())
x2=float(input())

#greater than x1

print(round(100 - cdf(x1)*100,2))

#greater than x2 

print(round(100 - cdf(x2)*100,2))

#lower than x2 

print(round(cdf(x2)*100,2))