# class InvalidInput(Exception):
#     pass

# try:
#     user = input("Enter a Some Data : ")
#     if user.isalpha():
#         print("Your Data : ",user)
#     else:
#         raise InvalidInput("same only text data only.....")
# except InvalidInput as e:
#     print("Error : ",e)


# import pandas as pd

# data = pd.read_csv("MCA\\stud.csv")
# df = pd.DataFrame(data)

# new_data = [{
#     "roll":6,
#     "name":"pratik",
#     "age":21,
#     "course":"BCA"
# }]
# print(df)

# df_new = pd.DataFrame(new_data)
# df.to_csv("MCA\\stud.csv",index=False)
# print(df.duplicated())

# print(df)
# import random as r

# l1 = [r.randint(1,100) for num in range(10)]
# print(l1)
# l2 = [r.randint(1,100) for i in range(10)]
# print(l2)
# com = []

# file = open("MCA/t1.txt","r")
# line = file.readlines()

# file_list = []
# for i in line :
#     data = i.strip().split(',')
    
# for i in data: 
#     file_list.append(int(i))

    
# print(file_list)
# for i in l1:
#     if i in file_list:
#         com.append(i)
# print(com) 

# import mysql.connector as mysql
# import matplotlib.pyplot as pl

# con = mysql.connect(host ="localhost", user = "root", password ="",database = "py_try")

# cur = con.cursor()

# sql = "select * from product"

# cur.execute(sql)

# data = cur.fetchall()
# name = []
# price = []
# for i in data:
#     print(i)
#     name.append(i[1])
#     price.append(i[2])

# print(name)
# print(price)

# col = []
# for i in price:
#     if i == max(price):
#         col.append("green")
#     else:
#         col.append("blue")


# pl.pie(price , labels=name)
# pl.title("Product price pie chart....")
# pl.show()

# pl.bar(name,price,color = col)
# pl.xlabel("name")
# pl.ylabel("price")
# pl.title("max price is in green color ....")
# pl.show()
# import pandas as pd
# Products = {
#     'p1': ['Pen', 10],
#     'p2': ['Eraser', 2],
#     'p3': ['Pencil', 5],
#     'p4': ['Notebook', 25],
#     'p5': ['Scale', 8],
#     'p6': ['Sharpener', 4],
#     'p7': ['Marker', 15],
#     'p8': ['Highlighter', 20]
# } 

# df  = pd.DataFrame(Products)

# print(df)

# for i in range(5):
#     for j in range(i):
#         print("*",end="")
#     print()

# s = input("enter a string : ")

# print("reverce string ",s[::-1])

# f=1
# for i in range(1,num+1):
#     f=f*i
# print(f)    

# num = int(input("Enter a number : "))
# sum=0
# for i in range(0,num+1):
#     sum=sum+i

# print(sum)

# s1 = input("Enter a string and check it's palindrome or not : ")

# if s1 == s1[::-1]:
#     print("string is palindrome")

# s1 = input("Enter a string : ")

# v = 0
# c = 0
# vowel = ('a','e','i','o','u')
# for i in s1:
#     if i in vowel:
#         v += 1
#     c += 1

# print("total vowels : ",v)
# print("total consonants ",c)

# num = input("Enter a number in word : ")

# words = num.split(' ')

# word_to_num ={
#     "zero": 0,
#     "one": 1,
#     "two": 2,
#     "three": 3,
#     "four": 4,
#     "five": 5,
#     "six": 6,
#     "seven": 7,
#     "eight": 8,
#     "nine": 9
# }
# for i in words:
#     if i in word_to_num:
#         print(word_to_num[i] , end =" ")
#     else:
#         print("plz Enter between 0 to 9 only...!")


# s1 = input("enter string : ")

# d= ""
# l= ""

# for i in s1:
#     if i.isalpha():
#         l += i
#     if i.isdigit():
#         d += i

# print(l+d)

x="hello"[0]
print(x)