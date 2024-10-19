#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

#Interpolation using lagrange polynomial
def lagrange_poly(x,fx,N):

    p=np.linspace(x[0],x[-1],N,endpoint=True)
    #p=np.insert(p,0,x[0]-1)
    #p=np.append(p,x[-1]+1)
    px=np.array([])
    
    for xi in p:
        c=np.array([])
        for i,j in enumerate(x):
            s=np.delete(x,i)
            n=xi-s
            n=np.prod(n)
            d=j-s
            d=np.prod(d)
            c=np.append(c,(n/d)*fx[i])
    
        px=np.append(px,np.sum(c))
    
    return(p,px)


#Eulers centered method to solve second order ODE
#Usage:
# t,y1,y2,dy2=eulers_ode(t0,tn,N,lambda r:(-G*Me/((r)**2))) where r is the 0 order function
def eulers_ode(t0,tn,y0,dy0,N,func):
    t=np.linspace(t0,tn,num=N,endpoint=True)
    h=t[1]-t[0]
    
    
    y1=np.array([y0])
    y2=np.array([dy0])
    
    for i in range(0,N-1):
        xa=t[i]+(h/2)
        y1a=y1[i]+(h/2)*y2[i]
        y2a=y2[i]+(h/2)*func(y1[i],y2[i])
        y1=np.append(y1,y1[i]+h*y2a)
        y2=np.append(y2,y2[i]+h*func(y1a,y2a))
    
    
    dy2=func(y1,y2)
    return(t,y1,y2,dy2)
    

