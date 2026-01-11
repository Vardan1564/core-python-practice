import random


def check(com,user ):
    if com==user:
        return 0
    if (com==0 and user== 2):
        return -1 
    if (com==1 and user==0):
        return -1
    if (com==2 and user==1):
        return -1
    
    return 1



com=random.randint(0,2)
user =int(input("""ENTER 
-----------------------------
0 FOR stone->👍
-----------------------------
1 FOR paper->📄: 
-----------------------------
2 FOR scissor->✂️:==> """))
                 

s=check(com,user)

print("-------------------------------------------------")

print("YOUR choise: ",user)
print("Computer choise: ",com)

print("-------------------------------------------------")

if(s==0):
    print("DRAW")
elif(s==-1):
    print("You lose")
else :
    print("You wonnnnnn")

print("-------------------------------------------------")
    






