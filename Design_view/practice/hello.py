total_a=int(input("enter total amount : "))
print("-"*20)
interest=float(input("enter interest : "))
print("-"*20)
year=int(input("enter year : "))
print("_"*20)
print("-"*20)
c=(total_a*interest*year)/100


if  c>=1 and c<=1000:
    print("your interest is v good ")
    print("-"*20)
    print("your interest rate is ",c)

elif c>1000 and c<=5000:
    print("your interest is good ")
    print("-"*20)
    print("your interest rate is ",c)

elif c>5000 and c<=10000:
    print("your interest is not a Bad ")
    print("-"*20)
    print("your interest rate is ",c)

else:
    print("your interest is so high ")
    print("-"*20)
    print("your interest rate is ",c)