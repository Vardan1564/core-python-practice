def add (a,s):
    return a+s

# d=add(12,3)

# x=add

# print(f"sum = {d} x = {id(x)}")


# --------lambda -------

# way 1 
k=(lambda a,b:a+b)(1,2)
# print(k)

# way 2

l=lambda d,b:d+b
# print(l(12,4))

# ----------
# -----factorial-----
f=1
for i in range(1,5+1):
    f=f*i
    # print(f)

# --------using while loop---

# f1=1
# i=1
# while i<=5:
#     f1=f1*i
#     print(f1)
#     i=i+1

"""
f1 value is 1 

f1=f1*i
    | |
    1*1=1
now value f1 is 1
    1*2=2
now value f1 is 2
    2*3=6
now value f1 is 6
    6*4=24
now value f1 is 24
    24*5=120
now value f1 is 120

output=120
"""

#  -------factorial using lambda function-----------
f=lambda n:1 if n==0 or n==1 else n*f(n-1)
                                    # recall function 
                                    # 

print(f(5))