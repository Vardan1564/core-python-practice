import mysql.connector

c=mysql.connector.connect(host='localhost',user='root',password='',database='smit')

print("connected",c)

cur=c.cursor()

# cur.execute("create database smit")

# print("database is created ")

# cur.execute("create table abc(id int,nm varchar(20))")

# print("table is created")

# cur.execute("insert into abc values(5,'vardan')")


print(cur.rowcount)

cur.execute("update abc set nm='lalo' where id=3")

cur.execute("select * from abc")

r=cur.fetchall()

for i in r:
    print(i)

c.commit()