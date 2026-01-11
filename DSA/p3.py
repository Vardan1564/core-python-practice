# import random
# l1=[['-> what is sum of 1+9'],[' -> what is multiphcation of 2x2']]
# ans=['10','4']

# r=random.choice(l1)
# Q1=input("ENTER YES FOR START AND NO FOR STOP: ")



# while True:
#     if Q1=='no':
#         break
#     else:
#         print(r)
#         a1=input("ENTER YOUR ANS : ")
#         print(a1)
#         if (a1 in ans):
#             print("YOUR ANS IS RIGHT ",Q1)
#         else:
#             print("YOUR ANS IS RONGE")

# for i in range(5,0,-1):
#     for j in range(i):
#         print(i,end=" ")
#     print("\n")
# for k in range(6):
#     for y in range(k):
#         print(k,end=" ")
#     print("\n")

# n=int(input("ENTER A NUMBER:"))
# for i in range(1, n + 1):
#         # Print leading spaces
#         for j in range(n - i):
#             print(" ", end="")
        
#         # Print asterisks for the current row
#         for k in range(1, 2*i):
#             print("*", end="")
#         print()

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print()



for i in range(6,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()