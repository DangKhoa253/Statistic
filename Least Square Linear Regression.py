#Linear Regression - Y^= a + b*X 

# 1.Using original method 
from statistics import mean, pstdev
#a.if data is X={} and Y={} 
n=int(input())
X=list(map(int,input().split()))
Y=list(map(int,input().split()))

#calculate sum X,Y
Xi=sum(X)
Yi=sum(Y)

#mean X,Y 
x=mean(X)
y=mean(Y)

#calculate sum of square 
def square_list(a):
    return[ i**2 for i in a]

X2=square_list(X)
Xi_2=sum(X2)
XY=sum([a*b for a,b in zip(X,Y)]) 

#finding value of b:
#b= ((n*XY) - (Xi*Yi)) / ((n*Xi_2) - (Xi**2))

#another way to find value of b - using pearson correlation coefficient: 
def pearson(x, y):
    mx,my,stdx,stdy = mean(x), mean(y), pstdev(x), pstdev(y)
    return sum( (xi - mx) * (yi - my) for xi, yi in zip(x,y)) / (len(x) * stdx * stdy)
b = pearson(X,Y) * (pstdev(Y) / pstdev(X))
#finding value of a:
a= y - b*x

#The regression line : Y^ = a + bX 
print("The regression line: Y^ = ",round(a,2)," +",round(b,2)," X")


#b. if data is (xi,yi): ( Ex. 95 85, 85 95, 80 70,70 65,60 70) 
#zip(*...) -> divide into 2 lists
x,y=zip(*(map(float,input().split()) for i in range(5)))

def pearson(x, y):
    mx,my,stdx,stdy = mean(x), mean(y), pstdev(x), pstdev(y)
    return sum( (xi - mx) * (yi - my) for xi, yi in zip(x,y)) / (len(x) * stdx * stdy)

def linear_reg(x,y):
    b = pearson(X,Y) * (pstdev(Y) / pstdev(X)) 
    return mean(y) - mean(x)*b,b 

a,b=linear_reg(x,y)
print(a,b)


#2.Using sklearn: 
from sklearn import linear_model 
import numpy as np 
xl=[1,2,3,4,5]
x=np.asarray(xl).reshape(-1,1)
y=[2,1,4,3,5]
lm=linear_model.LinearRegression()
lm.fit(x,y)
print(lm.intercept_)
print(lm.coef_[0])

#
