class library:
    def __init__(self,book):
        self.book=book
        self.value = len(book)

    def info(self):
        if self.book==self.book:
            print(f"Books are  {self.book} ")
            print(f"no. of books {self.value}")
        else :
            print("books is not mach than ENTER books retuen... ")

l=[]
n=int(input("ENTER NUMBER FOR YOU WANT TO ENTER BOOKS:"))
for i in range(1, n+1):
    print(f"ENTER THE BOOKS: {i}")
    ele= input()
    l.append(ele)
o=library(l)
o.info()