class vector:
    def __init__(self,a,b,c) :
        self.a=a
        self.b=b 
        self.c=c 
    
    def __str__(self) :
        return f"{self.a}a + {self.b}b + {self.c}c"
    
    def __add__(self,i):
        return vector(self.a+i.a , self.b+i.b , self.c+i.c)
    
v1=vector(int(input("Enter Any Three Number: ")),(int(input("Enter Any Three Number: "))),(int(input("Enter Any Three Number: "))))
print(v1)

v2=vector(int(input("Enter Any Three Number: ")),(int(input("Enter Any Three Number: "))),(int(input("Enter Any Three Number: "))))
print(v2)

print(v1+v2)