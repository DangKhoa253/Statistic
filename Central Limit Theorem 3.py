from math import sqrt 

n=int(input())
mean=int(input())
sigma=int(input())
interval=float(input())
z=float(input())

# We have interval formula: 
# 1) meanCI = mean(x) + -  Z score * sigma / sqrt(n) 
# 2) proportionCI = p^ + - Z Score * sigma / sqrt (n)
# 3) upperlimit =samplePara + Zscore(a/2) * SE 
#    lowerlimit= samplePara - Zscore(a/2) * SE 
# SE = sigma / sqrt (n )

#P(A)
print(round(mean - z * (sigma / sqrt(n)),2 ))
#P(B)
print(round(mean + z * (sigma / sqrt(n)),2 ))