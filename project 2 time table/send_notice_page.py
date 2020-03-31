#In here I will provide a page in which will come a window to write the notice and submit it and print things on LCD
#python py file to exe file
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mc
import time
#remove the # below to work on Pi
import gsm_function_module as gsm

import lcd_model as lm

# ? what is ttk
#ttk.button menu.confige(font=('Impact', 30))
def notice_sender():
    time.sleep(1)
    lstatus.configure(text="")
    yes_no = messagebox.askquestion("Do you want to Send Notice","Are you Sure?",icon='question')
    if yes_no == 'yes':
        
        data_str=entry_box.get()
        print(data_str)
        update_notice()
        send_notice_SMS()
        lm.display_LCD()
        lcdstatus.configure(text="SENT TO LCD")

#192.168.43.252
        
def update_notice():
    db=mc.connect(host="192.168.43.252",database="notice",user="root",password="sera")
    cur =db.cursor()
    cmd = "UPDATE physics_class SET p_notice = '{}' WHERE id = 1".format(entry_box.get())
    cur.execute(cmd)
    db.commit()
    cur.close()
    db.close()
    lstatus.configure(text="SUCESSFULLY SENT")

def display_on_LCD():
    lm.display_LCD()
    

def send_notice_SMS(): # Through GSM
    gsm.GSM_send_notice()


def notice_box():
    global root2
    root2 = tkinter.Tk()
    root2.geometry("800x400+800+400")
    root2.minsize(width=0,height=0)
    root2.maxsize(width=600,height=300)
    root2['bg']="grey"

    f1=Frame(root2,bg="SpringGreen",height=80,width=500)
    f1.pack(fill=X)
    l1=Label(f1,text="WRITE THE NOTICE HERE",font=("TimesNewRoman",18,"bold"),\
             height=2,width=25,bd=2,bg="lightblue",fg="red",relief="solid")
    l1.place(x=80,y=0)

    #f2 is the frame in which the entry option will be there
    notice_box=Frame(root2,bg="skyblue",bd=1,relief='solid',height=210,width=550)
    notice_box.place(x=20,y=80)



    #Entry_box_where you will write the code
    global entry_box
    entry_box = Entry(notice_box,font=("TimesNewRoman",15),bd=2,width=48,relief='sunken') #textvariable=v
    entry_box.place(x=10, y = 40)
    entry_box.insert(1,"Enter text here")

    #submit Button
    nc_button=Button(notice_box,text="SEND NOTICE",font=("TimesNewRoman",15,"bold"),bd=3,bg="white",fg="black",relief="raised",command = notice_sender)
    nc_button.place(x=50,y=100)
    

    #status_successful_or_unsuccesful tag
    global lstatus
    lstatus = Label(notice_box, text="",font=("TimesNewRoman",15,"bold"),bd=2,bg="white",fg="red",relief="solid")
    lstatus.place(x=255, y=100)

    #lcd_button=Button(notice_box,text="DISPLAY ON LCD",font=("TimesNewRoman",15,"bold"),bd=3,bg="white",fg="black",relief="raised",command = display_on_LCD)
    #lcd_button.place(x=50,y=160)
    global lcdstatus

    lcdstatus = Label(notice_box, text="",font=("TimesNewRoman",15,"bold"),bd=2,bg="white",fg="red",relief="solid")
    lcdstatus.place(x=255, y=150)

    root2.mainloop()

if __name__ == '__main__':
    notice_box()














