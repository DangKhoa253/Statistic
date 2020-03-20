#Using method

import math 

male=float(input())
female=float(input())
ratio=round(float(male/(male+female)),3)


n=int(input("number of children: "))
k=int(input("number expected male: "))

def nCr(n,k):
    f=math.factorial
    return f(n) // (f(k) * f(n-k))
def method(n,i,ratio):
    return nCr(n,i) * math.pow(ratio,i) * math.pow(1-ratio,n-i) 
 
result=round(sum(method(n,i,ratio) for i in range(0,k)),3)

print(round(1-result,3))

#Using library 
import seaborn as sb, numpy as np
from scipy.stats import binom 

data_binom = binom.rvs(size=10,n=20,p=0.8)
data_binom = binom.rvs(n=20,p=0.8,loc=0,size=100)
print(data_binom)
ax = sb.distplot(data_binom,kde=True,color='blue',hist_kws={"linewidth": 25,'alpha':1})
ax.set(xlabel='Binomial', ylabel='Frequency')

