 
class m_table:
   
    def __init__(self,u) :
        self.u=u
        for i in range(1,11):
            print(f"\n{u} X {i} = {u*i}\n")

    def info(self):
        print("you can see your table")

class table(m_table):
    def __init__(self,y):
        self.y=y
        for i in range(1,11):
            print(f"{y} X {i} = {y*i}")

    def info(self):
        super().info()        

x=m_table(11)
x.info()

y=table(10)
y.info()