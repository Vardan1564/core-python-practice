# import mysql.connector

# c=mysql.connector.connect(host='localhost',user='root',password='',database='smit')

# print(f"connected {c}")


# cur=c.cursor()

# # cur.execute("create table hello(id int , name varchar(20),city varchar(20))")

# # print("table is created .... !")

# cur.execute("insert into hello values(1,'vardan','khirasara')")

# # cur.execute("delete from hello where id=1")

# # cur.execute("update hello set name='lalo' where id=2")

# print(cur.rowcount)
# cur.execute("select * from hello")

# r=cur.fetchall()

# for i in r:
#     print(r)

# c.commit()


import mysql.connector

c=mysql.connector.connect(host='localhost',user='root',password='',database='smit')

print("connected")

cur=c.cursor()

# cur.execute("insert into hello values(6,'smit','rajkot')")
cur.execute("update hello set name='bhargv' where id=6")

# print("inserted")

cur.execute("select * from hello")

r=cur.fetchall()

for i in r:
    print(i)

c.commit()