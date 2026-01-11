class NumberError(Exception):
    pass

user_list= []
try:
    for string in range(2):
        user_in =  input("Enter a name : ")

        if (user_in.isdigit()):
            raise NumberError("Enter only string not number")
        else:
            user_list.append(user_in)
            
except NumberError as n:
    print("Error : ",n)

print("your input  : ",user_list )