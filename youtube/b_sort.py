import matplotlib 
from matplotlib import pyplot as p 

day = [1,2,3,4,5]
s=[5,8,6,3]
color = ['r','g','b','y']
lable=['sleep','eating','enjoy','movie']
p.pie(s,  labels=lable  ,colors=color  ,
      startangle=50,  explode=(0,0.2,0,0),
      shadow=True, autopct="%1.1f%%")
p.axis("equal")
p.legend(loc=3)
p.show()
