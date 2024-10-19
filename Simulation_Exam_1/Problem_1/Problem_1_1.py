#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate
import pdb
from Problem1 import lagrange_poly

x=np.array([-1,0,1,2])
fx=np.array([2.2,1.2,0.8,1])

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




