class vip():
  def __init__(self,value):
    self.value =value

  def info(self):
    print(f"value is {self.value}")

  @property # it is getter use=>|get value |
  def v(self):
    return 10* self.value

  @v.setter # it is setter use=>|set value|
  def v(self,new_value):
    self.value=new_value/20

#class obj
a=vip(10)
# print value
a.info()
# getter value
print(a.v)
# setter value |or NEW VALUE|
a.v=int(input("ENTER THE NUMBER "))