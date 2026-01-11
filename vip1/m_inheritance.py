class emp:
    def __init__(self,emp_name):
        self.emp_name=emp_name
    def info(self):
        print(f"the emp name is {self.emp_name}")

class ad:
    def __init__(self,ad_name):
        self.ad_name=ad_name
    def info(self):
        print(f"the admin name is {self.ad_name}")

class combo(emp,ad):
    def __init__(self, emp_name,ad_name):
        self.emp_name=emp_name
        self.ad_name=ad_name

o1=combo("Dhairya","Vardan")
o1.info()
print(combo.mro())