#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb
import sys
sys.path.insert(1, '../Exam1/')
import Useful_functions as nsae

def cubic_spline(x,fx):
    # calculate Cubic Spline using Scipy method
    cs=interpolate.CubicSpline(x,fx,bc_type='natural')
    xr=np.linspace(min(x),max(x)+1,100)
    #Construct the polinomials for each section
    p=[]
    for i in range(len(fx)-1):
        px=cs.c[0,i]*(xr-x[i])**3+cs.c[1,i]*(xr-x[i])**2+cs.c[2,i]*(xr-x[i])+cs.c[3,i]
        p.append(px)
    
    p=np.asarray(p)
    return(cs,p,xr)


b=m=vo=1

#Time points
t=np.array([1,2,3,4])
#Position data points
ft=np.sqrt(t)
#Axis creation

#cubic spline calculation
cs1,p1,tr=nsae.cubic_spline(t,ft)

#Real function 
#xr=m*vo/b*(1-np.exp(-b/m*tr))
ftr=np.sqrt(tr)
#Graphs and data visualitzation
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.set_xlabel('t(s)')
ax.set_ylabel('x(km)')
ax.set_xlim(min(tr),max(tr))
ax.plot(t,ft,'or',markersize=10,label='data')
ax.plot(tr,cs1(tr),color='blue',label='S')
#ax.plot(tr,cs1(tr,1),label="S'")
#ax.plot(tr,cs1(tr,2),label="S''")
#ax.plot(tr,cs1(tr,3),label="S'''")
ax.plot(tr,ftr,'--',linewidth=5,label="x(t)")
#ax.plot(tr,p1[0],'-.',label="p1,2")
#ax.plot(tr,p1[1],'-.',label="p2,3")
#ax.plot(tr,p1[2],'-.',label="p3,4")
#
ax.legend(loc='lower right', ncol=2)

plt.show()
