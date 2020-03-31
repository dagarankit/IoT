""" This project is for creating a app such that this page here is
    it's login page , here you can also register if you are new using app.
    * upon the click of register buton a window will show with entry for name and password , and have to save those data in some variable
    * upon login a page should come with four inputs that can change the status of the the fan,cooler ,ac and light
"""



#This page will have the data saving variable and the Login window

import tkinter
from tkinter import *
from tkinter import messagebox


import Register_page as rp
import Main_Frame_GUI as mf


#---------------mysql connection
import mysql.connector as mc


def data():
    print("welcome")
    db=mc.connect(host="192.168.43.252",database="list_of_students",user="root",password="sera")
    cur =db.cursor()
    cmd="select * from users"
    cur.execute(cmd)
    x=cur.fetchall()
    print(x)
    db.commit() # save the Database
    cur.close()
    db.close()
    return x


#---------------


#def print_user()

#    for i in range(size(users)):
#        print("|{}|".format(users[i]),end=",")

def verify():

    x=e1.get()
    y=e2.get()
    print(x)
    print(y)

#---------Defining name and password
    users=data()
    name=list(range(len(users)))
    password=list(range(len(users)))
    for i in range(len(users)):
        name[i]=users[i][1]
    for i in range(len(users)):
        password[i]=users[i][2]

    state=0  
    for i in range(len(users)):
        if(x== name[i] and y == password[i]):
            messagebox.showinfo(title="welcome ",message="Welcome {}".format(e1.get()))
            root.destroy()
            mf.the_main_frame()
            break
        if i== len(users)-1 :
            state= 1
    if state == 1:    
        messagebox.showinfo(title="error",message="Invalid Entry")
#Destroy the root here

def register():
    root.destroy()
    rp.registeration()


def login_page():
    global e1
    global e2
    global root
    root =tkinter.Tk()
    root['bg']="skyblue"
    root.title("GIIST")
    root.geometry("1600x1000")

    f1=Frame(root,height=100,width=500,bg="SpringGreen",bd=2,relief='solid')
    f1.pack(fill=X)

    f2=Frame(root,height=400,width=800,bg="AliceBlue",bd=2,relief='solid')
    f2.place(x=350,y=100)

    l1=Label(f1,text="THE GREAT INDIAN INSTITUTE OF SCIENCE AND TECHNOLOGY",font=("TimesNewRoman",25,"bold"),bg="SpringGreen",fg='red')
    l1.place(x=300,y=10)

    l2 = Label(f2,text="LOGIN ID",font=("TimesNewRoman",20,"bold"),width=10,fg="blue",bg='white',bd='2',relief='solid')
    l2.place(x=150,y=100)

    l3 = Label(f2,text="PASSWORD",font=("TimesNewRoman",20,"bold"),width=10,fg="blue",bg='white',bd='2',relief='solid')
    l3.place(x=150,y=200)

    e1=Entry(f2,font=("arial",25,"bold"),bg="white",width=10,bd=5)
    e1.place(x=400,y=100)

    e2=Entry(f2,font=("arial",25,"bold"),bg="white",width=10,show="@",bd=5)
    e2.place(x=400,y=200)


    b1=Button(f2,text="LOG IN",font=("arial",14,"bold"),width=8,command=verify,bd=3,relief='raised')
    b1.place(x=170,y=250)

    b2=Button(f2,text="REGISTER",font=("arial",14,"bold"),width=8,command=register,bd=3,relief='raised')
    b2.place(x=170,y=300)
    root.mainloop()

#Entry box always return a string
# ? strongly private ,private and system defined private



if __name__ == "__main__":
    login_page()
    
