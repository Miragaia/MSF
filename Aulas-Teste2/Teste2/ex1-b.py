# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 17:50:33 2022

@author: draki
"""

import matplotlib.pyplot as plt
import numpy as np


import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
m = 0.45 #massa
r = 11/100
area = np.pi*r**2
PAr = 1.225
TerminalVel = 100*1000/3600
t = np.arange(0,15+dt, dt)
g = -9.8
ang0 = 16/180*np.pi
v0 = 100/3.6 #vel m/s

D = -g /TerminalVel**2
CMag = 0.5*PAr*r*area/m

Wz = -10
# Wy=400 #rad/s
Rx = np.zeros(t.size)
Ry = np.zeros(t.size)
Rz = np.zeros(t.size)

# Rx[0] = 
# Ry[0] = 2.5



Vx = np.zeros(t.size)
Vy = np.zeros(t.size)
Vz = np.zeros(t.size)

Vx[0] = v0*np.cos(ang0)#v0*np.cos(ang0)
Vy[0] = v0*np.sin(ang0)#v0*np.sin(ang0)


for i in range(t.size-1):
    vAbs = np.sqrt(Vx[i]**2+Vy[i]**2+Vz[i]**2)
    
    Amx = CMag * Wz * Vy[i]
    Amy = CMag * Wz * Vx[i]
    # Amz=-CMag * Wy * Vx[i]
    #Não existe Amz pois existe um Wz
    
    Ax = -D*vAbs*Vx[i] + Amx
    Ay =  g -D*vAbs*Vy[i] + Amy
    Az =  -D*vAbs*Vz[i] 

    
    Vx[i+1] = Vx[i]+ Ax*dt
    Vy[i+1] = Vy[i]+ Ay*dt
    Vz[i+1] = Vz[i]+ Az*dt
    
    Rx[i+1] = Rx[i] + Vx[i]*dt
    Ry[i+1] = Ry[i] + Vy[i]*dt
    Rz[i+1] = Rz[i] + Vz[i]*dt
    
    if(Rx[i] > 20):
        break;

t = t[:i+2]
Rx = Rx[:i+2]
Ry = Ry[:i+2]
Rz = Rz[:i+2]
Vx = Vx[:i+2]
Vy = Vy[:i+2]
Vz = Vz[:i+2]

plt.plot(t,Rx, label="X")
plt.plot(t,Ry, label="Y")
plt.plot(t,Rz, label="Z")

plt.legend()
plt.grid()
plt.show()
# plt.plot(Rx,Ry)
plt.show()

aux = np.argmin(abs(Ry[-2:]))
tsolosi = t[-2:][aux]
xsolosi = Rx[-2:][aux]
plt.plot(Rx,Ry)
plt.plot([20],[2.4], "gx")
print("Com RES")
print("Instante de altura máxima")
print(t[np.where(Ry == np.amax(Ry))])
print("Altura máxima")
print(np.amax(Ry))
print("Instante de regresso ao solo")
print(tsolosi)
print("Maximo alcançe")
print(xsolosi)
print(Ry[-1])
        