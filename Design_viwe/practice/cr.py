# x=int(input("ENTER THE NUMBER : "))

# y=str(x)

# if (len(y)==3):
#     print("no is three digit")

# else:
#     print("no is not in three digit")
# if len(x):
#     print(x)

# else:
#     print("NUMBER IS NOT A THREE DUGIT")

# =========================================================

print("""
===================
Marks Grade
===================
0-34 Fail
35-59 Second Class
60-79 First Class
80-59 Dist""")
while True:
    i=input("enter yes for start | enter end for stop :")
    if i=="yes":
        marks=int(input("ENTER YOUR MARKS :"))

        if(marks==0 and marks<=34):
            print("you are fail")
        elif(marks>=35 and marks<=59):
            print("you are pass and your grade is | second class |")
        elif(marks>=60 and marks<=79) :
            print("you are pass and your grade is | first class |")
        else:
            print("you are pass and your grade is | dist class |")
    else:
        break

