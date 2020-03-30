import math 
from statistics import mean,stdev

n=int(input())
X=list(map(float,input().split()))
Y=list(map(float,input().split()))

def cov(X,Y):
    x=mean(X)
    y=mean(Y)

    sum=0 

    for i in range(0,n):
        sum += (X[i] - x ) * (Y[i] - y )

    return sum/(n-1)

sigmaX=stdev(X)
sigmaY=stdev(Y)

result=cov(X,Y)/(sigmaX * sigmaY)

print(round(result,3))