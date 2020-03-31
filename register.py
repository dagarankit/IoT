import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
import random
import scan
# import serial
# import RPi.GPIO as GPIO
import time
def reg():



    def submit():

        global O
        O = e8.get()
        print(O, type(O), OT, type(OT))

        if int(OT) == int(O):
            db = mc.connect(host="localhost", user="deepak", password="deepak!@#", database="lib_mgmt")
            cur = db.cursor()
            cmd = "insert into students(name,login_id,branch,mob,email,pass) values('" + name + "','" + login_id + "','" + branch + "','" + mob + "','" + email + "','" + passw + "');"
            cur.execute(cmd)
            db.commit()
            cur.close()
            db.close()
            root.destroy()
            scan.sc()

        else:
            messagebox.showinfo(title="ERROR", message="OTP not match")

    def proceed():
        global login_id,passw,re,name,branch,mob,email
        login_id=e1.get()
        passw=e2.get()
        re=e3.get()
        name=e4.get()
        branch=e5.get()
        mob=e6.get()
        email=e7.get()

        if login_id=="" or passw=="" or name=="" or branch=="" or mob=="":
            messagebox.showerror(title="ERROR",message="Any Mandatory(*) field is blank")

        elif passw==re:
            global OT

            OT=random.randint(1000,9999)

            global OTP

            def OTP():

                return

                ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, timeout=1)
                time.sleep(1)
                x = 'AT'

                def stri_send(message):
                    message = message.encode('UTF-8')
                    ser.write(message)

                ser.write(x.encode('UTF-8'))
                stri_send(chr(13))
                time.sleep(0.5)
                stri_send('AT+CMGF=1')
                stri_send(chr(13))
                time.sleep(0.5)
                stri_send('AT+CMGS="+91%i"'%mob)
                stri_send(chr(13))
                time.sleep(0.5)
                stri_send('%i'%OT)
                stri_send(chr(13))
                time.sleep(0.5)
                stri_send(chr(26))
                print("Sent")
                time.sleep(5)

            OTP()

            print(OT)

            messagebox.showinfo(title="Alert", message="An OTP sent to your mobile")

            l9 = Label(f1, text="OTP", font=("ubuntu", 20), bg="#424242", fg="white")
            l9.place(x=500, y=600)
            global e8
            e8 = Entry(f1, bg="white", bd=1, width=10, font=("URW gothic L", 15, "bold"))
            e8.place(x=620, y=600)
            b2 = Button(f1, text="Submit", font=("ubuntu", 20), command=submit)
            b2.place(x=500, y=650)
            b2 = Button(f1, text="Resend", font=("ubuntu", 20), command=OTP)
            b2.place(x=640, y=650)

        else:
            messagebox.showinfo(title="ERROR", message="Password not match")

    root=tkinter.Tk()
    root.title("Registration")
    #root.geometry("1366*768")

    root["bg"]="#424242"

    f1=Frame(root,height="700",width="1300",bg="#424242")
    f1.pack(side="top")

    l1=Label(f1,text="REGISTRATION PORTAL",font=("ubuntu",20),bg="#424242",fg="white")
    l1.place(x=500,y=50)
    l2=Label(f1,text="User ID*",font=("ubuntu",20),bg="#424242",fg="white")
    l2.place(x=350,y=150)
    l3=Label(f1,text="New Password*",font=("ubuntu",20),bg="#424242",fg="white")
    l3.place(x=350,y=200)
    l4=Label(f1,text="Re-Enter*",font=("ubuntu",20),bg="#424242",fg="white")
    l4.place(x=350,y=250)
    l5=Label(f1,text="Full Name*",font=("ubuntu",20),bg="#424242",fg="white")
    l5.place(x=350,y=300)
    l6=Label(f1,text="Branch*",font=("ubuntu",20),bg="#424242",fg="white")
    l6.place(x=350,y=350)
    l7=Label(f1,text="Mobile No.*",font=("ubuntu",20),bg="#424242",fg="white")
    l7.place(x=350,y=400)
    l8=Label(f1,text="Email ID",font=("ubuntu",20),bg="#424242",fg="white")
    l8.place(x=350,y=450)

    e1 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"))
    e1.place(x=600, y=150)
    e2 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"), show="*")
    e2.place(x=600, y=200)
    e3 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"), show="*")
    e3.place(x=600, y=250)
    e4 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"))
    e4.place(x=600, y=300)
    e5 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"))
    e5.place(x=600, y=350)
    e6 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"))
    e6.place(x=600, y=400)
    e7 = Entry(f1, bg="gray", bd=1, width=30, font=("URW gothic L", 15, "bold"))
    e7.place(x=600, y=450)

    b1 = Button(f1, text="Proceed", font=("ubuntu", 20),command=proceed)
    b1.place(x=650, y=510)
    #b2 = Button(f1, text=" Login ", font=("ubuntu", 20))
    #b2.place(x=700, y=490)

    root.mainloop()