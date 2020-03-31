import RPi.GPIO as GPIO
import time

import mysql.connector as mc




def str_generator():
    db=mc.connect(host="192.168.43.252",database="notice",user="root",password="sera")
    cur = db.cursor()
    cmd="select * from physics_class;"
    cur.execute(cmd)
    x= cur.fetchall()
    u_notice=x[0][1]
    print(u_notice)
    db.commit()
    cur.close()
    db.close()
    return u_notice




def ini():
    lcdcmd(0x33) # Sets initially to 8 bit mode
    lcdcmd(0x32) # sets to the 4 bit mode , what i don't get is why 3 infront is used
    lcdcmd(0x01) #clear display screen
    lcdcmd(0x28) #function for 2-line display
    lcdcmd(0x80) #Cursor begining of first row
    lcdcmd(0x0e) #display on cursor on
    lcdcmd(0x06) #entry mode

def lcdcmd(value):
    GPIO.output(rs,False)
    
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x10==0x10:
        GPIO.output(d0,True)
    if value&0x20==0x20:
        GPIO.output(d1,True)
    if value&0x40==0x40:
        GPIO.output(d2,True)
    if value&0x80==0x80:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)

    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x01==0x01:
        GPIO.output(d0,True)
    if value&0x02==0x02:
        GPIO.output(d1,True)
    if value&0x04==0x04:
        GPIO.output(d2,True)
    if value&0x08==0x08:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)
    
def lcddata(value):
    GPIO.output(rs,True)
    
    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x10==0x10:
        GPIO.output(d0,True)
    if value&0x20==0x20:
        GPIO.output(d1,True)
    if value&0x40==0x40:
        GPIO.output(d2,True)
    if value&0x80==0x80:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)

    GPIO.output(d0,False)
    GPIO.output(d1,False)
    GPIO.output(d2,False)
    GPIO.output(d3,False)
    
    if value&0x01==0x01:
        GPIO.output(d0,True)
    if value&0x02==0x02:
        GPIO.output(d1,True)
    if value&0x04==0x04:
        GPIO.output(d2,True)
    if value&0x08==0x08:
        GPIO.output(d3,True)

    GPIO.output(en,True)
    time.sleep(0.001)
    GPIO.output(en,False)
    time.sleep(0.001)

def stri(message):
    
    for i in range (len(message)):
        
        lcddata(ord(message[i]))

def display_LCD():
    # definition
    global rs,en,d0,d1,d2,d3
    rs= 7 # py 26
    en =8 # py 24
    d0=25 # py 22
    d1=24 # py 18
    d2=23 # py 16
    d3=18 # py 12
    s_notice=str_generator()
    s_notice1=''
    s_notice2=''
    l=len(s_notice)
    if l>16 and l <= 32:
        l1=int(l/2)
        s_notice1=s_notice[0:l1]
        s_notice2=s_notice[l1:l]
    elif l>32:
        s_notice='Notice string too large'
    else:
        pass
    
    try :

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rs,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)
        GPIO.setup(d0,GPIO.OUT)
        GPIO.setup(d1,GPIO.OUT)
        GPIO.setup(d2,GPIO.OUT)
        GPIO.setup(d3,GPIO.OUT)
        ini() #This initializes the LC
    
        lcdcmd(0x01) # Clear Screen
        lcdcmd(0x80) #cursor to the first row
        if(l>16 and l<32):
            stri(s_notice1)
            time.sleep(2)
            lcdcmd(0xc0) #cursor to the second row
            stri(s_notice2)
            time.sleep(2)
            print("hello")
        else:
            stri(s_notice)
            print(s_notice)
        
    except KeyboardInterrupt:
        pass

if __name__=='__main__':
    display_LCD()
    
    
