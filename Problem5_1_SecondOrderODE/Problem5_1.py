#!/usr/bin/env python3

import numpy as np
import math
import matplotlib.pyplot as plt
plt.rcParams['text.usetex'] = True
import seaborn as sns
sns.set_theme()

plt.close('all')

def leap_frog_ode(t0,tn,y0,dy0,N,func):
    t=np.linspace(t0,tn,num=N,endpoint=True)
    h=t[1]-t[0]
    
    y1=np.array([y0])
    y2=np.array([dy0])
    
    for i in range(0,N-1):
        y1=np.append(y1,y1[i]+h*y2[i])
        y2=np.append(y2,y2[i]+h*func(y1[i],y2[i]))
    
    dy2=func(y1,y2)
    return(t,y1,y2,dy2)


b=m=1
N=50
t0=0
tn=5

y10=0
y20=1

t,y1,y2,dy2=leap_frog_ode(t0,tn,y10,y20,N,lambda y,dy: (-b/m)*dy+0*y)

yreal=(m*y20/b)*(1-np.exp(-b*t/m))
dyreal=y20*np.exp(-b*t/m)
ddyreal=-(y20*b/m)*np.exp(-b*t/m)

#Graphs and data visualitzation using seaborn
fig, ax = plt.subplots(3,1,sharex=True)

ax[2].set_xlabel('t(s)')
ax[0].set_ylabel('y(m)')
ax[1].set_ylabel('v(m/s)')
ax[2].set_ylabel(r'$a(m/s^2)$')
for i in range(3):
    ax[i].set_xlim(0,5)

sns.scatterplot(x=t,y=y1,ax=ax[0],label='y (leapfrog)',hue=1,palette='plasma',legend=False)
sns.scatterplot(x=t,y=y2,ax=ax[1],label="y'",hue=2,palette='cividis',legend=False)
sns.scatterplot(x=t,y=dy2,ax=ax[2],label="y''",hue=3,palette='Accent',legend=False)
sns.lineplot(x=t,y=yreal,ax=ax[0],
             label=r'\[f(t)=\frac{mv_o}{b}(1-exp\left(-\frac{b}{m}t\right))\]',hue=1,palette='plasma',legend=False)
sns.lineplot(x=t,y=dyreal,ax=ax[1],
             label=r"\[f'(t)=v_oexp\left(-\frac{b}{m}t\right)\]",hue=2,palette='cividis',legend=False)
sns.lineplot(x=t,y=ddyreal,ax=ax[2],
             label=r"\[f(t)=-\frac{bv_o}{m}exp\left(-\frac{b}{m}t\right)\]",hue=3,palette='Accent',legend=False)
#ax.set_title('Analytical vs Numerical solution')
fig.tight_layout()
fig.subplots_adjust(right=0.72) 
fig.legend(loc='outside center right')
plt.show()   
