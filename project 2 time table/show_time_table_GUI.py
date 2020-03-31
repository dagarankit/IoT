import tkinter
from tkinter import *
from tkinter import messagebox

from tkinter import ttk




import mysql.connector as mc
import Main_Frame_GUI as mf



""" Reference for the show the tables contents
cur = db.cursor()
cmd = "select * from Monday"
cur.execute(cmd)
x=cur.fetchall()
print(x)
"""

##header = ('TT').center(3,'_')+'|'+('{}'.format("8:00-9:00")).center(20,'_')+' |'+('{}'.format("9:00-10:00")).center(20,'_')+' |' +('{}'.format("10:00-11:00")).center(20,'_')+' |' + \
##         ('{}'.format("11:00-12:00")).center(20,'_')+' |'+('{}'.format("13:00-14:00")).center(20,'_')+' |'+ ('{}'.format("14:00-15:00")).center(20,'_')+' |'+\
##         ('{}'.format("15:00-16:00")).center(20,'_')+' |'+('{}'.format("16:00-17:00")).center(20,'_')+' |'

##Monday = ''
##Tuesday = ''
##Wednusday = ''
##Thursday = ''
##Friday = ''
#time_table = ''


def string_generator(day):
    db=mc.connect(host="192.168.43.252",database="physics_masters_year1",user="root",password="sera")
    cur = db.cursor()
    cmd = "select * from {}".format(day)
    cur.execute(cmd)
    x=cur.fetchall()
    db.commit()
    cur.close()
    db.close()
    string_day=list(range(len(x)))
    

    for i in range(len(x)):
        string_day[i] =  ("{} {} {}" .format(x[i][1],x[i][2],x[i][3])).center(19)

    return string_day

def go_back():
    yes_no = messagebox.askquestion("GO BACK","Are you sure you want to go to Main Window?",icon='question')

    if yes_no == 'yes':
        root.destroy()
        mf.the_main_frame()
        


#time_table = header+'\n'+'MON|' + Monday + '\n' + 'TUE|' + Tuesday + '\n' + 'WED|' + Wednusday + '\n' + 'THU|' + Thursday + '\n' + 'FRI|' + Friday  y)
##print(Wednusday)
##print(Thursday)
##print(Friday)



def show_time_table():
            

    time = ['8.00-9.00','9.00-10.00','10.00-11.00','11.00-12.00','12.00-13.00','13.00-14.00','14.00-15.00','15.00-16.00','16.00-17.00']
    Monday = string_generator('Monday')
    Tuesday = string_generator('Tuesday')
    Wednusday = string_generator('Wednusday')
    Thursday = string_generator('Thursday')
    Friday = string_generator('Friday')
    global root;
    root = tkinter.Tk()
    root.geometry("1600x1000")
    root['bg']="skyblue"
    f1=Frame(root,bg="navyblue",height=100,width=100)
    f1.pack(fill=X)
    l1=Label(f1,text="PHYSICS MASTERS FIRST YEAR TIME TABLE",font=("arial",40),bg="SpringGreen",fg="white",bd=2,relief='solid')
    l1.pack()
    f2=Frame(root,bg="skyblue",height=500,width=1400)
    f2.place(x=50,y=100)


    #Time of the day
    lt=Label(f2,text="Time",font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt.place(x=50,y=35)


    lt2=Label(f2,text=time[0],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt2.place(x=181,y=35)

    lt3=Label(f2,text=time[1],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt3.place(x=312,y=35)

    lt4=Label(f2,text=time[2],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt4.place(x=443,y=35)

    lt5=Label(f2,text=time[3],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt5.place(x=574,y=35)

    lt6=Label(f2,text=time[4],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt6.place(x=705,y=35)

    lt7=Label(f2,text=time[5],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt7.place(x=836,y=35)

    lt8=Label(f2,text=time[6],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt8.place(x=967,y=35)

    lt9=Label(f2,text=time[7],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt9.place(x=1098,y=35)

    lt10=Label(f2,text=time[8],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="SpringGreen",fg="blue") # use relief
    lt10.place(x=1229,y=35)


    ##Label for Monday

    l11=Label(f2,text="MON",font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="silver",fg="black") # use relief
    l11.place(x=50,y=100)


    l2=Label(f2,text=Monday[0],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l2.place(x=181,y=100)

    l3=Label(f2,text=Monday[1],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l3.place(x=312,y=100)

    l4=Label(f2,text=Monday[2],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l4.place(x=443,y=100)

    l5=Label(f2,text=Monday[3],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l5.place(x=574,y=100)

    l6=Label(f2,text=Monday[4],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l6.place(x=705,y=100)

    l7=Label(f2,text=Monday[5],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l7.place(x=836,y=100)

    l8=Label(f2,text=Monday[6],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l8.place(x=967,y=100)

    l9=Label(f2,text=Monday[7],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l9.place(x=1098,y=100)

    l10=Label(f2,text=Monday[8],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l10.place(x=1229,y=100)

    #Label for Tuesday

    l11=Label(f2,text="TUE",font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="white",fg="black") # use relief
    l11.place(x=50,y=165)

    l2=Label(f2,text=Tuesday[0],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l2.place(x=181,y=165)

    l3=Label(f2,text=Tuesday[1],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l3.place(x=312,y=165)

    l4=Label(f2,text=Tuesday[2],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l4.place(x=443,y=165)

    l5=Label(f2,text=Tuesday[3],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l5.place(x=574,y=165)

    l6=Label(f2,text=Tuesday[4],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l6.place(x=705,y=165)

    l7=Label(f2,text=Tuesday[5],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l7.place(x=836,y=165)

    l8=Label(f2,text=Tuesday[6],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l8.place(x=967,y=165)

    l9=Label(f2,text=Tuesday[7],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l9.place(x=1098,y=165)

    l10=Label(f2,text=Tuesday[8],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l10.place(x=1229,y=165)

    ##LABEL FOR WEDNUSDAY

    l11=Label(f2,text="WED",font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="grey",fg="black") # use relief
    l11.place(x=50,y=230)

    l2=Label(f2,text=Wednusday[0],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l2.place(x=181,y=230)

    l3=Label(f2,text=Wednusday[1],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l3.place(x=312,y=230)

    l4=Label(f2,text=Wednusday[2],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l4.place(x=443,y=230)

    l5=Label(f2,text=Wednusday[3],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l5.place(x=574,y=230)

    l6=Label(f2,text=Wednusday[4],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l6.place(x=705,y=230)

    l7=Label(f2,text=Wednusday[5],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l7.place(x=836,y=230)

    l8=Label(f2,text=Wednusday[6],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l8.place(x=967,y=230)

    l9=Label(f2,text=Wednusday[7],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l9.place(x=1098,y=230)

    l10=Label(f2,text=Wednusday[8],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l10.place(x=1229,y=230)


    #Label for Thursday

    l11=Label(f2,text="THU",font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="white",fg="black") # use relief
    l11.place(x=50,y=295)

    l2=Label(f2,text=Tuesday[0],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l2.place(x=181,y=295)

    l3=Label(f2,text=Tuesday[1],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l3.place(x=312,y=295)

    l4=Label(f2,text=Tuesday[2],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l4.place(x=443,y=295)

    l5=Label(f2,text=Tuesday[3],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l5.place(x=574,y=295)

    l6=Label(f2,text=Tuesday[4],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l6.place(x=705,y=295)

    l7=Label(f2,text=Tuesday[5],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l7.place(x=836,y=295)

    l8=Label(f2,text=Tuesday[6],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l8.place(x=967,y=295)

    l9=Label(f2,text=Tuesday[7],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l9.place(x=1098,y=295)

    l10=Label(f2,text=Tuesday[8],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l10.place(x=1229,y=295)

    ##LABEL FOR FRIDAY lavender aquamarine

    l11=Label(f2,text="FRI",font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="grey",fg="black") # use relief
    l11.place(x=50,y=360)

    l2=Label(f2,text=Wednusday[0],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l2.place(x=181,y=360)

    l3=Label(f2,text=Wednusday[1],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l3.place(x=312,y=360)

    l4=Label(f2,text=Wednusday[2],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l4.place(x=443,y=360)

    l5=Label(f2,text=Wednusday[3],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l5.place(x=574,y=360)

    l6=Label(f2,text=Wednusday[4],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l6.place(x=705,y=360)

    l7=Label(f2,text=Wednusday[5],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l7.place(x=836,y=360)

    l8=Label(f2,text=Wednusday[6],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l8.place(x=967,y=360)

    l9=Label(f2,text=Wednusday[7],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="aquamarine",fg="blue") # use relief
    l9.place(x=1098,y=360)

    l10=Label(f2,text=Wednusday[8],font=("TimesNewRoman",8),height=3,width=18,bd=10,bg="lavender",fg="blue") # use relief
    l10.place(x=1229,y=360)



    back_button=Button(root,text="GO BACK",font=("TimesNewRoman",14,"bold"),bd=3,bg="white",fg="black",relief="raised",command = go_back)
    back_button.place(x=1400,y=15)



    ##l3=Label(f2,text=Monday,font=("TimesNewRoman",12),bg="red",fg="blue")
    ##l3.place(x=50,y=150)
    ##l4=Label(f2,text=Tuesday,font=("TimesNewRoman",12),bg="red",fg="blue")
    ##l4.place(x=50,y=200)



    root.mainloop()

if __name__ == '__main__':
    show_time_table()

