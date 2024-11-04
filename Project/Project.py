
import numpy as np 
import matplotlib.pyplot as plt

def fractal(l0,l,a):
    px=[l0]
    py=[0]
    px.append(l0-l*np.cos(a))
    py.append(l*np.sin(a))
    px.append(l0-l*np.cos(-a))
    py.append(l*np.sin(-a))
    px.append(px[0])
    py.append(py[0])
    return px,py



l=1
l0=1
a=np.pi/3
iter=7
px=[]
py=[]


for i in range(iter):
    x,y=fractal(l0,l,a)
    px.append(x)
    py.append(y)
    l=l/2

fig, ax = plt.subplots()
for j in range(len(px)):
    ax.plot(px[j],py[j],'--.')
ax.grid(True)
ax.set_xlim(0,1.5)
plt.show()

