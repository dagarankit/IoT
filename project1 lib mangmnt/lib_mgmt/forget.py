import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc

def forget():

    root=tkinter.Tk()
    root.geometry("1366x768")
    root["bg"]="black"
    root["bd"]="30"
    root.title("Forget page")

    f1=Frame(root,height=700,width=1300,bg="#454545")
    f1.pack()


    def update():
        pss = e4.get()
        re = e5.get()

        if pss == re:
            print("in")
            usr=e1.get()

            db = mc.connect(host="localhost", user="deepak", password="deepak!@#", database="lib_mgmt")
            print("connected")
            cur = db.cursor()
            print("cursor created")
            print(usr,pss)
            print(type(pss))
            cmd="UPDATE students set pass=%s where login_id='"+usr+"';"

            print("command given")
            cur.execute(cmd)
            print("command executed")
            cur.close()
            db.close()
            print("close")

        else:

            messagebox.showinfo(title="ERROR", message="Password not match")




    def query():

        db=mc.connect(host="localhost",user="deepak",password="deepak!@#",database="lib_mgmt")
        cur=db.cursor()
        cmd="select * from students;"
        cur.execute(cmd)
        x=cur.fetchall()
        cur.close()
        db.close()
        id=e1.get()
        mob=e2.get()
        email=e3.get()
        l=0

        for i in x:
            global data
            data=i
            l+=1
            if (id==i[2] and mob==i[4]):

                l5 = Label(f1, text="New Password", font=("ubuntu", 20), bg="#454545", fg="white")
                l5.place(x=400, y=380)
                l6 = Label(f1, text="Re-Type", font=("ubuntu", 20), bg="#454545", fg="white")
                l6.place(x=400, y=430)
                global e4
                global e5
                e4 = Entry(f1, bg="white", width=25, font=("URW gothic L", 15, "bold"))
                e4.place(x=600, y=380)
                e5 = Entry(f1, bg="white", width=25, font=("URW gothic L", 15, "bold"))
                e5.place(x=600, y=430)

                b2 = Button(f1, text="Submit", font=("ubuntu", 15), command=update)
                b2.place(x=550, y=500)
                b3 = Button(f1, text=" Login ", font=("ubuntu", 15), command=query)
                b3.place(x=745, y=500)

                break

            if l==len(x):
                messagebox.showinfo(title="Error", message="Input Data Not Match")


    l1=Label(f1,text="Forget Password",font=("ubuntu",30),bg="#454545",fg="white")
    l1.place(x=500,y=50)
    l2=Label(f1,text="User ID*",font=("ubuntu",20),bg="#454545",fg="white")
    l2.place(x=400,y=150)
    l3=Label(f1,text="Mobile No*",font=("ubuntu",20),bg="#454545",fg="white")
    l3.place(x=400,y=200)
    l4=Label(f1,text="Email ID*",font=("ubuntu",20),bg="#454545",fg="white")
    l4.place(x=400,y=250)

    e1=Entry(f1,bg="white",width=25,font=("URW gothic L",15,"bold"))
    e1.place(x=600,y=150)
    e2=Entry(f1,bg="white",width=25,font=("URW gothic L",15,"bold"))
    e2.place(x=600,y=200)
    e3=Entry(f1,bg="white",width=25,font=("URW gothic L",15,"bold"))
    e3.place(x=600,y=250)

    b1=Button(f1,text="Forget",command=query,font=("ubuntu",15))
    b1.place(x=650,y=320)

    root.mainloop()