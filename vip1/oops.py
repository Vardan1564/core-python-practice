class form:

    name="vardan"
    surname="patadiya"
    age=19
    phone_no=0000000000
    work="developer"

#----------------   
 
    def info(self):
        print(f"{self.name} is a {self.work} and phone no. is a{self.phone_no} and age is {self.age}")

a=form()
a.name=input("ENTER THE NAME      : ")
a.surname=input("ENTER THE SURNAME: ")
a.work=input("ENTER YOUR WORK     : ")

# -------------

if (a.name=="" or a.surname=="" or a.work==""):
    print("plzz enter your name  ,  surname ,  work")

else:
    print("thenks for rgister our form ")

# ---------------

a.info()