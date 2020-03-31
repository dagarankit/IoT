import tkinter
import time
from tkinter import messagebox
from tkinter import *
import urllib
import sys

global var
global b1
def registerwindow():
    def submit():
        f = e1.get()
        m = e2.get()
        a = e3.get()
        p = e4.get()
        global var
        http=urllib.PoolManager()
        if(f=="" or m=="" or a==""or p==""):
            messagebox.showinfo(title="Error",message="All fields are not filled")
        else:
            global var
            print(var)
            string=""
            for i in var:
                string+=str(i)
            print(string)
            print(type(string))
            #string=str(504848485067655170555356)
            print(sys.getsizeof(string))
            w=http.request('GET',"dhanajay.000webhostapp.com/HALDIRAM/updatestatus1.php?NAME="+f+"&PASSWORD="+p+"&PHONE_NUMBER="+m+"&ADDRESS="+a+"&Amount=200&RFID="+string)
            data=w.data.decode('utf-8')
            w.close()
            if data=="success":
                messagebox.showinfo(title="Done",message="Registration successful")
                root.destroy()
            else:
                messagebox.showerror(title="Error",message="OOPS! Something went wrong.")
                
    def scan():
        global var
##        var=[245,456,34,34]
##        
        import serial
        ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)
        while(1):
            x=list(ser.readall())
            print(x)
            if(x != []):
                var=x
                break
        b1=Button(f4,text="Register",font=("Times New Roman",15),bd=4,bg="white",fg=("black"),command=submit)
        b1.place(x=180,y=2)
        

    import serial
    
    root  = tkinter.Tk()
    root.title("New Registration")
    root.geometry("520x620+300+50")
    root['bg'] = "dark red"
    root.resizable(0,0)
    def cancel():
        root.destroy()
        import emp


    # Frame 1
    f1 = Frame(root,height=150,width=250,bg = 'dark red')
    f1.pack(side=TOP)
    f1.pack(fill=X)
    # Label 1
    l1 = Label(f1,text = "REGISTRATION PAGE",font = ("Times New Roman",25),bg="dark red",fg="white")
    l1.place(x=90,y=100)
    # Frame 2
    f2 = Frame(root,height=400,width=500,bg = 'dark red')
    f2.place(x=65,y=200)
    # Label 2
    l2 = Label(f2,text = "Full Name:",height=2,font = ("Times New Roman",20),bg="dark red",fg="white")
    l2.pack()
    # Label 3
##    l3 = Label(f2,text = "Email:",height=2,font = ("Times New Roman",20),bg="dark red",fg="white")
##    l3.pack()
    # Label 4
    l4 = Label(f2,text = "Mob. Number:",height=2,font = ("Times New Roman",20),bg="dark red",fg="white")
    l4.pack()
    # Label 5
    l5 = Label(f2,text = "Address:",height=2,font = ("Times New Roman",20),bg="dark red",fg="white")
    l5.pack()
    # Label 6
    l6 = Label(f2,text = "Password:",height=2,font = ("Times New Roman",20),bg="dark red",fg="white")
    l6.pack()
    # Frame 3
    f3 = Frame(root,height=340,width=250,bg = 'dark red')
    f3.place(x=233,y=200)
    # Entry 1
    e1=Entry(f3,bg="white",width=16,bd=4.5,font=("arial",18))
    e1.place(x=10,y=15)
    # Entry 2
    e2=Entry(f3,bg="white",width=16,bd=4.5,font=("arial",18))
    e2.place(x=10,y=82)
    # Entry 3
    e3=Entry(f3,bg="white",width=16,bd=4.5,font=("arial",18))
    e3.place(x=10,y=151)
    # Entry 4
    e4=Entry(f3,bg="white",width=16,bd=4.5,font=("arial",18))
    e4.place(x=10,y=220)
    # Entry 5
##    e5=Entry(f3,bg="white",width=16,bd=4.5,font=("arial",18))
##    e5.place(x=10,y=290)
    # Frame 4
    b3=Button(f3,width=30,text="Scan Your Card",font=("Times New Roman",10),bd=4,bg="white",fg=("black"),command=scan)
    b3.place(x=10,y=290)
    f4 = Frame(root,height=50,width=419,bg = 'dark red')
    f4.place(x=64,y=543)
    # Button 1
##    b1=Button(f4,text="Register",font=("Times New Roman",15),bd=4,bg="white",fg=("black"),status=DISABLED,command=submit)
##    b1.place(x=180,y=2)
    # Button 2
    b2=Button(f4,text="Cancel",font=("Times New Roman",15),bd=4,bg="white",fg=("black"),command=cancel)
    b2.place(x=320,y=2)
    root.mainloop()

