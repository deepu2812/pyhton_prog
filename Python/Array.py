from array import  *

vals = array('i',[6,5,9,12,3])

newArray = array(vals.typecode , (a*a for a in vals))

for e in newArray:
    print(e)