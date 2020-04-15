import numpy as np 

#import Y 
Y = np.array([[350],[460],[350],[430],[350]])

#import matrix 
X = np.array([[1,5.50,3.3],[1,7.50,3.3],[1,8.00,3.0],[1,8.00,4.5],[1,6.80,3.0]])

#import transpose matrix X 
XT=np.transpose(X)

#dot transpose matrix X and matrix X, call as XTX  
XTX=XT.dot(X)
print(" dot of matrix XT and Matrix X: ")

#pseudo inverse matrix XTX, call as XTX_inv
XTX_inv=np.linalg.inv(XTX)
print(" pseudo inverse matrix XTX: ",XTX_inv)

#dot of matrix XT and matrix Y, call as X 
XTY=XT.dot(Y)
print("dot of matrix XT and matrix Y:",XTY)

#find paramenters learning beta 
theta=np.dot(XTX_inv,XTY)
print("parameters learning are: ",theta)
