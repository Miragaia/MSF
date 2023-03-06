# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 18:11:42 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,2000+dt,dt)

ax = np.zeros(t.size)
vx = np.zeros(t.size)
x = np.zeros(t.size)

Cyu = 0.01
Cres = 0.9
area = 0.5
Par = 1.225
m = 60+12
Potencia = 0.48*735.4975
vx[0] = 0.5
g = 9.8
    
for i in range(t.size-1):
    Fcic = Potencia/vx[i]
    FRes = Cres/2*area*Par*vx[i]**2+Cyu*m*g
    F = Fcic - FRes
    ax[i] = F/m  
    vx[i+1] = vx[i] + ax[i]*dt
    x[i+1] = x[i] + vx[i]*dt
    if x[i+1] > 2000:
        break
    
t = t[:i+2]
ax = ax[:i+2]
vx = vx[:i+2]
x = x[:i+2]
    
plt.plot(t,vx, label="velocity")

plt.grid()
print("Metros:",x[-1])
print("Tempo:",t[-1])
print(t[-1]//60,":",t[-1]%60)