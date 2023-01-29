from numpy import *

a= array([100,200,300,400,500])
b=array([10,20,30,40,50])

c=a==b
print(any(c))

d=array([1,2,3,4,5])
e=array([1,2,3,4,5,])
result=d==e
print(all(result))