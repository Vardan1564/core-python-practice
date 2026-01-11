# -------------- STR -----------------

# s1=input("ENTER NO : ")
# l1=s1.split(',')

# for i in l1:
#     print(int(i))

# print(s1)

# ---join ----------

# l1="hello my college name is h.n.shikla\n"

# x=l1.split(' ')

# print(x)

# o='_'.join(x)

# print(o)

# ----------- format ------------

# a,b=11,22
# s1="sum of {} and {} is {}"

# y=s1.format(a,b,a+b)
# print(y)

# ------- lc 13

# s1="hello vardan patadiya"

# x=s1.split(" ")

# for i in x[::-1]:
#     print(i,end=" ")


# ---------revers string by word in one line code---------

# l1=" ".join(input("aaa ").split(" ")[::-1])
# print(l1)


# ----------revers string percharactor ---------

# l1 = " ".join(input(":")[::-1])
# print(l1)

# user=input(":")

# s=user.split(' ')

# for i in s[::-1]:
#     print(i,end=' ')

# s=str(i)

user = int(input("ENTER YEAR "))

# if user%400==0 and user%100==0 or user%4==0 and user%100!=0:
#     print("leap year")

# else:
#     print("not leap year")

i=print("leap year") if user%400==0 and user%100==0 or user%4==0 and user%100!=0 else print("noooo")

print(i)