import tkinter

from tkinter import *

from tkinter import messagebox

import mysql.connector as mc
def 
destroy():
    
   r.destroy()

def displaynote(book1,book2):
    
  db=mc.connect(host="localhost",database="iotlibrary",user="root",password="")
    
  cur= db.cursor()
     
  cmd="UPDATE books SET quantity=quantity-1 WHERE booktitle='"+book1+"' or booktitle='"+book2+"'"
    
  cur.execute(cmd)
    db.commit()
    cur.close()
    db.close()
    l1=Label(f1,text="Note : Please get your books from library by swapping you cards.",font=("arial",15),bg="#424242",fg="red")
    l1.place(x=50,y=160)
    b1=Button(f1,text="Finish",command=destroy)
    b1.place(x=50,y=200)
def proceed(book1,book2):
    global r,f1
    r=tkinter.Tk()
    r.title("Confirm Page")
    r.geometry("720x480")
    r['bg']="#424242"
    f1=Frame(r,height="800",width="800",bg="#424242")
    f1.pack(fill=X)

    l1=Label(f1,text="Your Selected Books",font=("arial",25),bg="#424242",fg="white")
    l1.place(x=50,y=5)
    l1=Label(f1,text="Book1 : "+book1,font=("arial",10),bg="#424242",fg="white")
    l1.place(x=50,y=70)
    l1=Label(f1,text="Book2 : "+book2,font=("arial",10),bg="#424242",fg="white")
    l1.place(x=50,y=100)
    b1=Button(f1,text="continue...",command=lambda: displaynote(book1,book2))
    b1.place(x=50,y=130)

    r.mainloop()

from tkinter import messagebox
import mysql.connector as mc
def destroy():
    r.destroy()
def displaynote(book1,book2):
    db=mc.connect(host="localhost",database="lib_mgmt",user="deepak",password="deepak!@#")
    cur= db.cursor()
    cmd="UPDATE books SET quantity=quantity-1 WHERE booktitle='"+book1+"' or booktitle='"+book2+"'"
    cur.execute(cmd)
    db.commit()
    cur.close()
    db.close()
    l1=Label(f1,text="Note : Please get your books from library by swapping you cards.",font=("arial",15),bg="#424242",fg="red")
    l1.place(x=50,y=160)
    b1=Button(f1,text="Finish",command=destroy)
    b1.place(x=50,y=200)
def proceed(book1,book2):
    global r,f1
    r=tkinter.Tk()
    r.title("Confirm Page")
    r.geometry("720x480")
    r['bg']="#424242"
    f1=Frame(r,height="800",width="800",bg="#424242")
    f1.pack(fill=X)

    l1=Label(f1,text="Your Selected Books",font=("arial",25),bg="#424242",fg="white")
    l1.place(x=50,y=5)
    l1=Label(f1,text="Book1 : "+book1,font=("arial",10),bg="#424242",fg="white")
    l1.place(x=50,y=70)
    l1=Label(f1,text="Book2 : "+book2,font=("arial",10),bg="#424242",fg="white")
    l1.place(x=50,y=100)
    b1=Button(f1,text="continue...",command=lambda: displaynote(book1,book2))
    b1.place(x=50,y=130)

    r.mainloop()


