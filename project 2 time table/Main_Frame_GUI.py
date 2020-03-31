import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mc






#notice_string="The admission procedure has been made online \n please visit university website for admission"

import update_time_table_GUI as utt
import show_time_table_GUI as stt
#import send_notice_page as ns
import call_RFID as rf_scan

#This function will return two value user name and password
def update_page():
    cd=Department.get()
    cy=year.get() # the year of the course

    if cd=='Physics'and cy == 'Masters_Degree_year_1' :
        yes_no = messagebox.askquestion("Do you want to Update","Are you Sure?",icon='question')
        if yes_no == 'yes':
            root.destroy()
            utt.call_update()
        else:
            pass
    else:
        messagebox.showinfo("Database unavailable","Sorry Database for this class isn't ready")

def show_tt_page():
    cd=Department.get()
    cy=year.get() # the year of the course

    if cd=='Physics'and cy == 'Masters_Degree_year_1' :
        yes_no = messagebox.askquestion("Do you want to see Time Tabel","Are you Sure ?",icon='question')
        if yes_no == 'yes':
            root.destroy()
            stt.show_time_table()
        else:
            pass
    else:
         messagebox.showinfo("Database unavailable","Sorry Data Base for this class isn't ready")
        

       

def send_notice():
    yes_no = messagebox.askquestion("Do you want to Send Notice","Are you Sure?",icon='question')
    if yes_no == 'yes':
        rf_scan.RFID_GUI()
        #ns.notice_box()
    else:
        pass

    
def update_notice():
    db=mc.connect(host="192.168.43.252",database="notice",user="root",password="sera")
    cur =db.cursor()
    cmd = "select * from physics_class"
    cur.execute(cmd)
    x=cur.fetchall()
    #--------notice_string
    u_notice=x[0][1]
    l=len(u_notice)
    if l > 60 :
        l1=int(l/2)
        u_notice = u_notice[0:l1]+'- \n'+u_notice[l1:l]
    notice.config(text=u_notice)
    notice.update_idletasks()
    #----------------
    print(x[0][1])
    db.commit()
    cur.close()
    db.close()
     
    
    
    
            

def the_main_frame():
    global root
    root = tkinter.Tk()
    root.geometry("1600x1000")
    root['bg']="white"
    f1=Frame(root,bg="blue",height=100,width=500)
    f1.pack(fill=X)
    l1=Label(f1,text="THE GREAT INDIAN INSTITUTE OF SCIENCE AND TECHNOLOGY",font=("TimesNewRoman",25,"bold"),height=3,width=18,bd=2,bg="yellow",fg="red",relief="solid")
    l1.pack(fill=X)


    #f2 is the frame in which the entry option will be there
    f2=Frame(root,bg="skyblue",height=800,width=1100)
    f2.place(x=200,y=120)


    uf=Frame(f2,height=400,width=800,bd=2,bg='SpringGreen',relief='solid')
    uf.place(x=100,y=260)
    #sf=Frame(f2,height=400,width=550,bd=2,bg='SpringGreen',relief='solid')
    #sf.place(x=550,y=260)
    nf=Frame(f2,bg="greenYellow",height=200,width=1100,bd=2,relief='solid')
    nf.place(x=0,y=20)


    #Now the code for the upadate and show frame
    #---------------UPDATE/SHOW FRAME-----------------
    # Create a Tkinter variable
    global Department
    Department = StringVar(f2)
    choice_of_Department = ['ELectrical','ComputerScience','Electronics','Mechanical','Civil','Aerospcae','Biotechnology','Chemistry','Physics','Mathematics','Neurology'] # set the default option
    Department.set('Electronics')
    Department_dropdown = ttk.OptionMenu(uf,Department , *choice_of_Department)
    Label(uf, text="Department:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=70)
    Department_dropdown.place( x=320,y=70)

    # on change dropdown value
    def change_Department(*args):
        print( Department.get() )

    # link function to change dropdown
    Department.trace('w', change_Department)

    # Create a Tkinter variable
    global year
    year = StringVar(f2)
    year.set('')
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option

    choice_of_year = ['Bachelor_Degree_year_1','Bachelor_Degree_year_2','Bachelor_Degree_year_3','BBachelor_Degree_year_4','Masters_Degree_year_1','Masters_Degree_year2','phD'] # set the default option
    year.set('Bachelor_Degree_year_1')
        
    year_dropdown = ttk.OptionMenu(uf,year , *choice_of_year)
    Label(uf, text="year:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=150)
    year_dropdown.place( x=320,y=150)

    #very important code ttk style
    s = ttk.Style()
    s.configure('.', font=('Helvetica', 16),bd=3,relief='raised')

    # on change dropdown value
    def change_year(*args):
        print( year.get() )

    # link function to change dropdown
    year.trace('w', change_year)


    #update buton this will run the function that leads to a new GUI
    uf_button=Button(uf,text="UPDATE",font=("TimesNewRoman",15,"bold"),bd=5,bg="white",fg="black",relief="raised",command = update_page).place(x=180,y=210)


    #for the bove the code for show and update are the same / here is the unnique part for the show time table button
    #show time buton this will run the function that leads to a new GUI
    sf_button=Button(uf,text="SHOW TIME TABLE",font=("TimesNewRoman",15,"bold"),bd=5,bg="white",fg="black",relief="raised",command = show_tt_page).place(x=310,y=210)

    #--------------END OF UPDATE/SHOW FRAME-----------


    #--------------------NOTICE FRAME-----------------
    global notice
    s_n = Label(nf, text="NOTICE",font=("TimesNewRoman",18,"bold"),height=1,width=10,bd=2,bg="cyan",fg="white",relief="solid")
    s_n.place(x=360,y=10)
    notice=Label(nf, text="",font=("TimesNewRoman",18,"bold"),height=4,width=60,bd=2,bg="white",fg="red",relief="solid")
    notice.place(x=10,y=60)

    notice.config(text="The admission procedure has been made online , for \n detail check Institutes web page")
    notice.update_idletasks()


    #Button to show notice on everyone mobile number and the notice label itself
    sf_button=Button(nf,text="SEND NOTICE",font=("TimesNewRoman",15,"bold"),bd=5,bg="white",fg="black",relief="raised",command = send_notice)
    sf_button.place(x=920,y=50)

    un_button=Button(nf,text="UPDATE NOTICE",font=("TimesNewRoman",14,"bold"),bd=5,bg="white",fg="black",relief="raised",command = update_notice)
    un_button.place(x=920,y=100)
    #-------------------------------------------------


    update_notice()
    
    
    root.mainloop()


if __name__ == '__main__':
    the_main_frame()
    
