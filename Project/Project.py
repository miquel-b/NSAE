
import numpy as np
import matplotlib
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


a=np.linspace(np.pi/3,np.pi/2,4,endpoint=True)
l=1
l0=1
iter=7
colors = matplotlib.colormaps['Dark2'].colors

fig1, ax = plt.subplots()
for ind,ai in enumerate(a):
    px=[]
    py=[]
    l=1
    l0=1
    for i in range(iter):
        x,y=fractal(l0,l,ai)
        px.append(x)
        py.append(y)
        l=l/2
    for j in range(len(px)):
        if j==len(px)-1:
            ax.plot(px[j],py[j],'--.',color=colors[ind],label=f"angle={ai/np.pi:.2f}*pi")
        else:
            ax.plot(px[j],py[j],'--.',color=colors[ind],)
    ax.grid(True)
    ax.set_title(f"Fractal angle variable")
    ax.legend()
fig1.tight_layout()

fig2,bx = plt.subplots(4)
for ind,ai in enumerate(a):
    px=[]
    py=[]
    l=1
    l0=1
    for i in range(iter):
        x,y=fractal(l0,l,ai)
        px.append(x)
        py.append(y)
        l=l/2
    for j in range(len(px)):
        bx[ind].plot(px[j],py[j],'--.',color=colors[ind],)
    bx[ind].grid(True)
    bx[ind].set_title(f"Fractal angle={ai/np.pi:.2f}*pi")

fig2.tight_layout()
plt.show()

