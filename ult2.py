import serial
import time

ser2 = serial.Serial('COM15',9600)


def read():
    
    ser2.flushInput()
    t1 = ser2.read(1)
    t2 = ser2.read(1)
    t3 = ser2.read(1)
    t4 = ser2.read(1)



    

    z=(t2[0])*256+(t3[0])
    time.sleep(0.5)
    with open("real.txt","a") as f:
        txt=str(z)
        f.write(txt+'\n')
    return z

