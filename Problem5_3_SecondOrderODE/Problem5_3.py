#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
import sys
sys.path.insert(1, '../Exam1/')
from Useful_functions import eulers_ode

def jacobi_method(x0,xn,N,y0,yn,yguess,func,tol,maxiter):
    x=np.linspace(x0,xn,num=N,endpoint=True)
    h=x[1]-x[0]
    y=np.ones(len(x)-2)*yguess
    y=np.insert(y,0,y0)
    y=np.append(y,yn)
    j=0
    err=np.inf
    while(err>tol and j<maxiter):
        yp=np.copy(y)
        for i in range(1,len(y)-1):
            y[i]=func(x[i],yp[i-1],yp[i+1],h)
        err=np.mean(abs(yp-y))
        j+=1

    if(j>=maxiter): 
        print("Max iteration reached", "\n","Not converged")
    
    return(x,y,j)


 

Th=10000 #N
gamma=20 #kg/m
g=9.8 #ms-2
N=50

y0=1
yn=np.exp(2)
yguess=3
x0=0
xn=1


def math_func(x,yp,yn,h):
    res=(yn+yp)/(2+4*(h**2))
    return res

tol=1e-3
maxiter=500

x,y,iter=jacobi_method(x0,xn,N,y0,yn,yguess,math_func,tol,maxiter)
yreal=np.exp(2*x)

#Graphs and data visualitzation
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.set_xlabel('x(m)')
ax.set_ylabel('y(m)')
ax.set_ylim(1,8)
ax.set_xlim(0,1)
ax.plot(x,y,'or',markersize=10,label=f'y num {iter} it')
ax.plot(x,yreal,'-b',markersize=10,label='y analytical')

ax.legend(loc='best', ncol=2)

plt.show()

