import random


def check(com,user):
    if (user==com):
        return 0
    if (user==0 and com==2):
        return -1
    if (user==1 and com==0):
        return -1
    if (user==2 and com==1):
        return -1
    return 1

user=int(input("ENTER 0 FOR SNAKE, 1 FOR WATER AND 2 FOR GUN: "))
com=random.randint(0,2)

result= check(com,user)

print(f"your choise {user}")
print(f"computer choise {com}")

if (result==0):
    print("draw")
elif(result==-1):
    print("you losssss")
else:
    print("you wonnnn")