import tkinter
from tkinter import *
from tkinter import messagebox
import RPi.GPIO as lcd
import pay

order_num=0
global gt
def menu(stri):
    root=Tk()
    root.title("Menu")
    root.geometry("720x480+700+300")
    root.resizable(0,0)
    root['bg']='#F8E7BD'
    f1=Frame(root,height=100,width=200,bg='#766843')
    f1.pack(fill=X)
    l1=Label(f1,text="Haldiram's",font=("monotype corsiva",30,"italic","underline"),fg='white',bg='#766843')
    l1.place(x=245,y=30)
    f2=Frame(root,height=400,width=300,bg='#F8E7BD')
    f2.place(x=10,y=100)
    

    def calc():
        global gt
        a1=e1.get()
        a2=e2.get()
        a3=e3.get()
        a4=e4.get()
        a5=e5.get()
        a6=e6.get()
        a7=e7.get()
        a8=e8.get()
        a9=e9.get()
        a10=e10.get()
        a11=e11.get()
        a12=e12.get()
        a13=e13.get()
        a14=e14.get()
        a15=e15.get()
        a16=e16.get()
        
        if(a1 == ""):
            a1=0
        else:
            a1=int(a1)
        if(a2 == ""):
            a2=0
        else:
            a2=int(a2)
        if(a3 == ""):
            a3=0
        else:
            a3=int(a3)
        if(a4 == ""):
            a4=0
        else:
            a4=int(a4)
        if(a5 == ""):
            a5=0
        else:
            a5=int(a5)
        if(a6 == ""):
            a6=0
        else:
            a6=int(a6)
        if(a7 == ""):
            a7=0
        else:
            a7=int(a7)
        if(a8 == ""):
            a8=0
        else:
            a8=int(a8)
        if(a9 == ""):
            a9=0
        else:
            a9=int(a9)
        if(a10 == ""):
            a10=0
        else:
            a10=int(a10)
        if(a11 == ""):
            a11=0
        else:
            a11=int(a11)
        if(a12 == ""):
            a12=0
        else:
            a12=int(a12)
        if(a13 == ""):
            a13=0
        else:
            a13=int(a13)
        if(a14 == ""):
            a14=0
        else:
            a14=int(a14)
        if(a15 == ""):
            a15=0
        else:
            a15=int(a15)
        if(a16 == ""):
            a16=0
        else:
            a16=int(a16)
        total=(a1*65)+(a2*80)+(a3*90)+(a4*90)+(a5*98)+(a6*115)+(a7*115)+(a8*120)+(a9*130)+(a10*150)+(a11*180)+(a12*200)+(a13*220)+(a14*230)+(a15*250)+(a16*275)
        gst=(0.05)*total
        gt=total+gst
        print(total,gst,gt)
        b3=Button(f3,text="Proceed to Pay",height=1,width=20,font=("monotype corsiva",15),command=order)
        b3.place(x=10,y=330)
        l4.config(text=("total cost: "+str(total)+" "*5+"GST: "+str(gst)),fg='white',bg='#766843')
        l5.config(text=("Grand Total: "+str(gt)),fg='white',bg='#766843')
        global order_num
        order_num+=1
        d={'A':a1,'B':a2,'C':a3,'D':a4,'E':a5,'F':a6,'G':a7,'H':a8,'I':a9,'J':a10,'K':a11,'L':a12,'M':a13,'N':a14,'O':a15,'P':a16}
        return d
        
    def res():
        e1.delete(0,"end")
        e2.delete(0,"end")
        e3.delete(0,"end")
        e4.delete(0,"end")
        e5.delete(0,"end")
        e6.delete(0,"end")
        e7.delete(0,"end")
        e8.delete(0,"end")
        e9.delete(0,"end")
        e10.delete(0,"end")
        e11.delete(0,"end")
        e12.delete(0,"end")
        e13.delete(0,"end")
        e14.delete(0,"end")
        e15.delete(0,"end")
        e16.delete(0,"end")
        l4.config(text="",bg='#F8E7BD')
        l5.config(text="",bg='#F8E7BD')
        b3=Button(f3,text="Proceed to Pay",height=1,width=20,font=("monotype corsiva",15),state=DISABLED)
        b3.place(x=10,y=330)
        
    def order():
        global gt
        print("order number :",order_num)
        print("Your order is:",calc())
        root.destroy()
        pay.pay(gt,stri)
        

    l2=Label(f2,text="Aloo Tikki            65/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=10)
    e1=Entry(f2,width=6)
    e1.place(x=250,y=14)
    l2=Label(f2,text="Matar Kulcha       80/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=40)
    e2=Entry(f2,width=6)
    e2.place(x=250,y=44)
    l2=Label(f2,text="Dahi Bhalla         90/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=70)
    e3=Entry(f2,width=6)
    e3.place(x=250,y=74)
    l2=Label(f2,text="Papdi Chaat        90/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=100)
    e4=Entry(f2,width=6)
    e4.place(x=250,y=104)
    l2=Label(f2,text="Raj Kachori         98/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=130)
    e5=Entry(f2,width=6)
    e5.place(x=250,y=134)
    l2=Label(f2,text="Chole Bhature   115/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=160)
    e6=Entry(f2,width=6)
    e6.place(x=250,y=164)
    l2=Label(f2,text="Pav Bhaji           115/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=190)
    e7=Entry(f2,width=6)
    e7.place(x=250,y=194)
    l2=Label(f2,text="Veg Noodles     120/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=220)
    e8=Entry(f2,width=6)
    e8.place(x=250,y=224)
    l2=Label(f2,text="Fried Rice         130/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=250)
    e9=Entry(f2,width=6)
    e9.place(x=250,y=254)
    l2=Label(f2,text="Chilli Paneer     150/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=280)
    e10=Entry(f2,width=6)
    e10.place(x=250,y=284)
    l2=Label(f2,text="Veg Sandwich  180/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=310)
    e11=Entry(f2,width=6)
    e11.place(x=250,y=314)
    f3=Frame(root,height=400,width=300,bg='#F8E7BD')
    f3.place(x=400,y=100)
    l2=Label(f3,text="Paneer Tikka       200/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=10)
    e12=Entry(f3,width=6)
    e12.place(x=250,y=14)
    l2=Label(f3,text="Pasta                   220/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=40)
    e13=Entry(f3,width=6)
    e13.place(x=250,y=44)
    l2=Label(f3,text="Veg. Thali            230/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=70)
    e14=Entry(f3,width=6)
    e14.place(x=250,y=74)
    l2=Label(f3,text="Tandoori Platter  250/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=100)
    e15=Entry(f3,width=6)
    e15.place(x=250,y=104)
    l2=Label(f3,text="Special Thali       275/-",font=("monotype corsiva",15),fg='#766843',bg='#F8E7BD')
    l2.place(x=10,y=130)
    e16=Entry(f3,width=6)
    e16.place(x=250,y=134)
    b1=Button(f3,text="Place Order",font=("monotype corsiva",10),height=4,width=6,command=calc)
    b1.place(x=40,y=170)
    b1=Button(f3,text="Reset",font=("monotype corsiva",10),height=4,width=6,command=res)
    b1.place(x=170,y=170)
    l4=Label(f3,font=("monotype corsiva",15),bg='#F8E7BD')
    l4.place(x=5,y=250)
    l5=Label(f3,font=("monotype corsiva",15),bg='#F8E7BD')
    l5.place(x=45,y=290)





    root.mainloop()
