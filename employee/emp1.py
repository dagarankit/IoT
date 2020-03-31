import tkinter
from tkinter import *
from tkinter import messagebox
import registration_window
def new():
    root=Tk()
    root.title("Menu")
    root.geometry("720x480+700+300")
    root.resizable(0,0)
    root['bg']='#F8E7BD'
    f1=Frame(root,height=100,width=200,bg='#766843')
    f1.pack(fill=X)
    l1=Label(f1,text="Haldiram's",font=("monotype corsiva",30,"italic","underline"),fg='white',bg='#766843')
    l1.place(x=245,y=30)

    def reg():
        root.destroy()
        registration_window.registerwindow()
    def insert():
        import money

    f2=Frame(root,height=250,width=450,bg='#F8E7BD')
    f2.place(x=135,y=100)
    b1=Button(f2,height=6,width=8,text="Register",font=("monotype corsiva",15),command=reg)
    b1.place(x=25,y=50)
    b1=Button(f2,height=6,width=8,text="Add Money",font=("monotype corsiva",15),command=insert)
    b1.place(x=285,y=50)
    root.mainloop()
