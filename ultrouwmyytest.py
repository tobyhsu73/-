import serial
import time
port = 'COM15'
baud = 9600
ser = serial.Serial(port,baud)
ser2 = serial.Serial('COM12',9600)
i=0
#讀取感測資料
def readsensor():
    ser2.flushInput()
    t1 = ser2.read(1)
    t2 = ser2.read(1)
    t3 = ser2.read(1)
    t4 = ser2.read(1)
    
    ser.flushInput()
    p1 = ser.read(1)
    p2 = ser.read(1)
    p3 = ser.read(1)
    p4 = ser.read(1)
    
    if t1 != b'\xff' or p1 != b'\xff':
        d=1
    else:
        d=0
        
        

    
    x=(p2[0])*256+(p3[0])
    y=(t2[0])*256+(t3[0])
    print(x,y)
    
    time.sleep(0.3)
    return(x,y,d)
    
while True:
    
    value1=readsensor()
    x1=value1[0]
    y1=value1[1]
    d1=value1[2]
    
    value2=readsensor()
    x2=value2[0]
    y2=value2[1]
    d2=value2[2]

    res1=abs(x1-x2)
    res2=abs(y1-y2)


    if res1 >= 200 or res2 >= 200:
        continue

    elif d1==1 or d2 ==1:
        continue
    else:
        print(i)
        with open("ex3-5.txt","a") as f:
            txt=str(x1)
            f.write(txt+',')
        with open("ex3-6.txt","a") as f:
            txt=str(y1)
            f.write(txt+',')
        i=i+1
        if i ==14400:
            break
    
      
    
    
    
    
    
    
'''    
with open("ex3-3.txt","a") as f:
    txt=str(x)
    f.write(txt+',')
with open("ex3-4.txt","a") as f:
    txt=str(y)
    f.write(txt+',')
i=i+1
if i ==14400:
    break
'''   
