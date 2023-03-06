# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 17:17:01 2022

@author: draki
"""


import matplotlib.pyplot as plt
import numpy as np

dt = 0.001

t = np.arange(0,10+dt,dt)

Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

Ax = np.zeros(t.size)
Ay = np.zeros(t.size)
Az = np.zeros(t.size)

Rx[0] = 0

alturadabaliza = 20

V0 = 100/3.6

ang = 16/180*np.pi

g = -9.8
vt = 100/3.6

dres=g/vt**2

Vx[0] = V0 * np.cos(ang)
Vy[0] = V0 * np.sin(ang)

for i in range(t.size-1):
    vv=np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    Ax[i] = -dres*vv*Vx[i]    
    Ay[i] = g -dres*vv*Vy[i]
    Az[i] = 0
    
    Vx[i+1] = Vx[i] + Ax[i]*dt
    Vy[i+1] = Vy[i] + Ay[i]*dt
    Vz[i+1] = Vz[i] + Az[i]*dt
    
    Rx[i+1] = Rx[i] + Vx[i]*dt
    Ry[i+1] = Ry[i] + Vy[i]*dt
    Rz[i+1] = Rz[i] + Vz[i]*dt
    if Rx[i] > 20 or Ry[i] < 0:
        break;
        
t = t[:i+2]
Rx = Rx[:i+2]
Ry = Ry[:i+2]
Rz = Rz[:i+2]
Vx = Vx[:i+2]
Vy = Vy[:i+2]
Vz = Vz[:i+2]
Ax = Ax[:i+2]
Ay = Ay[:i+2]
Az = Az[:i+2]

plt.plot(Rx,Ry)
print(Ry[-2])
print(Rx[-2])
