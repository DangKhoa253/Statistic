from math import pow
from math import factorial
from math import exp 


mean = float(input("mean of data: "))
x = int(input("variable: "))

#method : P= ( e^-x * x ^ k )/ k! 

result= ( pow(mean,x) * exp(-mean) / factorial(x) )

print("poisson proba is: ",round(result,3))



