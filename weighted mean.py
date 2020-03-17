
num=int(input("Lenght of array"))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[]
def weighted_mean():
    total_b=sum(b)
    for i in range (0, num):
        c.append(a[i]*b[i])
    result=sum(c)/total_b
    print(round(result),1)

weighted_mean()

#
N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))