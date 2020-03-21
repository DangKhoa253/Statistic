from math import pow

a,b=map(int,input().split())
n=int(input())

p=round((a/b) ,3)

result= pow(1-p,n)

print(round(1-result,3))