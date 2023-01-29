# This method is used to add element at the end of the existing array.

from array import *

stud_roll = array("i",[1,2,3,4,5,6,7,8,9])

i=0

n=len(stud_roll)

while i<n:
    print(stud_roll[i])
    i+=1


print("Array after append:")

stud_roll.append(26)

i=0
n=len(stud_roll)

while i<n:
    print(stud_roll[i])
    i+=1