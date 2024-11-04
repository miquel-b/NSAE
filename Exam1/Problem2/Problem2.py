#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt

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
            y[i]=func(yp[i-1],yp[i+1],h)
        err=np.mean(abs(yp-y))
        j+=1

    if(j>=maxiter): 
        print("Max iteration reached", "\n","Not converged")
    
    return(x,y,j)


 

N=100

y0=1
yn=np.exp(-2)
yguess=0.57
x0=0
xn=2


def math_func(yp,yn,h):
    res=((yp)*((3/2/h)-(2/h**2))-yn*((2/h**2)+(3/2/h)))/(1-4/h**2)
    return res

#def math_func(yp,y,yn,h):
#    res=(-3*(yn+yp)/(2*h))+(-2*(yn-2*y+yp)/(h**2))
#    return res

tol=1e-5
maxiter=10000

x,y,iter=jacobi_method(x0,xn,N,y0,yn,yguess,math_func,tol,maxiter)
yreal=np.exp(-x)

#Graphs and data visualitzation
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.set_xlabel('x(m)')
ax.set_ylabel('y(m)')
#ax.set_ylim(0,1)
#ax.set_xlim(0,1)
ax.plot(x,y,'or',markersize=10,label=f'y num {iter} it')
ax.plot(x,yreal,'-b',markersize=10,label='y analytical')

ax.legend(loc='best', ncol=2)

plt.show()

