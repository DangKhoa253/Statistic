import statistics

a=int(input())
X=[int(x) for x in input().split()]
X.sort()
i=int(len(X)/2)
if len(X) % 2 != 0:
    L=X[:i]
    U=X[i+1:]
else: 
    L=X[:i]
    U=X[i:]

print(int(statistics.median(L)))
print(int(statistics.median(X)))
print(int(statistics.median(U)))



