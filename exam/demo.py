# p =eval(input("Enter a P : "))
# r=eval(input("Enter a R : "))
# n=eval(input("Enter a N : "))

# print("Your interest : ",(p*r*n)/100)


# num1 = eval(input("Enter a number1 : "))
# num2 = eval(input("Enter a number2 : "))

# print(num1>num2)

# str=input("Enter a String : ")

# print("String in upper : ",str.upper())
# print("String in upper : ",str.lower())

# l=str.split(' ')

# print("Split string : ",l)


# s1 = input("Enter a s1 : ")
# s2 = input("Enter a s2 : ")
# count = s1.count(s2)

# if (count>0):
#     print("s2 is : ",count)
# else:
#     print("noo")

# print(count)
     

# s1 = input("Enter a s1 : ")

# print(len(s1.split()))

# word=s1.split(' ')
# c=0
# for i in range(len(word)):
#    c = c+1

# print(c) 

# user = input("Enter a name : ")
# s=('vardan',('smit'),('vijay'))

# for i in s:
#     for j in i:
#         if (user in i):
#             print('name : ',user)
#             break
#         else:
#             print("Noo")
#             break
        

# t1=tuple(i for i in range(11))
# even=[]
# odd=[]
# print(t1)

# for i in t1:
#     if i%2==0:
#         even+=[i,]
#     else:
#         odd+=[i,]

# print(even)
# print(odd)


# for i in range(10,0,-1):
#     print(i,end=' ',)
# print()
# print()
# for i in range(1,11):
#     print(i,end=' ')

# for i in range(5):
#     for s in range(5-i):
#         print(' ',end=' ')
#     for j in  range(i):
#             print("* ",end=' ')
#     print()

# str = input('Enter a String : ')

# print("replace o to @",str.replace('o','@'))

# st=('Pen', 'Marker', 'Pencil','Eraser','Scale')
# t=()
# for i in st:
#     t+=(i[::-1],)

# print(st)
# print(t)

# l=[]

# for i in range(5):
#     user = input("Enter name : ")
#     l+=[user,]

# print(l)

# l=['vardan','pratik','smit']

# for i in l:
#     if 'a' in i:
#         print(i)

# l=['vardan','smit','vijay']

# l=[1,32,4,5,6]
# l2=[1,32,4,5,6]
# f1= list(map(lambda a,b:a+b ,l,l2))
# f2=list(map(lambda a : a*a , l))
# print(f1)
# print(f2)

# m=lambda a,b : a if a>b else b

# print(m(12,3))
# s=[23,54,67,89,90]
# print(list(map(lambda r : 'A' if r>90 else 'B' if r>80 else 'C' if r>70 else 'D' if r>50 else 'Fail' , s)))

# l=[12,3,True,'vardan',23.4,'smit']

# print(list(filter(lambda name : type(name) == str , l)))

# d= {1:'vardan' , 2 : 'smit'}

# from functools import reduce

# l=[1,2,3,4,5]

# print(reduce(lambda a,b : a+b , l))

# d={}

# for i in range(2):
#     name = input("Enter a name : ")
#     age = eval(input("Enter a age : "))

#     d[i] = {name,age}
# print(d)


# num = eval(input("Enter a Numner : "))

# if(num > 2):
#     for i in range(2 , num):
#         if (num % i == 0):
#             print("Not prime : ",num)
#             break
#     else:
#         print("prime : ", num)
# else:
#     print("Enter number > 2")
 
l = []
for i in range(2):
    name = input("Enter a Name : ")
    age =eval(input("Enter a age : "))
    l += [i,[name,age]]
print(l)