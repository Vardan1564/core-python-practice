# v=["vardan","dhairya","vijay","lalo","hrash\n"]
# for index,i in enumerate(v,start=1):
#     print(index,i) 

class gfather:
    def gfather(self,name):
        print("he is father..... ")

class gfson1(gfather):
    def son1(self):
        print("he is son of gfather")

class gfson2(gfather):
    def son2(self):
        print("he is son2 of gfather")

class son1(gfson1):
    def s1(self):
        print("he is son of gfson1")

class son2(gfson2):
    def s1(self):
        print("he is son of gfson2")

a=gfather("a")
print(a)

a1=gfson1("a to b")
print(a1)

a2=gfson2("a to b")
print(a2)

a3=son1("b to c")
print(a3)

a4=son2("b to c")
print(a4)