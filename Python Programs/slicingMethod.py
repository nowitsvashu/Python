from array import *

a= array("i",[])

n=int(input("Size of array:"))

i=0

while i<n:
    a.append(int(input("Enter the element:")))
    i+=1


b=a[0:2]
i=0
while i<len(b):
    print(a[i])
    i+=1
