#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

b=m=vo=1

#Time points
t=np.linspace(0,3,4,dtype=int)
#Position data points
xd=np.array([0,0.63,0.86,0.95])
#Axis creation
tr=np.linspace(0,3.5,1000)

#Real function 
xr=m*vo/b*(1-np.exp(-b/m*tr))

# calculate Cubic Spline using Scipy method
cs=interpolate.CubicSpline(t,xd,bc_type='natural')

#Construct the polinomials for each section
p12=cs.c[0,0]*(tr-t[0])**3+cs.c[1,0]*(tr-t[0])**2+cs.c[2,0]*(tr-t[0])+cs.c[3,0]
p23=cs.c[0,1]*(tr-t[1])**3+cs.c[1,1]*(tr-t[1])**2+cs.c[2,1]*(tr-t[1])+cs.c[3,1]
p34=cs.c[0,2]*(tr-t[2])**3+cs.c[1,2]*(tr-t[2])**2+cs.c[2,2]*(tr-t[2])+cs.c[3,2]


#Graphs and data visualitzation
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.set_xlabel('t(s)')
ax.set_ylabel('x(km)')
ax.set_xlim(0,3)
ax.plot(t,xd,'or',markersize=10,label='data')
ax.plot(tr,cs(tr),color='blue',label='S')
ax.plot(tr,cs(tr,1),label="S'")
ax.plot(tr,cs(tr,2),label="S''")
ax.plot(tr,cs(tr,3),label="S'''")
ax.plot(tr,xr,'--',linewidth=5,label="x(t)")
#ax.plot(tr,p12,'-.',label="p1,2")
#ax.plot(tr,p23,'-.',label="p2,3")
#ax.plot(tr,p34,'-.',label="p3,4")
#
ax.legend(loc='lower right', ncol=2)

plt.show()
