# coding=utf-8
import matplotlib.pyplot as plt

with open("real.txt","r") as f:
    data=f.readlines()
for n in range(0,len(data)):
    data[n]=int(data[n])
x=range(0,len(data))
figure, ax = plt.subplots()
plt.plot(x,data)
plt.plot(x,data)

print(len(data))
ax.set_title('Waterproof ultrasonic test(2HR)')
ax.set_xlabel('time(0.5s)')
ax.set_ylabel('distance(mm)')
ax.set_ylim([0, 1000])
ax.set_xlim([1200, 2400])
plt.show()