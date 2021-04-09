# coding=utf-8
import matplotlib.pyplot as plt
y=[]
y2=[]
with open("ex2-1.txt","r") as f:
    data=f.readlines()
with open("ex1-1.txt","r") as f:
    data2=f.readlines()
for n in range(0,len(data)):
    data[n]=int(data[n])
    
    y.append(data[n])
for n in range(0,len(data2)):
    data2[n]=int(data2[n])
    
    y2.append(data2[n])
x=range(0,len(y))
x2=range(0,len(y2))
p1,=plt.plot(x,y)

figure, ax = plt.subplots()
p1,=plt.plot(x,y)
p2,=plt.plot(x2,y2)



print(len(data))
ax.set_title('Waterproof ultrasonic test(2HR)')
ax.set_xlabel('time(s)')
ax.set_ylabel('distance(mm)')
ax.set_ylim([460, 464])
ax.set_xlim([0, 1500])
ax.annotate('Sampling interval 0.5s', xy=(10000,288))

plt.legend([p1,p2],['processed','nonproccessed'],loc = 'lower left',scatterpoints=1)
figure2, ax = plt.subplots()
p2,=plt.plot(x2,y2)
ax.set_ylim([461.8, 463.2])
ax.set_xlim([0, 1500])
plt.show()