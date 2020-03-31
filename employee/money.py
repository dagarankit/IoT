import tkinter

from tkinter import *

from tkinter import messagebox

import urllib3

import json

import emp1


root=Tk()

root.title("Money")

root.geometry("720x480+700+300")

root.resizable(0,0)

root['bg']='#F8E7BD'

http=urllib3.PoolManager()

f1=Frame(root,height=100,width=200,bg='#766843')

f1.pack(fill=X)
l1=Label(f1,text="Haldiram's",font=("monotype corsiva",30,"italic","underline"),fg='white',bg='#766843')

l1.place(x=245,y=30)


def add(d,st):
    
	a=e1.get()
    
	am=int(d)+int(a)
    
	print(am)
    
	q=http.request('GET',"https://kshamaiot.000webhostapp.com/HALDIRAMS/updatestatusamount.php?RFID="+st+"&Amount="+str(am))
    
	w=q.data.decode("utf-8")
    
	if w=="success":
        
		messagebox.showinfo(title="Done",message="Amount Updated")
    
	else:
        
		messagebox.showerror(title="Error",message="OOPS! Something went wrong.")
    
	emp1.new()

def check():
        
	import serial
        
	ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)
        
	st=""
        
	while(1):
            
		x=list(ser.readall())
            
		print(x)
            
	if(x != []):
                
		var=x
                
	break
        
	for i in var:
            
		st+=str(i)
        
		print(st)
        
		r=http.request('GET',"https://kshamaiot.000webhostapp.com/HALDIRAMS/getstatusamount.php?RFID="+st) #+var
        
		d=r.data.decode("utf-8")
        
		print(d)
        
	add(d,st)
    ###################Code to update table
##    
root.destroy()

##    import emp


f2=Frame(root,height=250,width=450,bg='#F8E7BD')

f2.place(x=135,y=100)

l2=Label(f2,text="Enter the amount: ",font=("monotype corsiva",15),bg='#F8E7BD',fg='#766843')

l2.place(x=20,y=50)

e1=Entry(f2,width=20)

e1.place(x=250,y=54)

b1=Button(f2,text="Scan your card",font=("monotype corsiva",15),command=check)

b1.place(x=140,y=105)
##de=str(check())

##l2=Label(f2,text="Total Amount in your card is"+str(de),bg='#F8E7BD',fg='#766843',font=("monotype corsiva",15))

##l2.place(x=140,y=120)
root.mainloop()
