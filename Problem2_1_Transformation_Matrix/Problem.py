import numpy as np
import math
from math import radians as rd
import matplotlib.pyplot as plt


o=45
l1=math.sqrt(2)
l2=math.sqrt(5)


x=[0,1,3]
y=[0,1,0]

pxc=0
pyc=0
Pc=np.array([[pxc],[pyc],[1]])
Tcb=np.array([[1,0,-l2],[0,1,0],[0,0,1]])
Tba=np.array([[math.cos(rd(90-o)),-math.sin(rd(90-o)),0],
     [math.sin(rd(90-o)),math.cos(rd(90-o)),-l1],
     [0,0,1]])

print("Pc Matrix:\n",Pc)
print("Tbc Matrix:\n",Tcb)
print("Tba Matrix:\n",Tba)

Pb=Tcb @ Pc
Pa=Tba @ Pb

print("Pb Matrix:\n",Pb)
print("Pa Matrix:\n",Pa)

plt.plot(x,y)
plt.scatter([Pc[0],Pb[0],Pa[0]],[Pc[1],Pb[1],Pa[1]])
plt.show()

