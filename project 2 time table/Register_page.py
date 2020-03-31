""" This is the registeration page it is almost done """

import tkinter
from tkinter import *
from tkinter import messagebox
import the_login_page as lp
#from GUI_entry_windows_with_mySQL import *

import mysql.connector as mc



def register_check():
    x=e1.get()
    y=e2.get()
    z=e3.get()
    print("|{}||{}||{}|".format(x,y,z))
    if((x!= '')and( y != '')and(z!= '')):
        submit(x,y)
        messagebox.showinfo(title="Status",message="SUCCESFULLY ACCOUNT CREATED!")
        root2.destroy()
        lp.login_page()
       # return x,y,z
    else:
        messagebox.showinfo(title="status",message="FILL ALL THE BLANKS!")

def submit(x,y):
    name=x
    password=y
    db= mc.connect(host="192.168.43.252",database="list_of_students",user="root",password="sera")
    cur = db.cursor()
    cmd= "INSERT into users (name,password) values ('"+name+"','"+password+"');"
    cur.execute(cmd)
    db.commit()
    cur.close()
    db.close()                    

def go_back():
    yes_no = messagebox.askquestion("Don't want to create an account","Are you Sure?",icon='question')

    if yes_no == 'yes':
        root2.destroy()
        lp.login_page()
        
    
    
 

def registeration():
    global e1
    global e2
    global e3
    global root2
    root2 = tkinter.Tk()
    root2['bg']="skyblue"
    root2.title("Regiseration")
    root2.geometry("1600x1200")
    f_dis_reg=Frame(root2,height=350,width=500,bg="SpringGreen",bd=2,relief='solid')
    f_dis_reg.pack(fill=X)

    l_dis_reg=Label(f_dis_reg,text="REGISTERATION:FILL UP THE BLANKS",font=("TimesNewRoman",25,"bold"),bg="SpringGreen",fg="Red")
    l_dis_reg.pack()

    f_fillups=Frame(root2,height=600,width=800,bg="AliceBlue",bd=2,relief='solid')
    f_fillups.place(x=300,y=50)

    #Now the buttons and the labels and the entry


    l1=Label(f_fillups,text="Name      :",font=("TimesNewRoman",25,"bold"),width=10,bg="white",fg="black",bd=2,relief='solid')
    l1.place(x=50,y=60)
    l2=Label(f_fillups,text="Password :",font=("TimesNewRoman",25,"bold"),width=10,bg="white",fg="black",bd=2,relief='solid')
    l2.place(x=50,y=160)
    l3=Label(f_fillups,text="Email ID  :",font=("TimesNewRoman",25,"bold"),width=10,bg="white",fg="black",bd=2,relief='solid')
    l3.place(x=50,y=260)

    e1=Entry(f_fillups,font=("arial",18,"bold"),bg="white",width=20,bd=5)
    e1.place(x=280,y=60)
    e2=Entry(f_fillups,font=("arial",18,"bold"),bg="white",width=20,bd=5)
    e2.place(x=280,y=160)
    e3=Entry(f_fillups,font=("arial",18,"bold"),bg="white",width=20,bd=5)
    e3.place(x=280,y=260)

    b1=Button(f_fillups,text="Register",font=("arial",20,"bold"),command=register_check,bd=3,relief='raised')
    b1.place(x=100,y=360)
    b2=Button(f_fillups,text="Already have an Account",font=("arial",20,"bold"),bd=3,relief='raised',command=go_back)
    b2.place(x=250,y=360)
    root2.mainloop()

if __name__=='__main__':
    registeration()
