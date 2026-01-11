# LEAP YEAR PROGRAM_____

# year=int(input("ENTER THE YEAR : "))



# if year%400==0 and year%100==0:
#     print(year," is leap year")
# elif (year % 4 ==0) and (year % 100 != 0):
#     print(year," is a leap year")
# else:
#     print(year," not is leap year")

# ------------------------------------------------

# dividle by 5 or not__________

# n=int(input("enter no : "))

# if n%5==0:
#     print("yes")

# else:

#     print("NO")
# ---------------------------------------------------

# swaping two variable________

# x=int(input("enter x no : "))
# y=int(input("enter y no : "))

# print("x=",x  ,"y=",y)

# a=x
# x=y
# y=a
# print("x=",x  ,"y=",y)

# ----------------------------------------

# sum of no like no is 3 than output is 1+2 =3 3+3 =6 than sum is 3 

# i=1
# sum=0
# while(i<=5):
#     sum=sum+i
#     i=i+1
#     print(i,sum)

# --------------------------------------

# fingd out uniqu code of any string 

# x="MysirG"

# for i in x:
#     print(ord(i))

# ----------------------

# count digit 

# u=int(input("ENTER NO: "))

# convert=str(u)

# print(len(convert))

# -------------

# s=int(input("enter start no :"))

# e=int(int(input("enter end no: ")))

# for n in range(s,e+1):
#     if n%2!=0:
#         print(n)

# for i in range(1,s+1):
#     if i%2==0:
#         print(i)

# for i  in range(1,10+1):
#     print(i,2*i)

# i=0
# while i<=10:
#     print(2*i-1)
#     i=i+1

# ------range--------
# range ma first value start ,second value end and last value comman gap

# u=int(input(":"))
# for i in range(1,u,10):
    # print(i)

# ----------

# ------list------

# l1=[23,4,5,54,45,45,34,23]
# i=7
# while (i<=7):
#     print(l1[i])
#     i=i+1

# while (i>=0):
#     print(l1[i])
#     i=i-1


# --------------------------------

# ------------------ packing and unpacking -----------------

# unpacking___

# l1=[10,20,30]
# s=sum(l1)
# print(s)
# a,b,c=l1

# print(a) # o/p = 10

# --------- patne ----------

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print("*",end=" ")
#         else:
#             print("_",end=" ")
#     print()

# --------------------------------------------------------------------
"""
Given two int values, return their sum. Unless the two values are the same, then return double their sum.


sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
# while True:    
#     m=input("ENTER | y | FOR CACULATE AND | n | FOR EXIT :")
#     if m=="y":
#         a=int(input("ENTER THE NUMBER :"))
#         b=int(input("ENTER THE NUMBER :"))
#         sum=a+b
#         if a==b:
#             print(sum*2)
#         else:
#             print("A SUM IS ", sum)
#     else:
#         break

# -------------
# a=int(input("ENTER THE NUMBER :"))
# b=int(input("ENTER THE NUMBER :"))

# if a==10 or b==10 or a+b==10:
#     print(True)
# else:
#     print(False)

# def first_two(str):
#   l=str[0]+str[1]
#   if len(str)>2:
#     print(str[0]+str[1])
#   else : 
#     print(str)


# first_two(input("ENTER WORD OR CHAR "))
# str="vardan"
# r=str.split(",")
# r1=",".join(r)
# print(r1[1:-1:1])

# x=10
def f1():
    x=5
    g=globals() # it is function that is return dict
    print("Local x=",x)
    print("global x=",g['x'])

# print("global x=",x)
# f1()
# a=[12,2,3,1,2]
# a_l=(len(a)-1)/2
# # b_l=(len(b)-1)/2
# c_i=int(a_l)
# print(a[c_i])

# def middle_way(a, b):
#   if len(a)>=3 and len(b)>=3:
#     a_l=(len(a)-1)/2
#     c_a=int(a)
#     b_l=(len(b)-1)/2
#     c_b=int(b)
#     new_list=[a[c_a],b[c_b]]
#     return new_list
  
# s=[12,3,4,5,5]
# f=[2,45,6,7,8,9,6]
# middle_way(s,f)


# ///////////////////////////

no1=int(input("first no"))
# no2=int(input("second no"))
# sub=no1/no2
# print(sub)

