#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb

plt.close('all')

def eulers_ode(t0,tn,N,func):
    t=np.linspace(t0,tn,num=N,endpoint=True)
    h=t[1]-t[0]
    
    y10=r0
    y20=v0
    
    y1=np.array([y10])
    y2=np.array([y20])
    
    for i in range(0,N-1):
        xa=t[i]+(h/2)
        y1a=y1[i]+(h/2)*y2[i]
        y2a=y2[i]+(h/2)*func(y1[i])
        y1=np.append(y1,y1[i]+h*y2a)
        y2=np.append(y2,y2[i]+h*func(y1a))
    
    
    dy2=func(y1)
    return(t,y1,y2,dy2)
    
    #Exemple:
    # t,y1,y2,dy2=eulers_ode(t0,tn,N,lambda r:(-G*Me/((r)**2))) where r is the 0 order function

if __name__=="__main__":

    Me=5.97e24 #kg
    Re=6400 #km
    G=6.67e-20*(3600**2) #km3/kg/s2 * 3600**2s2/1h2
    
    N=500
    r0=Re
    v0=10 #km/s *3600s/1h
    v0=v0*3600 #km/h
    t0=0 #h
    tn=3 #h
    
    t,y1,y2,dy2=eulers_ode(t0,tn,N,lambda r:(-G*Me/((r)**2)))
    print('y1=', y1, '\n')
    print('y2=', y2, '\n')
    
    yreal=1/((1/(G*Me))*(((G*Me)/Re)+0.5*((y2**2)-(v0**2))))
    
    
    #Graphs and data visualitzation
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.set_xlabel('t')
    ax.set_ylabel('r')
    ax.plot(t,y1,'or',markersize=10,label='numerical')
    ax.plot(t,yreal,'ob',markersize=5,label='analytical')
    ax.plot(t,yreal,'--b')
    
    ax.legend(loc='best', ncol=2)
    
    plt.show()

