import math
import matplotlib.pyplot as plt
import numpy as np

To=50
Ts=-4
k=4.5

dt=0.1
t=0
Ta=Ts+(To-Ts)*math.exp(-k*t)
Tb=0.001
count=0
tx=[t]
y=[Ta]

while(abs((Ta-Tb)/Tb)>(10**(-8))):
    t=t+dt
    Tb=Ta
    Ta=Ts+(To-Ts)*np.exp(-k*t)
    tx.append(t)
    y.append(Ta)
    count+=1
    if(count>(10**4)):
       print('Too much interation')
       break

print('The reached t=',t)
print('Ts=',Ts,'\n','T=',Ta)

plt.plot(tx,y,'ob')

tr=np.linspace(0,5,1000,endpoint=True)
yr=Ts+(To-Ts)*np.exp(-k*tr)
plt.plot(tr,yr,'-r')
plt.show()


