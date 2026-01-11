import mysql.connector as mysql

con = mysql.connect(host ="localhost",user="root",password="",database="py_try")
cur=con.cursor()
def check_con():
    if(mysql.connect()):
        print("Connected successfully....")
    else:
        print("error..........:(")

def insert_book():
    if(mysql.connect()):
        sql = "INSERT INTO book VALUES(%s,%s,%s)"
        
        id=int(input("Enter a Book ID : "))
        name=input("Enter a Book Name : ")
        price=int(input("Enter a Book Price : "))

        book=(id,name,price)
        cur.execute(sql,book)
        con.commit()
    else:
        print("connection error..........:(")

def update_book():
    if(mysql.connect()):
        sql = "UPDATE book SET Titel= %s where Titel=%s"
        old_book_name=input("Enter a old Book Name : ")
        new_book_name=input("Enter a new Book Name : ")

        Update_book_name=(new_book_name,old_book_name)
        cur.execute(sql,Update_book_name)
        con.commit()
    else:
        print("connection error.....:(")

def delete_book():
    if(mysql.connect()):
        sql = "delete from book where Titel = %s"
        book_name=input("Enter a Book Name : ")
        d1=(book_name,)
        cur.execute(sql,d1)
        con.commit()
    else:
        print("connection error.....:(")
    
def display():
    if(mysql.connect()):
        sql = "SELECT * FROM book"
        cur.execute(sql)
        result=cur.fetchall()
        
        for books in result:
            print(books)
    else:
        print("connection error.....:(")


while True:
    print("---------------------------------")
    print("1. Check connection ")
    print("2. Display Data")
    print("3. Insert/Add Book")
    print("4. Update Book Name")
    print("5. Delete Book ")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        check_con()
    elif ch == 2:
        display()
    elif ch == 3:
        insert_book()
    elif ch == 4:
        update_book()
    elif ch == 5:
        delete_book() 
    elif ch == 6:
        break
    else:
        print("Other options not implemented yet.")

con.close()  
