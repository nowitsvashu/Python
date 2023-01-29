from array import *

a=array("i",[ ])
n=int(input("Enter the number of elements:"))

i=0
while i<n:
    a.append(int(input("Enter the item:")))
    i+=1


print("Items are:")
for i in range(len(a)):
    print(a[i])