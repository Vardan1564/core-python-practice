import random
l1 = [random.randint(1,100)  for i in range(10)]
l2 = [random.randint(1,100)  for i in range(10)]
def comman():
    comman = []
    for i in l1:
        if i in l2:
            comman.append(i)
    print("comman :",comman)  

    # now check is prime or not
    p = []
    for i in comman:
        if prime(i):
            p.append(i)
    if len(p)<=0:
        print("No prime ")
    else:
        print("prime : ",p)


def prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

print("list 1: ",l1)
print("list 1: ",l2)
comman()
        
