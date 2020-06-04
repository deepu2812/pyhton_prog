from array import *

arr = array('i',[])

n = int(input("Enter your Number of Element:"))

for i in range(n):
    x = int(input("Enter next Value:"))
    arr.append(x)

print(arr)

k=0
val = int(input("Which element do you want to search?"))

for e in arr:
    if e == val:
        print(k)
        break
    k+=1
