import tkinter
from tkinter import *
from tkinter import messagebox
import urllib3
import menu
root=tkinter.Tk()
root.title("Login Here")
root.geometry("600x500+100+100")
root["bg"]="black"
root.resizable(0,0)
global stri
def loginwindow():
    def scan():
        global stri
        stri=""
        e2.config(state=NORMAL)
        b1.config(state=NORMAL)
        ####RFID CODE YAHAN PE IKHNA HAI
        import serial
        ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)
        stri=""
        while(1):
            x=list(ser.readall())
            print(x)
            if( x!= []):
                break
        for i in x:
            stri+=str(i)
        
    def login():
        baseURL="http://kshamaiot.000webhostapp.com/HALDIRAMS/getstatus1.php?RFID="+stri
        http=urllib3.PoolManager()
        r=http.request('GET',baseURL)
        data=r.data.decode('utf-8')
        print(data)
        p=e2.get()
        if(data==p):
            messagebox.showinfo(title="INFO",message="Login Successful")
            root.destroy()
            menu.menu(stri)
        else:
            messagebox.showerror(title="Error",message="Either password is incorrect or you are not registered")
            e1.delete(0,'end')
            e2.delete(0,'end')
            
    f1=Frame(root,bg="black",height=200,width=700)
    f1.pack(side="top")
    l1=Label(f1,text="WELCOME TO HALDIRAM'S",font=("Times New Roman",25),bg="black",fg="white")
    l1.place(x=90,y=70)
    f2=Frame(root,bg="black",height=250,width=600)
    f2.place(x=30,y=180)
    b2=Button(f2,text="Scan your RFID card",bg="white",bd=5,font=("arial",15,),width=30,command=scan)
    b2.place(x=120,y=0)
    e2=Entry(f2,bg="white",state=DISABLED,width=15,bd=5,font=("arial",18,"bold"),show='*')
    e2.place(x=257,y=80)
    #e2.config(status=DISABLED)
    l3=Label(f2,text="Password:",font=("Times New Roman",20),bg="black",fg="white")
    l3.place(x=120,y=80)
    b1=Button(f2,text="LOGIN",font=("Times New Roman",15),bg="white",fg="black",state=DISABLED,command=login)
    b1.place(x=230,y=160)
    root.mainloop()

loginwindow()
