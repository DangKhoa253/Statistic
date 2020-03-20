import math 

n=int(input())
p=float(input())

def nCr(n,k):
    f=math.factorial
    return f(n) // ( f(k) * f(n-k ))
def method(n,k,p):
    return nCr(n,k) * math.pow(p,k) * math.pow(1-p,n-k)

# a) no more 2 pistons rejected
p_a=round(1-p,3)

result_a=round(sum(method(n,k,p_a) for k in range(8,11)),3)
print(result_a)

# b) at least 2 pistons rejected
p_b=round(p,3)

result_b=round(sum(method(n,k,p_b) for k in range(2,11)),3)
print(result_b)
