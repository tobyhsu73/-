# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 20:24:30 2021

@author: willy
"""

import serial
import time

#ser = serial.Serial("port",9600)

def reads():
    '''
    ser.flushInput()
    while(True):
        while(ser.read(1) != 0xFF):
            pass
        data = ser.read(3)
        if data[2] == (0xff+data[0]+data[1])%255:
            dist = data[0]*256+data[1]
            break
        else:
            pass
    '''
    dist = 123
    return dist

coordinate = input("請輸入座標 x.y ")
print("座標為 "+coordinate)


dist = []
for n in range(0,30):
    dist.append(reads())

with open("超音波_1.txt", "a", encoding="utf8") as fp:
    fp.write(coordinate+" : "+repr(dist)+' ,\n')



    
    
