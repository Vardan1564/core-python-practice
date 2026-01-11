# ///////////////////////////
# fibonacci series

# def fibonacci(num):
#     f=0
#     for i in range(1,num+1):
#         f=f+i
#     print(f)

# no=int(input("ENTER A NUMBER"))

# if no>1:
#     fibonacci(no)
# else:
#     print("ENTER LARGE NUMBER")


# ///////////////////////////////////////////////////
# Find INTEREST and total amount
 
# P=int(input("ENTER A MAIN AMOUNT :"))
# R=int(input("ENTER A MAIN INTEREST RATE :"))
# T=int(input("ENTER A MAIN TIME OF LOAN :"))

# print(f"YOUR INTEREST IS {P*R*T/100}")

# print(f"YOUR FAINALE AMOUNT IS {P*R*T/100 + P}")

# /////////////////////////////////////////////////////////
# circle

# PI=3.14
# r=int(input("ENTER A CIRCLE RADIUS :"))

# print(f"YOUR CIRCLE RADIUS IS -> {r}\n")

# print(f"YOUR CIRCLE AREA IS   -> {PI*(r*r)}")

# /////////////////////////////////////////////////////////
# number is prime or not

# from math import *

# num=int(input("EMTER A NUMBER : "))

# for i in  range(2,int(sqrt(num))+1):
    
#     if num%i==0:
#         print(f"{num} is not a prime number")
#     else:
#         print(f"{num} is prime number")
#     print(i) 

# ////////////////////////////////////////////////////////
# check number is fibonacci

# num=int(input("ENTER A NUMBER :"))
# f=0
# l=[]
# for i in range(num+1):
#     f=f+i
#     l.append(f)
    

# if  str(num) in str(l):
#      print("YES THIS NUMBER IS FIBONACCI NUMBER 👍")
# else:
#      print("NO THIS NUMBER IS FIBONACCI NUMBER 😒")

# /////////////////////////////////////////////////
# ASCLL VALUE OF CHARECTER
# means a in value 97
# a to z ni value

# l=['a','b','c']

# print("char" , "value")
# for i in l:
    
#     print(i,"-->",ord(i))

# ////////////////////////////////////////////////////////
# sum of squres of first num....

# from math import *

# num=int(input("ENTER A NUMBER :"))
# sum=0

# for i in range(1,num+1):
#      sum=sum+(i*i*i)
# print(sum)

# ////////////////////////////////////////////
# saprat int no in new list

# l1=[1,2,3,"wer",4,'r',5,6,"utut",7,8,True,9,0]

# n=1
# add=[]

# for i in l1:
#     if type(n)==type(i):
#         add.append(i)

# print(add)

# ///////////////////////////////////////////////////
# using numpy "prod" method for multiply a list

# from numpy import *

# l1=[1,2,3]
# t1=4
# x=1
# print(f"ans is {prod(l1)}")

# for i in l1:
#     if type(t1)==type(i):
#             x=x*i

# print(x)

# ////////////////////////////////////////////////////////

# l1=[23,4,23,4,34,5,2,35,23,5,4]

# print(max(l1))

# # //////////////////////////////////
# l=[2,5,3,1,7,3,8,3,0]
# a=sorted(l)
# l1=[]
# l1.append(str(a))
# print(l1)
# a1=l1.reverse()
# print(a1)

# /////////////////////////////////////////////
