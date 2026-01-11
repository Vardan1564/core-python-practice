from tkinter import *

t=Tk()
width=t.winfo_screenmmwidth()
height=t.winfo_screenheight()
t.geometry("%dx%d" % (height,width))


title=Label(text="WELCOME TO LOGIN FORM",font=(80)).place(x=270,y=10)
l=Label(text="____________________________________________________________").place(x=255,y=35)

l1=Label(text="USER NAME :",font=(30)).place(x=170,y=150)
l2=Label(text="PASSWORD  :",font=(30)).place(x=170,y=200)

t1=Entry(width=35,font=(30)).place(x=350,y=150)
t2=Entry(width=35,font=(30)).place(x=350,y=200)

def newwin():
    win=Tk()
    win.geometry("1000x1000")

    title=Label(win,text="ADMIN",font=(300)).place(x=500,y=10)
    

    win.mainloop()

b1=Button(text="SUBMIT",font=(30),command=newwin).place(x=170,y=300)

t.mainloop()