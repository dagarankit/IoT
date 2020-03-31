from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tki
import time



import RFID_modfun as rf
import send_notice_page as ns

def scan_card():
    time.sleep(1)
    lstatus.configure(text="Scanning")
    a=rf.Validate_card()
    print(a)

    if a=='yes':
        lstatus.configure(text="Verified")
        time.sleep(1)
        r_root.destroy()
        ns.notice_box()
        
    if a=='no':
        lstatus.configure(text="Cannot Verify")
            
        
        
                          
        

def RFID_GUI():
    global r_root
    r_root = tki.Tk()
    r_root.geometry("600x300+800+400")
    #(width=600,height=300)
    r_root.minsize(width=0,height=0)
    r_root.maxsize(width=600,height=300)
    r_root['bg']='lavender'
    f1=Frame(r_root,bg='SpringGreen',height=80,width=500)
    f1.pack(fill=X)
    l1=Label(f1,text="VERIFIFICATION NEEDED TO SEND NOTICE",font=("TimesNewRoman",18,"bold"),\
             height=2,width=48,bd=2,bg="lightblue",fg="red",relief="solid")
    l1.place(x=10,y=0)

    scan_f=Frame(r_root,bg="skyblue",bd=1,relief='solid',height=180,width=400)
    scan_f.place(x=20,y=80)

    #scan Button
    nc_button=Button(scan_f,text="SCAN",font=("TimesNewRoman",15,"bold"),bd=3,bg="white",fg="black",relief="raised",command = scan_card)
    nc_button.place(x=50,y=60)

        #status_successful_or_unsuccesful tag
    global lstatus
    lstatus = Label(scan_f, text="Press scan",font=("TimesNewRoman",20,"bold"),bd=2,bg="white",fg="red",relief="solid")
    lstatus.place(x=200, y=60)

    r_root.mainloop()


if __name__ == '__main__':
    RFID_GUI()
    

    
    
