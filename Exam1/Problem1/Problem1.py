#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb
plt.close('all')

w=0.5
p=5
N=300
t=np.linspace(-2*np.pi,2*np.pi,N,endpoint=True)

Pax=(p/(1+np.cos(w*t)))*np.cos(w*t)
Pay=(p/(1+np.cos(w*t)))*np.sin(w*t)

y=np.linspace(-500,500,N)
x=p/2-(y**2)/(2*p)


plt.plot(x,y,label='Parabola x(y)')
plt.scatter(Pax,Pay,color='r',label='Pa(wt)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

