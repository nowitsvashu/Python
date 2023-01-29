from array import *

a= array("i",[])

n=int(input("Size of array:"))

i=0

while i<n:
    a.append(int(input("Enter the element:")))
    i+=1

print("Elements are:")
i=0
while i<n:
    print(a[i])
    i+=1

a.pop(int(input("Enter the Loc:")))

print("Elements after pop:")
for i in range(len(a)):
    print(a[i])
     