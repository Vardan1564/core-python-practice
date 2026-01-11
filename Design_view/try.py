import mysql.connector

c=mysql.connector.connect(host='localhost',user='root',password='',database="hello")


print("connected",c)

cur=c.cursor()

# cur.execute("CREATE TABLE xyz(id int ,nm varchar(50), surname varchar(50))")

# print("table is created....!")

cur.execute("insert into xyz values(1,'vardan','patadiya')")

print(cur._rowcount)

cur.execute("select * from xyz")

result=cur.fetchall()
for row in result:
    print(row)
c.commit()
