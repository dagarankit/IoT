import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
import proceedpage
def sel():

    def proceed(book1, book2):
        root.destroy()
        proceedpage.proceed(book1, book2)


    def page():
        global root
        root = tkinter.Tk()
        root.title("Select Book")
        root.geometry("720x480")
        root['bg'] = "#424242"
        f1 = Frame(root, height="800", width="800", bg="#424242")
        f1.pack(fill=X)

        l1 = Label(f1, text="Select Your Desired book here", font=("arial", 25), bg="#424242", fg="white")
        l1.pack()

        f1 = Frame(root, height="800", width="800", bg="#424242")
        f1.place(x=50, y=50)

        #Select Book1

        l1 = Label(f1, text="Select Branch : ", font=("arial", 10), bg="#424242", fg="white")
        l1.place(x=50, y=50)

        defop5 = StringVar(f1)
        choice = ["CSE", "ME", "CE", "ECE"]
        defop5.set(choice[0])

        dd = OptionMenu(f1, defop5, *choice)
        dd.place(x=150, y=45)

        def getbooks1():
            global defop1
            print(defop5.get())
            db = mc.connect(host="localhost", database="lib_mgmt", user="deepak", password="deepak!@#")
            cur = db.cursor()
            cmd = "select * from books where branch='" + defop5.get() + "' and quantity>0"
            cur.execute(cmd)
            x = cur.fetchall()
            defop1 = StringVar(f1)
            choice1 = []
            for i in range(len(x)):
                choice1.append(x[i][2])
                print("choice1 : ")
                print(choice1)
            defop1.set(choice1[0])
            l1 = Label(f1, text="Select Book : ", font=("arial", 10), bg="#424242", fg="white")
            l1.place(x=50, y=100)

            dd = OptionMenu(f1, defop1, *choice1)
            dd.place(x=150, y=95)
            print(x)
            db.commit()
            cur.close()
            db.close()

        b1 = Button(f1, text="Get Books", command=getbooks1)
        b1.place(x=250, y=47)

        ## select book 2
        l2 = Label(f1, text="Select Branch : ", font=("arial", 10), bg="#424242", fg="white")
        l2.place(x=50, y=150)

        defop = StringVar(f1)
        choice = ["CSE", "ME", "CE", "ECE"]
        defop.set(choice[0])

        dd = OptionMenu(f1, defop, *choice)
        dd.place(x=150, y=145)

        def getbooks2():
            global defop2
            db = mc.connect(host="localhost", database="lib_mgmt", user="deepak", password="deepak!@#")
            cur = db.cursor()
            cmd = "select * from books where branch='" + defop.get() + "' and quantity>0"
            cur.execute(cmd)
            x = cur.fetchall()
            defop2 = StringVar(f1)
            choice1 = []
            for i in range(len(x)):
                choice1.append(x[i][2])
                print("choice1 : ")
                print(choice1)
            defop2.set(choice1[0])
            l1 = Label(f1, text="Select Book : ", font=("arial", 10), bg="#424242", fg="white")
            l1.place(x=50, y=200)

            dd = OptionMenu(f1, defop2, *choice1)
            dd.place(x=150, y=195)
            print(x)
            db.commit()
            cur.close()
            db.close()

        b2 = Button(f1, text="Get Books", command=getbooks2)
        b2.place(x=250, y=147)

        but = Button(f1, text="Click to proceed....", command=lambda: proceed(defop1.get(), defop2.get()))
        but.place(x=200, y=250)

        root.mainloop()


    page()

