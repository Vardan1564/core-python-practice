# def prime(a):
     

#     for i in range(2,a):
#         if a%i==0:
#            return False
            
#         else:
#             return True
        
# if prime(int(input("NO: "))):
#     print("prime ")
# else:
#     print("no")

# -------list--------------

# l1=[12,3,45,5,34,56,787,98]
# l2=[]
# a=sorted(l1)
# print(a)
# l2.append(a)
# print(l2)

# x= 12 in l1
# print(x)

# comprenersion
# x=int(input(":"))
# l1=[2*i for i in range(1,int(input(":")))]
# print(l1)

# l1=["vardan" for i in range(1,10+1)]
# print(l1)

# ----------give info using name -----------

l1=[["vardan","patadiya","90164 10956"],["dhairya","chouna","65455 12548"],["pratik","chotaliya", "65879 54681"]]
user=input("ENTER THE NAME AND YOU CAN GET INFO ADOUT :")

if user=="vardan":
    print(l1[0])
elif user=="dhairya":
    print(l1[1])
elif user=="pratik":
    print(l1[2])
else:
    print("---------------------------")
    print("THIS NAME IS NOT EXIST")
    print("CHECK ANTHER NAME")
    print("---------------------------")