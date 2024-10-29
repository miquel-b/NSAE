#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
import pdb

plt.close('all')

t1=30.
t2=20.
t3=15.
t4=15.
tg=np.mean([t1,t2,t4,t4])
#tg=10
N=500

yy,xx=np.mgrid[0:N,0:N]

t=np.array([np.insert([0,0],1,np.ones(N-2)*t1)])
t=np.append(t,np.tile(np.insert([t2,t3],1,np.ones(N-2)*tg),(N-2,1)),axis=0)
t=np.append(t,np.array([np.insert([0,0],1,np.ones(N-2)*t4)]),axis=0)

print('yy=',yy)
print('xx=',xx)
print('t=',t)

told=t.copy()
told.fill(0)
err=np.mean(abs(told-t))

tol=1e-4

while(err>tol):
    told=t.copy()
    for i in range(1,len(t)-2):
        for j in range(1,len(t)-2):
            t[j][i]=(told[i+1][j]+told[i-1][j]+told[i][j+1]+told[i][j-1])/4
    err=np.mean(abs(told-t))

print('yy=',yy)
print('xx=',xx)
print('t=',t)
print('err=',err)

fig1 = plt.figure()
ax = fig1.add_subplot(projection='3d')
ax.scatter(xx, yy, t)
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('T Label')

fig2 = plt.figure()
#ax = fig.add_subplot(projection='3d')
bx = fig2.add_subplot()
grid=bx.scatter(xx, yy, c=t, cmap='inferno')
bx.set_xlabel('X Label')
bx.set_ylabel('Y Label')
#ax.set_zlabel('T Label')
fig2.colorbar(grid,label='Temperature (ºC)')

fig3 = plt.figure()
cx = fig3.add_subplot(projection='3d')
dgrid=cx.scatter(xx, yy, t,c=t, cmap='inferno')
cx.set_xlabel('X Label')
cx.set_ylabel('Y Label')
cx.set_zlabel('T Label')
fig3.colorbar(dgrid,label='Temperature (ºC)')


plt.show()

