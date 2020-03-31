import time
import serial
import sys
ser=serial.Serial(port='/dev/ttyS0',baudrate=9600,parity=serial.PARITY_NONE,timeout=1)

valid_data1=[48, 68, 48, 48, 55, 54, 65, 55, 51, 67, 69, 48]
data=[]
valid_data=[52, 50, 48, 48, 54, 66, 52, 48, 48, 50, 54, 66]

def Validate_card():
    count=0;
    validate = 'no'
    while(count<8):
  
        global data
        x=list(ser.readall())
        print(x)
        if(x != data):
            data=x
            if (len(data)>1):
                if (data ==valid_data) or (data ==valid_data1) :
                    print("yes")
                    validate='yes'
                    break;
                else:
                    print("No")
                    validate='no'
                    break;
        count=count+1;
        print(count)
                
                
                        
    return validate




if __name__ == '__main__':
    a=Validate_card()
    print('outside'+a)
