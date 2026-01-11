class patadiya:
    def __init__(self,name) :
        self.name=name

class p1(patadiya):
    def __init__(self, name,fathername):
        patadiya.__init__(self,name="vardan")
        self.fathername=fathername

class p2(patadiya):
    def __init__(self, surname,fatheername):
        p1.__init__(self,fathername="vardan")
        self.surname=surname

a=p2("patadiya")
print(a)