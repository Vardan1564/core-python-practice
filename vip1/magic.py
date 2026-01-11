class stud:
    def __init__(self,name):
        self.name=name

    def __len__(self):
        i=0
        for i in self.name:
            i=i+1
        return i
    
    def __str__(self):
        return f"the name is {self.name}"
    
    def __repr__(self):
        return f"the name is (-->'{self.name}<--')"
    

a=stud("vardan")   
print(a)
        
