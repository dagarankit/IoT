import urllib3
import tkinter
from tkinter import *
from tkinter import messagebox
#import RPi.GPIO as lcd
import math
#import logiin


def pay(bill, st):
    http = urllib3.PoolManager()

    def verify():
        print(st)
        r = http.request('GET', "https://kshamaiot.000webhostapp.com/HALDIRAMS/getstatusamount.php?RFID=" + st)  # +var
        d = r.data.decode("utf-8")
        print(d)
        if (int(d) >= math.ceil(bill)):
            print("OK")
            sub(d)
        else:
            print("sorry")
            messagebox.showerror(title="Error", message="Insufficient Amount")

    def sub(d):
        am = int(d) - math.ceil(bill)

        q = http.request('GET',
                         "https://kshamaiot.000webhostapp.com/HALDIRAMS/updatestatusamount.php?RFID=" + st + "&Amount=" + str(
                             am))
        w = q.data.decode("utf-8")
        if w == "success":
            messagebox.showinfo(title="Done", message="Bill paid\nCurrent Balance:" + str(am) + "\nThanks For Visiting")
            root.destroy()
        else:
            messagebox.showerror(title="Error", message="OOPS! Something went wrong.")
        logiin.popo()

    root = Tk()
    root.title("Menu")
    root.geometry("720x480+700+300")
    root.resizable(0, 0)
    root['bg'] = '#F8E7BD'
    f1 = Frame(root, height=100, width=200, bg='#766843')
    f1.pack(fill=X)
    l1 = Label(f1, text="Haldiram's", font=("monotype corsiva", 30, "italic", "underline"), fg='white', bg='#766843')
    l1.place(x=245, y=30)
    f2 = Frame(root, height=300, width=400, bg='#F8E7BD')
    f2.place(x=150, y=150)
    b3 = Button(f2, text="Pay your bill", height=1, width=16, font=("monotype corsiva", 15), command=verify)
    b3.place(x=80, y=105)

    root.mainloop()


