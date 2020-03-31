
def spearman(n,X,Y):
    x=list(X)
    y=list(Y)
    x.sort()
    y.sort()
    #Calculate rank difference:
    di= ( [ (x.index(X[i]) - y.index(Y[i]) ) ** 2 for i in range(n) ] ) 
    return 1 - (6 * sum(di) / (n*(n**2 - 1)))

n=int(input())
X=[float(i) for i in input().split()]
Y=[float(i) for i in input().split()]


print(round(spearman(n,X,Y),3))