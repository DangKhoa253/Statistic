from math import pow

a,b=map(int,input().split())
n=int(input())

p=round((a/b) ,3)

result= pow(1-p,n-1) * p

print(round(result,3))