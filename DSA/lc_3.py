# ----------class & object ------------

class test: # test is a class object
    x=5  # class object variable / it also call static object 
    
    def f1():
        print("hello")
    
    def __init__(self,a,b) :
        self.a=a
        self.b=b
        # a and b both local variable
        # self.a and self.b both are instace object variable
        
        

    def f1(self):
        print(self.a,self.b)    # instace method

    @staticmethod
    def f2():
            pass

    @classmethod
    def f3(self1):
            print(self1.x)

# t1 is a instance object
# t1=test(12,12)

# # call instance method  f1()
# t1.f1()

# # call class method f3() / it call using class name 
# test.f3()

# print(type(t1.a))

class emp:
     def __init__(self,emp_name=None,emp_id=None,emp_salary=None) :
          pass