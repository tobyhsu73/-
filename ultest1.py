import serial
import time



ser2 = serial.Serial('COM10',9600)


while True:
    
    ser2.flushInput()
    t1 = ser2.read(1)
    t2 = ser2.read(1)
    t3 = ser2.read(1)
    t4 = ser2.read(1)
    
   

   
    print(t1,t2,t3,t4)
    
    
    y=(t2[0])*256+(t3[0])
    print(y)
    time.sleep(0.5)
    