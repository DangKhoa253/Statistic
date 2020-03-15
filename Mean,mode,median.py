import numpy as np 
from scipy import stats

#using scipy.stats library 
def stat1():
    number=int(input("write down number of list value:"))
    data=list(map(int,input().split()))
    print(np.mean(data))
    print(np.median(data))
    print(int(stats.mode(data)[0]))


#non using scipy.stats library 

number=int(input())
data=list(map(int,input().split()))
data.sort()
def mean():
    return sum(data)/number
def median():
    if number % 2 == 0:
        return (data[a//2] + data[a//2 +1])/2
    else:
        return (data[a//2 +1])/2
def mode():
    mode1=data[0]
    maxm=1
    cur_max=1
    flag=0
    for i in range(1,len(data)):
        if data[i] == data[i-1]:
            maxm +=1
            if cur_max > maxm:
                mode1=data[i]
                flag=1
        else:
            if flag ==1 :
                cur_max=maxm
                flag=0
                maxm=1 

#stat1()
#mean()
#median()
#mode()
