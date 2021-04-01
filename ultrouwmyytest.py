import serial
import time
port = 'COM15'
baud = 9600
ser = serial.Serial(port,baud)
ser2 = serial.Serial('COM11',9600)


while True:
    ser.flushInput()
    ser2.flushInput()
    t1 = ser2.read(1)
    t2 = ser2.read(1)
    t3 = ser2.read(1)
    t4 = ser2.read(1)
    
    p1 = ser.read(1)
    p2 = ser.read(1)
    p3 = ser.read(1)
    p4 = ser.read(1)

    print(p1,p2,p3,p4)
    print(t1,t2,t3,t4)
    
    x=(p2[0])*256+(p3[0])
    y=(t2[0])*256+(t3[0])
    print(x,y)
    time.sleep(0.5)
    with open("ex2-1.txt","a") as f:
        txt=str(x)
        f.write(txt+',')
    with open("ex2-2.txt","a") as f:
        txt=str(y)
        f.write(txt+',')
    