# lc 2
# -------------- numpy ----------

# import numpy as n

# a=n.array([1,6,57,3,2,67,7])

# print(a.sort())

# for i in a:
#     print(i)

# -------------- using array modul ---------------

# from array import *

# a1=array('i',[12,32,12])

#  for i in a1:
#     print(i)

# a1.append(13)

# print(a1.count(12))
# for i in  reversed(a1):
#     print(i)

# ---------------------------------------

from array import *


a=array('i',[97,56,3,543,5,1,5,6,36,7,4556,7])
s=set(a)
l1=list(s)
l1.sort()
c=array('i',l1)
for i1 in range(len(c)):
    print(i1,c[i1])
