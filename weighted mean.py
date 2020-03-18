# way 1
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

# way 2 
num=int(input())
a=list(map(float,input().split()))
b=list(map(float,input().split()))
#sum 
sum_up=sum([a*b for a,b in zip(a,b)])
weighted_mean=round(sum_up/sum(b),1)
print(weighted_mean)