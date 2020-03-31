import tkinter
from tkinter import *
from tkinter import messagebox


import mysql.connector as mc
import Main_Frame_GUI as mf


def go_back():
    yes_no = messagebox.askquestion("GO BACK","Are you sure you want to go to Main Window?",icon='question')

    if yes_no == 'yes':
        root.destroy()
        mf.the_main_frame()

def updation():
    lstatus.configure(text="")
    dy=day.get() # day of the week
    t_tempo=time1.get()
    tim=int(t_tempo[0]) #time
    cc=course_code1.get()
    ct=class_type.get()
    course_cod = cc[0:6]+'('+ct[0]+')' #the course_code with class type
    lc=lecturer.get()
    fac = lc[0:3] # lecturer
    cr=class_room.get() #class room
    result = messagebox.askquestion("Update", "Are You Sure?", icon='question')
    if result == 'yes':
        update_data(dy,course_cod,fac,cr,tim)
    else:
        pass
    

    
    
    
# used for development
##def show_data():
##    cur = db.cursor()
##    cmd = "select * from Monday"
##    cur.execute(cmd)
##    x=cur.fetchall()
##    print(x)
##    db.commit()
##    cur.close()

def update_data(day,course_code,faculty,room_no,tim):
    db=mc.connect(host="192.168.43.252",database="physics_masters_year1",user="root",password="sera")
    cur =db.cursor()
    if course_code[0:2]=='--':
        cmd = "UPDATE {} SET course_code = '--' , faculty = '' , room_no = '' WHERE time = {}".format(day,tim)

    else:
        cmd = "UPDATE {} SET course_code = '{}' , faculty = '{}' , room_no = '{}' WHERE time = {}".format(day,course_code,faculty,room_no,tim)
    print(cmd)
    lstatus.configure(text="SUCESSFULLY UPDATED") # update status
    cur.execute(cmd)
    db.commit()
    cur.close()
    db.close()
    
def call_update():
    global root
    root = tkinter.Tk()
    root.geometry("1600x1000")
    root['bg']="white"
    
    f1=Frame(root,bg="blue",height=100,width=500)
    f1.pack(fill=X)
    l1=Label(f1,text="UPDATION OF PHYSICS MASTERS TIME TABLE",font=("TimesNewRoman",25,"bold"),height=3,width=18,bd=2,bg="yellow",fg="red",relief="solid")
    l1.pack(fill=X)


    #f2 is the frame in which the entry option will be there
    f2=Frame(root,bg="skyblue",height=800,width=600)
    f2.place(x=450,y=120)


    #-------------------------------HERE IS THE DAY DROPDOWN OR COMBOBOX-------
    # Create a Tkinter variable
    global day
    day = StringVar(f2)
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option
    choices_of_day = ['Monday','Tuesday','Wednusday','Thursday','Friday']
    day.set('Monday') # set the default option

    day_drop_down = OptionMenu(f2, day, *choices_of_day)
    Label(f2, text="Day:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=50)
    day_drop_down.place( x=310,y=50)

    # on change dropdown value
    def choose_day(*args):
        print( day.get() )

    # link function to change dropdown
    day.trace('w', choose_day)
    #------------------------------END OF DAY DROPDOWN-----------------------------



    #--------------------------------HERE IS THE TIME DROPDOWN OR COMBOBOX----------
    # Create a Tkinter variable
    global time1
    time1 = StringVar(f2)
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option
    choices_of_time = ['8.00-9.00','9.00-10.00','10.00-11.00','11.00-12.00','12.00-13.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00']
    time1.set('8.00-9.00') # set the default option

    time_drop_down = OptionMenu(f2, time1, *choices_of_time)
    Label(f2, text="Time:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=100)
    time_drop_down.place( x=310,y=100)

    # on change dropdown value
    def choose_time(*args):
        print( time1.get() )

    # link function to change dropdown
    time1.trace('w', choose_time)
    #----------------------------END OF THE TIME DROP DOWN---------------------




    #----------------------------------HERE IS THE COURSE_CODE DROPDOWN-------------------------
    # Create a Tkinter variable
    global course_code1
    course_code1 = StringVar(f2)
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option
    choice_of_course_code = ['-- (No class)','PH7101 (ClasicalMechanics)','PH7102 (MathematicalPhysics)','PH7103 (ComputationalPhysics&Programming)','PH7104 QuantumMechanics-I','PH7151 (GeneralPhysicsLaboratory-I)','PH7152 (ComputerLaboratory)']
    course_code1.set('PH7101 (ClasicalMechanics)') # set the default option

    course_dropdown = OptionMenu(f2,course_code1 , *choice_of_course_code)
    Label(f2, text="Course Code:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=150)
    course_dropdown.place( x=310,y=150)

    # on change dropdown value
    def change_course(*args):
        print( course_code1.get() )

    # link function to change dropdown
    course_code1.trace('w', change_course)
    #----------------------------------END OF THE COURSE_CODE DROPDOWN-------------------


    #---------------------------------HERE IS CLASS_TYPE DROPDOWN--------------------------------------
    # Create a Tkinter variable
    global class_type
    class_type = StringVar(f2)
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option
    choice_of_class_type = ['-','T (Tutorial)','P (Practical)','L (Lecture)']
    class_type.set('L (Lecture)') # set the default option

    class_type_dropdown = OptionMenu(f2,class_type, *choice_of_class_type)
    Label(f2, text="Class Type:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=200)
    class_type_dropdown.place( x=310,y=200)

    # on change dropdown value
    def change_class_type(*args):
        print( class_type.get() )

    # link function to change dropdown
    class_type.trace('w', change_class_type)
    #---------------------------------END OF CLASS_TYPE DROPDOWN-----------------------------------


    #----------------------------------HERE IS THE LECTURERS DROPDOWN-------------------------------------
    # Create a Tkinter variable
    global lecturer
    lecturer = StringVar(f2)
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option
    choice_of_lecturer = ['-','TK (Dr.TADO KARLO)','PRA (Dr.Parameswara Rao Alapati)','MSG (Dr.Manan Sengupta)','ARP (Dr.Arvid Pandey)','TGD (Dr.TH.Gomti Devi)','KSR (Dr.Kamal Saharia)','SDM (Dr.Sanoujam Dhiren Meetei)','KB (Dr.Kunal Borah)','AJ (Dr. Akbari Jahan)','RKY (Dr.Rajesh Kumar Yadav)','MU (Dr.Mukesh Upadhyay)']
    lecturer.set('SDM (Dr.Sanoujam Dhiren Meetei)') # set the default option

    lecturer_dropdown = OptionMenu(f2,lecturer, *choice_of_lecturer)
    Label(f2, text="Lecturer:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=250)
    lecturer_dropdown.place( x=310,y=250)

    # on change dropdown value
    def change_lecturer(*args):
        print( lecturer.get() )

    # link function to change dropdown
    lecturer.trace('w', change_lecturer)

    #----------------------------------END OF LECTURER DROPDOWN-----------------------------------------


    #---------------------------------HERE IS THE CLASS_ROOM DROPDOWN-------------------
    # Create a Tkinter variable
    global class_room
    class_room = StringVar(f2)
    ##choices = { 'B.Sc_Physics_year1','B.Sc_Physics_year2','B.Sc_Physics_year3','M.Sc_Physics_year1','M.Sc_Physics_year2'}
    ##tkvar.set('B.Sc_Physics_year1') # set the default option
    choice_of_class_room = ['-','R-01','L3','L5']
    class_room.set('R-01') # set the default option

    class_room_dropdown = OptionMenu(f2,class_room, *choice_of_class_room)
    Label(f2, text="Class Room:",font=("TimesNewRoman",18,"bold"),height=1,width=13,bd=2,bg="white",fg="red",relief="solid").place(x=100, y=300)
    class_room_dropdown.place( x=310,y=300)

    # on change dropdown value
    def change_class_room(*args):
        print( class_room.get() )

    # link function to change dropdown
    class_room.trace('w', change_class_room)

    #---------------------------------END OF CLASSROOM DROPDOWN------------------



    #SUBMIT BUTTON
    u_button=Button(f2,text="UPDATE",font=("TimesNewRoman",18,"bold"),bd=5,bg="white",fg="black",relief="raised",command = updation).place(x=200,y=380)

    global lstatus
    lstatus = Label(f2, text="",font=("TimesNewRoman",18,"bold"),bd=2,bg="white",fg="red",relief="solid")
    lstatus.place(x=150, y=450)


    #Back Button
    back_button=Button(root,text="GO BACK",font=("TimesNewRoman",14,"bold"),bd=3,bg="white",fg="black",relief="raised",command = go_back)
    back_button.place(x=1400,y=15)

    root.mainloop()





#Now I will make drop down menu for choosing the options and have to learn how to get data from it.
if __name__ == '__main__':
    call_update()









