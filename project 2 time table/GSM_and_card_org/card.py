import RPi.GPIO as led
import time
led.setwarnings(False)
led.setmode(led.BCM)
led.setup(2,led.OUT)
import serial
ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)

valid_data1=[48, 68, 48, 48, 55, 54, 65, 55, 51, 67, 69, 48]
data=[]
valid_data=[50, 48, 48, 48, 50, 65, 48, 51, 53, 65, 53, 51]
while(1):
    global data
    x=list(ser.readall())
    print(x)
    if(x != data):
        data=x
        if (len(data)>1):
            if (data ==valid_data) or (data ==valid_data1) :
                led.output(2,True)
                print("yes")
            else:
                led.output(2,False)
                print("No")
                
        continue;
        
    
