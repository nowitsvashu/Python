from numpy import *

a = array([[1, 2, 3, 4, 5],
                 [5, 4, 3, 2, 1]])


for r in a:
    for c in r:
        print(c)
    print( ) 

print("Using while loop...")

n=len(a)
i=0
j=0
while i<n:
    while j<len(a[i]):
        print(a[i] [j])
        j+=1
    i+=1
    print( )


