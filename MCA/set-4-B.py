import mysql.connector as mysql
import matplotlib.pyplot as pl

con = mysql.connect(host = 'localhost' , user = 'root' , password = '' , database = 'py_try')

# if (con):
#     print("DOne")

# pro = [
#     (1,'tv',20000),
#     (2,'phone',10000),
#     (3,'laptop',30000),
#     (4,'headphone',3000)
# ]

cur = con.cursor()

# sql = "insert into product values(%s,%s,%s)"

# cur.executemany(sql,pro)

# x------------x-------------------x-----------x
# display using p_id and get user input

# id = int(input("enter a Product id : "))
# sql = "select * from product where p_id = %s"

# cur.execute(sql, (id,))

# r = cur.fetchall()
# for i in r:
#     print(i)

# x------------x-------------------x-----------x

sql = "SELECT name,price from product"
cur.execute(sql)
p_data = cur.fetchall()
con.close()

name = []
price = []

for i in p_data:
    name.append(i[0])
    price.append(i[1])
print("name of product : ",name)
print("price of product : ",price)

pl.pie(price,labels=name)
pl.show()