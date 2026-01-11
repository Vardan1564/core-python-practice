class student:

    def __init__(self,name,):
        self.name=name 
    
    def info(self):
        name=['vardan','vijay','lalo','pratik','abhi']
        
        for index,i in enumerate(name,start=1):
            if self.name==i:
                print(f"Studant name==>>{i} ")
                print(f"Studant roll no.==>>  {index}")
        else:
                print("this studant is not in this class ")

s=student(input("ENTER NAME: "))
s.info()



    