#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb
import sys
sys.path.insert(1, '../Exam1/')
from Useful_functions import lagrange_poly


def create_htm(R,O):
    if O.shape!=(R.shape[0],1):
        O=O.reshape(R.shape[0],1)

    T=np.hstack((R,O))
    c=np.zeros(T.shape[1]-1)
    c=np.append(c,np.array([1]))
    T=np.vstack((T,c))

    return(T)

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

def inversion_htm(R,O):
    if O.shape!=(R.shape[0],1):
        O=O.reshape(R.shape[0],1)

    T=np.hstack((R,-R*O))
    c=np.zeros(T.shape[1]-1)
    c=np.append(c,np.array([1]))
    T=np.vstack((T,c))

    return(T)



t=np.linspace(0,2*np.pi,100)
#Pax=Pay=Paz=Qax=Qay=Qaz=[]
Pai=[]
Qai=[]
for ti in t:

    Rx=rotation_matrix_creation(0,'x')
    Ry=rotation_matrix_creation(0,'y')
    Rz=rotation_matrix_creation(2*np.pi*ti/3,'z')
    
    Rba=Rx@Ry@Rz
    Oba=np.array([[ti],
                  [2*ti],
                  [0]])
    Tba=create_htm(Rba,Oba)
    Pb=np.array([[1],
                 [1],
                 [0]])
    
    Pa=Tba@np.vstack((Pb,1))
    Pa=np.delete(Pa,-1,axis=0)
    
    Qb=np.array([[np.cos(2*np.pi*ti/5)],
                 [-np.cos(2*np.pi*ti/5)],
                 [0]])
    Qa=Tba@np.vstack((Qb,1))
    Qa=np.delete(Qa,-1,axis=0)

    Pa=Pa.flatten()
    Qa=Qa.flatten()
    Pai.append(Pa)
    Qai.append(Qa)

Pai=np.asarray(Pai)
Qai=np.asarray(Qai)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.scatter(0, 0,0, marker='x')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.scatter(Pai[:,0], Pai[:,1],Pai[:,2], marker='o',color='r',label='P')
ax.scatter(Qai[:,0], Qai[:,1],Qai[:,2], marker='+',color='b',label='Q')
ax.legend()

plt.show()




