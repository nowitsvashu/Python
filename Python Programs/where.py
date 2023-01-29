from numpy import *

a=array([100,200,300,400,500])
b=array([10,20,30,40,50])

c=where(a<b,a,b)
print(c)