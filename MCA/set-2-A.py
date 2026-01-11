student =[]
class InvalidName(Exception):
    pass
try:
    num_stud = int(input("Enter a Number of Student you want to enter : "))
    for i in range(num_stud):
        name = input("Enter a Student name : ")
        if(not name.isalpha()):
             raise InvalidName("Name must be contain letter. ")
        else:
            student.append(name)
    print(student)
except InvalidName as e: 
    print("Error : ",e)
except ValueError:
    print("plz enter a valid number")

vowel = []
def count_v(name):
    v = 'aeiouAEIOU'
    c = 0
    for i in name:
        if i in v:
            c +=1
    vowel.append(c)
for name in student:
    count_v(name)
    
print(student)
print(vowel)