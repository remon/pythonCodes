#example 3
#added by @sagarbabalsure 
#This example show the some operations using numpy package. 


import numpy as np

#basics

a=np.array([[1,2,3],
			[4,5,6]])
print(type(a))
print(np.ndim(a))
print(np.size(a))
print(a.dtype)
print(a.shape)
#array creation
a=np.array((2,4,6))
print(a)
b=np.zeros((3,4),dtype='int')
print(b)
c=np.ones((2,2))
print(c)
d=np.full((3,3),4)
print(d)
e=np.arange(0,30,5)
print(e)
f=np.random.random((2,2))
print(f)
g=np.linspace(0,10,5,dtype='int')
print(g)

#array indexing
x=np.array([[1,2,3],[2,3,4],[1,4,7]])
t=x[:2,:2]
print(t)
t=x[[0,0]]
print(t)
t=x[[1,2],[1,0]]
print(t)

#operations
print(x+2)
print(x*3)
print(x)
print("transpose: ",x.T)
print("multiplication",a.dot(x))
print(x.max())
print(x.sum())
print(np.sort(x))
