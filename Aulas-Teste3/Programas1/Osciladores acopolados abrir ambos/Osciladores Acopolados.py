# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 19:33:39 2022

@author: draki
"""
from maxminv import maxminv, abfourier
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

modo=np.array([ 0.20890613, 0.27790793, 0.29974889, 0.27072261, 0.19575483, 0.08756756, -0.03547988, -
0.15250641, -0.24365267, -0.2934512 , -0.2934512 , -0.24365267, -0.15250641, -0.03547988, 0.08756756,
0.19575483, 0.27072261, 0.29974889, 0.27790793, 0.20890613])
fig1, ax = plt.subplots(1, 3, figsize=(13,6))

xeq=np.array([1. , 1.2, 1.4, 1.6, 1.8, 2. , 2.2, 2.4, 2.6, 2.8, 3. , 3.2, 3.4, 3.6, 3.8, 4. , 4.2, 4.4, 4.6, 4.8])
print(modo.size)
print(xeq.size)

ax[2].plot(xeq, modo, 'x')

ind_peaks = find_peaks(modo)[0]
n = np.arange(0,11,1)
Aaf = np.zeros(n.size)
Abf = np.zeros(n.size)
tmax = np.zeros(ind_peaks.size)
angmax = np.zeros(ind_peaks.size)

for i in range(tmax.size):
    k = ind_peaks[i]
    tmax[i], angmax[i] = maxminv(xeq[k-1],xeq[k],xeq[k+1],modo[k-1],modo[k],modo[k+1])
    
Ang_Num = angmax[-1]
T_Num = (tmax[-1]-tmax[-2])
print("\nA amplitdue é {:0.5f}º".format(Ang_Num))
print("\nO periodo é {:0.5f}s".format(T_Num))
for i in range(n.size):
    Aaf[i],Abf[i] = abfourier(xeq, modo, ind_peaks[-2], ind_peaks[-1], i)

print("\n{:^15}{:^15}{:^15}{:^15}".format("n","an","bn","sqrt(an^2+bn^2)"))
for i in range(n.size):
    print("{:^15}{:^15.5f}{:^15.5f}{:^15.5f}".format(n[i],Aaf[i],Abf[i],np.sqrt(Aaf[i]**2+Abf[i]**2)))

ax[0].bar(n,abs(Aaf),width=0.1, edgecolor="white", linewidth=0.7)
ax[1].bar(n,abs(Abf),width=0.1, edgecolor="white", linewidth=0.7)

values = np.zeros(xeq.size)
#for i in range(xeq.size-1):
#    values[i] = Aaf[0]/2 + Aaf[1]*np.cos(2*np.pi/3.02*xeq[i]) + Abf[1]*np.sin(2*np.pi/3.02*xeq[i])
#    print(values)

# ^ this works but its manually done using a0/2 + SUM(an*np.cos(n*2pi/period*t) + bn*np.sin(n*2*pi/period * t))
#   so fourier = 1


#  this should work for any fourier = n  
#= a1/2 + sum(an*cos(n * 𝜔 * 𝑡) + bn*sin(n * 𝜔 * t))
#for i in range(n.size):
#        ax[2].plot(xeq, Aaf[i]*np.cos(i*2*np.pi/3.02*xeq) + Abf[i]*np.sin(i*2*np.pi/3.02*xeq))
        
for i in range(n.size):
        ax[2].plot(xeq, np.sqrt(Aaf[i]**2+Abf[i]**2)*np.cos(i*2*np.pi/3*(xeq-1.4)))


# -1.4 to offset the axis so cossine = 1 when xeq is at a maximum position