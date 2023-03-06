# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 15:17:41 2022

@author: cient
"""

import matplotlib.pyplot as plt
import numpy as np


dt = 0.01
t = np.arange(0, 400, dt)
x = np.zeros(t.size) 
v = np.zeros(t.size)
a = np.zeros(t.size)  
Ep = np.zeros(t.size) 
Em = 4
 
k = 2
Beta = 0.02
alfa = -0.1
m = 0.5

x[0] = 0
v[0] = np.sqrt(2*(Em/m))


for i in range(0, t.size-1):
    a[i] = (-k*x[i]-3*alfa*x[i]**2-Em*Beta*x[i]**4)/m
    v[i+1] = v[i]+a[i]*dt
    x[i+1] = x[i]+v[i+1]*dt

for i in range(0, t.size-1): 
    Ep[i] = 0.5*k*x[i]**2 + alfa*x[i]**3 - Beta*x[i]**4

Ep[-1] = 0.5*k*x[-1]**2 + alfa*x[-1]**3 - Beta*x[-1]**4
plt.ylabel("Energia potêncial (J)")
plt.xlabel("posição (m)")       
plt.grid()
plt.plot(x, Ep, '--')
plt.ylim([0, 4])
#plt.xlim([-2,3])
plt.plot(x, np.zeros(x.size))