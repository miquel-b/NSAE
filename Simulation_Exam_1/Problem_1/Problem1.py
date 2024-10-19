#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb

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

if __name__=="__main__":

    x=np.array([0,np.pi/3,np.pi/2])
    fx=np.array([0,np.sqrt(3)/2,1])
    
    N=10
    
    p,px=lagrange_poly(x,fx,N)
    
    #Graphs and data visualitzation
    fig, ax = plt.subplots(figsize=(6.5, 4))
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.plot(x,fx,'or',markersize=10,label='data')
    ax.plot(p,px,'ob',markersize=5,label='interpolation')
    ax.plot(p,px,'--b')
    
    ax.legend(loc='best', ncol=2)
    
    plt.show()


