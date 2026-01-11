import mysql.connector as mysql
import matplotlib.pyplot as pl
import pandas as pd;

con = mysql.connect(host = "localhost" , user ="root" , password = "", database ="py_try")

cur = con.cursor()

sql = "select * from emp"

cur.execute(sql)

data = cur.fetchall()

df = pd.DataFrame(data , columns=["id","name","dept","gender","experience","salary"])
print(df)

max_salary = df["name"][df["salary"].idxmax()]

print(max_salary)

avg = "select dept, AVG(salary) from emp group by dept"

cur.execute(avg)
data = cur.fetchall()

for i in data:
    print(i)

p = "select dept , count(*) from emp group by dept"
cur.execute(p)

data1 = cur.fetchall()
dept = []
total_emp = []
for i in data1:
    dept.append(i[0])
    total_emp.append(i[1])

pl.pie(total_emp ,labels=dept)
pl.show()