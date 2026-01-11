from tkinter import *
from tkinter import messagebox

t=Tk()

t.geometry("1000x1000")


l1=Label(text="REGISTRATION",font=(20)).place(x=450,y=50)

l2=Label(text="Name",font=(20)).place(x=30,y=190)
t2=Entry(width=50).place(x=130,y=195)

l3=Label(text="surname",font=(20)).place(x=30,y=250)
t3=Entry(width=50).place(x=130,y=255)

var=IntVar()
ch=Checkbutton(text="c",variable=var, onvalue=1, offvalue=0,width=10)
ch.place(x=30,y=350)

var1=IntVar()
ch1=Checkbutton(text="c#",variable=var1, onvalue=1, offvalue=0,width=10)
ch1.place(x=90,y=350)

l4=Label(text="list",font=(20),height=2,width=4).place(x=30,y=450)

lb=Listbox(font=(20))
lb.insert(1,"hello")
lb.insert(2,"2hello")
lb.place(x=130,y=450)

t.mainloop()