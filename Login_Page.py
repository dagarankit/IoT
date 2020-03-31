import mysql.connector as mc
import tkinter
from tkinter import *
import register
import selectbook
import forget
from tkinter import messagebox





def log():


    def login():

        x=e1.get()
        y=e2.get()
        db=mc.connect(host="localhost",user="deepak",database="lib_mgmt",password="deepak!@#")
        cur=db.cursor()
        cmd="select * from students;"
        cur.execute(cmd)
        z=cur.fetchall()
        l=0

        for i in z:

            l+=1
            if x==i[2] and y==i[6]:

                messagebox.showinfo(title="Welcome", message="Hi! welcome to ISSUE portal")
                log.destroy()
                selectbook.sel()
                break

            if l==len(x):

                messagebox.showinfo(title="ERROR", message="User name or Password incorrect")

        db.commit()
        cur.close()
        db.close()

    def reg():
        log.destroy()
        register.reg()


    def forg():
        log.destroy()
        forget.forget()

    log=tkinter.Tk()
    log.title("Home Login")
    log.geometry("1366x768")
    log["bg"]="black"
    log["bd"]="150"

    f1=Frame(log,bg="black",height="500",width="900")
    f1.pack(side="top")

    l1=Label(f1,text=("Login Page"),font=("arial",50),bg="black",fg="white")
    l1.place(x=300,y=130)
    l2=Label(f1,text=("User Name"),font=("arial",25),bg="black",fg="white")
    l2.place(x=270,y=230)
    l3=Label(f1,text=("Password"),font=("arial",25),bg="black",fg="white")
    l3.place(x=270,y=280)

    e1=Entry(f1,bg="white",width=15,font=("arial",15),bd=2)
    e1.place(x=500,y=240)
    e2=Entry(f1,bg="white",width=15,font=("arial",15),bd=2,show="*")
    e2.place(x=500,y=290)

    b1=Button(f1,text="     Login     ",font="10",bg="white",fg="black",command=login)
    b1.place(x=420,y=350)
    b2=Button(f1,text="        Register      ",font="10",bg="white",fg="black",command=reg)
    b2.place(x=300,y=400)
    b3=Button(f1,text="Forget password",font="10",bg="white",fg="black",command=forg)
    b3.place(x=490, y=400)

    log.mainloop()

log()
