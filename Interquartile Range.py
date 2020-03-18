import statistics as stat
import numpy
import copy  

a=int(input("How many input in array X ?"))
X=[int(x) for x in input().split()]
F=[int(x) for x in input().split()]

setA=[]
for i in range(a):
    setA +=[X[i]]*F[i]
N=sum(F)
setA.sort()
print(setA)
if a % 2 == 0: 
    q1=stat.median(setA[:(N//2)])
    q2=stat.median(setA)
    q3=stat.median(setA[(N//2):])
else:
    q1=stat.median(setA[:(N//2)])
    q2=stat.median(setA)
    q3=stat.median(setA[(N//2)+1:])
print(q1)
print(q3)
print(round(float(q3-q1),1))
