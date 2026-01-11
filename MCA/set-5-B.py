import mysql.connector as mysql
import pandas as pd
import matplotlib.pyplot as pl
con = mysql.connect(host ="localhost" , user = "root" , password = "",database = "py_try")

cur = con.cursor()

# table = "CREATE TABLE c(id Integer ,name varchar(20),age Integer , fee Integer , mobile varchar(20) )"
# sql = "INSERT INTO c VALUES(%s,%s,%s,%s,%s)"

# data = [
#     (1,"Sameer",34,40000,"9032030301"),
#     (2,"Aryan",35,54000,"9911343989"),
#     (3,"Ram",34,45000,"981059357"),
#     (4,"Lata",36,60000,"991013998")
#     ]

data="SELECT * FROM c"

cur.execute(data)
all = cur.fetchall()

df = pd.DataFrame(all,columns=["id","name","age","fee","phone_num"])

print(df)
    
pl.bar(df["name"] , df["fee"])
pl.show()
pl.hist(df["age"] ,bins=5)
pl.show()
con.commit()
con.close()