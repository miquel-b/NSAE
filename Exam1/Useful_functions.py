#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate

#Interpolation using lagrange polynomial
def lagrange_poly(x,fx,N):
    '''
    x=known x points
    fx=known f(x) points
    N=Number of points to interpolate
    
    Return:
            p=x values where the polynomial has been evaluated (arr)
            px= p(x) points where interpolation has been evaluated
    '''


    p=np.linspace(x[0],x[-1],N)
    p=np.sort(np.append(p,x)) 
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

#Natural cubic spline interpolation using scipy
def cubic_spline(x,fx):
    '''
    x=known x points
    fx=known f(x) points
    
    Return:
            cs=Scipy cubic spline polynomial, can be plotted directly ax.plot(x,cs(x),color='blue',label='S') it can also calculate derivatives using cs(x,n) for n order derivative. It can also print coeficents by cs.c[0,n]*(x-xj)³+cs.c[1,n]*(x-xj)²+cs.c[2,n]*(x-xj)+cs.c[3,n], n being each polynomial.
            Esencially equivalent to aj,bj,cj,dj coefficents of documentation pdf pag 25 eq. 17.
            p= p(x) points where interpolation has been evaluated for xr arr(arr())
            xr= 100 points where the polynomial has been evaluated useful for plotting
    '''

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

#Eulers centered method to solve second order ODE
#Usage:
# t,y1,y2,dy2=eulers_ode(t0,tn,N,lambda t,r,dr:(-G*Me/((r)**2))) where r is the 0 order function
def eulers_ode(t0,tn,y0,dy0,N,func):
    '''
    t0=lower integration interval
    tn=upper integration interval
    y0=boundary condition 0 order derivative f(t=0)
    dy0=boundary condition 1 order dreivative f'(t=0)
    N=Number of points
    func=reference to mathematical expression of euler-centerd algorithm f(t,y1,y2)
    
    Return:
           t=intergration interval (arr)
           y1=f(t) numericaly integrated set of points (arr)
           y2=f'(t) numericaly integrated set of points (arr)
           dy2=f''(t) numericaly calculated f''(t)=f(t,y1,y2) using explicit func argument (arr)
    '''

    t=np.linspace(t0,tn,num=N,endpoint=True)
    h=t[1]-t[0]
    
    
    y1=np.array([y0])
    y2=np.array([dy0])
    
    for i in range(0,N-1):
        xa=t[i]+(h/2)
        y1a=y1[i]+(h/2)*y2[i]
        y2a=y2[i]+(h/2)*func(y1[i],y2[i])
        y1=np.append(y1,y1[i]+h*y2a)
        y2=np.append(y2,y2[i]+h*func(xa,y1a,y2a))
    
    
    dy2=func(t,y1,y2)
    return(t,y1,y2,dy2)
    

#Leap-frog method to solve second order ODE
#Usage:
#t,y1,y2,dy2=leap_frog_ode(t0,tn,y10,y20,N,lambda y,dy: (-b/m)*dy+0*y)
def leap_frog_ode(t0,tn,y0,dy0,N,func):
    '''
    t0=lower integration interval
    tn=upper integration interval
    y0=boundary condition 0 order derivative f(t=0)
    dy0=boundary condition 1 order dreivative f'(t=0)
    N=Number of points
    func=reference to mathematical expression of leap-frog algorithm f(t,y1,y2)
    
    Return:
           t=intergration interval (arr)
           y1=f(t) numericaly integrated set of points (arr)
           y2=f'(t) numericaly integrated set of points (arr)
           dy2=f''(t) numericaly calculated f''(t)=f(t,y1,y2) using explicit func argument (arr)
    '''
    t=np.linspace(t0,tn,num=N,endpoint=True)
    h=t[1]-t[0]
    
    y1=np.array([y0])
    y2=np.array([dy0])
    
    for i in range(0,N-1):
        y1=np.append(y1,y1[i]+h*y2[i])
        y2=np.append(y2,y2[i]+h*func(t[i],y1[i],y2[i]))
    
    dy2=func(t,y1,y2)
    return(t,y1,y2,dy2)


#Jacobi method
def jacobi_method(x0,xn,N,y0,yn,yguess,func,tol,maxiter):
    '''
    x0=lower integration interval
    xn=upper integration interval
    N=Number of points
    y0=boundary conditon origin f(x=0)
    yn=boudary condition end f(x=n)
    yguess=initial guess for all of inner interval should be a value y0<yguess<yn
    func=is the reference to the mathematical function used to calculate y_ij, ref to pdf Second order ODE pag 16. f(x,y_i-1,y_i+1,h)
    tol=minimum difference between iterations, stoppage condition
    maxiter=maximum iteration, in case of no convergance.

    Return:
            x=interval of integration spaced by h (arr)
            y=numericaly calculated integrated function (arr)
            j=number of iterations used (int)
    '''
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

#Creation of a Homogenous Transformation Matrix
def create_htm(R,O):
    if O.shape!=(R.shape[0],1):
        O=O.reshape(R.shape[0],1)

    T=np.hstack((R,O))
    c=np.zeros(T.shape[1]-1)
    c=np.append(c,np.array([1]))
    T=np.vstack((T,c))

    return(T)

#Creation of a rotation matrix depending on the angle of rotation along which axis
def rotation_matrix_creation(angle,axis):
#Angles must be in radians
    if axis=='x':
        R=np.array([[1,0,0],
                    [0,np.cos(angle),-np.sin(angle)],
                    [0,np.sin(angle),-np.cos(angle)]])
    elif axis=='y':
        R=np.array([[np.cos(angle),0,np.sin(angle)],
                    [0,1,0],
                    [-np.sin(angle),0,np.cos(angle)]])
    elif axis=='z':
        R=np.array([[np.cos(angle),-np.sin(angle),0],
                    [np.sin(angle),np.cos(angle),0],
                    [0,0,1]])
    return(R)

#inversion of a HTM to reverse the direction of it
def inversion_htm(R,O):
    if O.shape!=(R.shape[0],1):
        O=O.reshape(R.shape[0],1)

    T=np.hstack((R,-R*O))
    c=np.zeros(T.shape[1]-1)
    c=np.append(c,np.array([1]))
    T=np.vstack((T,c))

    return(T)

