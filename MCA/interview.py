# a=10
# b=20


# print("old")
# print("A = ",a)

# print("B = ",b)

# a,b = b,a

# print("new")
# print("A = ",a)

# print("B = ",b)

s1 = "vardan"
# rev=""
# for i in s1:
#     rev = i+rev
# print(rev)

# print(s1[::-1])

# ======================================

# Strings:
# Palindrome check

# s1 = input("Enter a String : ")
# p = ""

# for i in s1:
#     p = i+p

# if s1 == p:
#     print("yes")
# else :
#     print("no")

# ======================================

# arr = [1,3,2,4,2,1,4,3,1]

# result = []

# for i in range(len(arr)):
#     duplicate = False

#     for j in range(i):
#         if arr[i] == arr[j]:
#             duplicate = True
#             break

#     if not duplicate:
#         result.append(arr[i])

# print(result)

# a=10
# b=20
# c=5
# cou = 0
# while(a or b or c):
#     cou = cou+1
#     if a>0:
#         a = a-1
#     if b>0:
#         b = b-1
#     if c>0:
#        c = c-1

# print(cou)
# for i in range(1,5):
#     for j in range(i):
#         print("*", end="")
#     print()

# s1= input("enter a String : ")
# find = input("Enter \"one\" charater only \n that you want to get index : ")
# c=0
# for i in s1:
#     c = c+1
#     if find == i:
#         print("index is : ",c,"char is : ",find)
#         break
#     else:
#         print("this char is nothing in your string.....sorry")    
    
# a=10
# b=20
# c=30
# count =0
# while(a or b or c):
#     count= count+1
#     if (a != 0):
#         a = a-1
#     if ( b != 0):
#         b = b-1
#     if (c != 0):
#         c= c-1
    
# print(count)
l1 = [2,4,3]
l2 = [5,6,4]
s1 = ""
s2 = ""
for i in l1[::-1]:
    s1 = s1 + str(i)
for i in l2[::-1]:
    s2 = s2 + str(i)

print(int(s1)+int(s2))