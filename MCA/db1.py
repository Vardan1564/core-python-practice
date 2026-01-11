import mysql.connector as mydb

con = mydb.connect(host="localhost",user="root",password="",database="py_try")

# if(mydb.connect()):
#     print("connected")
# else:
#     print("error")

cur = con.cursor()

# create table
# sql = "CREATE TABLE book (B_ID integer, Titel varchar(20), price integer)"

# insert 
# sql ="insert into book values(%s,%s,%s)"
# number_of_books = int(input("Enter number of books you want to enter : "))

# b1=[]
# for i in range(number_of_books):
    # bookid=int(input("Enter a Book ID : "))
    # name = input("Enter a Book Name : ")
    # price=int(input("Enter a Book price : "))
    # b1.append((bookid,name,price))

# delete
# sql = "delete from book where Titel = %s"
# title = input("Enter a Book name : ")
# D1=(title,)

# update
# sql = "update book SET Titel = %s where Titel = %s"
# old_book_name=input("Enter a old Book name : ")
# new_book_name=input("Enter a new Book name : ")
# U1=(new_book_name,old_book_name)

# cur.execute(sql,U1)
con.commit()


