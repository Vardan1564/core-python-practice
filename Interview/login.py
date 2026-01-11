username = "vardan"
password = "123456"

loginAttempts  = 0 


for i in range(3):
    name = input("Enter a Username : ")
    userpass = input("Enter a password : ")
    if name == username and userpass == password:
        print("login succefully")
        break
    else: 
        if i == 2:
            print("Account Locked")
            break
        else:
            print("Try Again!!")

