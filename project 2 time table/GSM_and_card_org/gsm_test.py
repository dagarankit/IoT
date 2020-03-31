import serial
import RPi.GPIO as GPIO
import time

ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)
time.sleep(1)
x='AT'

def stri_send(message):
    message=message.encode('UTF-8')
    ser.write(message)
i=0
while (i<2):
    ser.write(x.encode('UTF-8'))
    stri_send(chr(13))
    time.sleep(0.5)
    stri_send('AT+CMGF=1')
    stri_send(chr(13))
    time.sleep(0.5)
    stri_send('AT+CMGS="+917641816981"')
    stri_send(chr(13))
    time.sleep(0.5)
    stri_send('WELCOME')
    stri_send(chr(13))
    time.sleep(0.5)
    stri_send(chr(26))
    print("yes")
    time.sleep(5)
    i=i+1






    
    
    
