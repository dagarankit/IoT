import serial
import RPi.GPIO as GPIO
import time
import mysql.connector as mc
ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)
time.sleep(1)
x='AT'
phone_no=['+917641816981','+918132973620']

def conn():
    db= mc.connect(host="192.168.43.252", database="notice",user= "root",password = "sera") #have to change host as per my IP ; Also have to configure the pi in serial com mode
    cur = db.cursor()
    cmd="select * from physics_class;"
    cur.execute(cmd)
    stri= cur.fetchall()
    notice_str=stri[0][1]
    db.commit()
    cur.close()
    db.close()
    return notice_str

def stri_send(message):
    message=message.encode('UTF-8')
    ser.write(message)

def GSM_send_notice():
# if say any of variable here is undefined
##    ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)
##    time.sleep(1)
##    x='AT'
##    phone_no=('+9176416981','+8132973620')


    
    notice_string=conn()
    j=0
    while (j<2):
        ser.write(x.encode('UTF-8')) #serial communication works in UTF format so when I write data I have to encode it to a UTF format
        stri_send(chr(13)) #ENTER
        time.sleep(0.5)  # ? why delay is needed

        #---------configure in SMS mode-----------------
        stri_send('AT+CMGF=1') # what does it do ? This was for setting to sending mode
        stri_send(chr(13))
        time.sleep(0.5)
        #-----------------------------------------------

        #----------send_message to the number saved in phone_no tuple---------------------
        for i in range(len(phone_no)):
        
            stri_send('AT+CMGS="{}"'.format(phone_no[i])) #how do I send message to multiple numbers ?
            stri_send(chr(13))
            time.sleep(0.5)
            stri_send(notice_string)  # notice_str is in my data_base
            stri_send(chr(13))
            time.sleep(0.5)
            stri_send(chr(26)) #{send_message}
            i=i+1

        j=j+1;
        print("yes")
        time.sleep(5)
        



if __name__=='__main__':
    GSM_send_notice()









    
    
    
