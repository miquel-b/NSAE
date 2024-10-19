#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb
import sys
sys.path.insert(1, '../Exam1/')
from Useful_functions import lagrange_poly

x=np.array([1,2,3,4])
fx=np.array([1, np.sqrt(2),np.sqrt(3),np.sqrt(4)])
N=50

p,px=lagrange_poly(x,fx,N)

xreal=np.linspace(min(x),max(x),100)
yreal=np.sqrt(xreal)


#Graphs and data visualitzation
fig, ax = plt.subplots(figsize=(6.5, 4))
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.plot(x,fx,'or',markersize=10,label='data')
ax.plot(p,px,'ob',markersize=5,label='interpolation')
ax.plot(xreal,yreal,'--r',label='y=2*x')

ax.legend(loc='best', ncol=2)

plt.show()


