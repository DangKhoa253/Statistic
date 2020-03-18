import numpy as np 

a=input("How long of your list?")
X=list(map(int,input().split()))



print(round(float(np.std(X)),1))