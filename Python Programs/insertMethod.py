# This method is used to add element at particular position in the existing array

from array import *

a= array("i",[])

n=int(input("Size of array:"))

i=0

while i<n:
    a.append(int(input("Enter the element:")))
    i+=1


i=0
while i<n:
    print(a[i])
    i+=1

a.insert(1,42)

n=len(a)

for i in range(n):
    print(a[i])