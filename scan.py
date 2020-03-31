import tkinter
from tkinter import *
from tkinter import messagebox
import mysql.connector as mc
#import serial
#import RPi.GPIO as RFID
import Login_Page
def sc():



    root=tkinter.Tk()
    root.title("RFID Scan")

    f1=Frame(root, height="500", width="500", bg="#424242")
    f1.pack(side="top")

    l1 = Label(f1, text="Scan Your RF-Card", font=("ubuntu", 20), bg="#424242", fg="white")
    l1.place(x=50,y=200)


    #
    # ser = serial.Serial(port='/dev/ttyS0', baudrate=9600, parity=serial.PARITY_NONE, timeout=1)
    #
    # while (1):
    #     global data
    #     x = list(ser.readall())
    #     print(x)
    #     if (x != data):
    #         data = x
    #         if (len(data) > 1):
    #             db = mc.connect(host="localhost", user="deepak", password="deepak!@#", database="lib_mgmt")
    #             cur = db.cursor()
    #             cmd = "insert into students(RFID) values('" + data + "');"
    #             cur.execute(cmd)
    #             db.commit()
    #             cur.close()
    #             db.close()

    messagebox.showinfo(title="Success", message="Scanned Successfully")

    root.destroy()
    Login_Page.log()

    root.mainloop()