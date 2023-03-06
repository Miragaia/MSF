import matplotlib.pyplot as plt
import numpy as np

dt = 0.001
dphi = 0.1
angle = 10

angleArr = []
alcanceArr = []
while angle < 45:
    angleArr.append(angle)
    ang0 = angle/180*np.pi
    g = -9.8
    t = np.arange(0,10+dt,dt)
    x = np.zeros(t.size)
    y = np.zeros(t.size)

    vx = np.zeros(t.size)
    vy = np.zeros(t.size)
    v0 = 230/3.6   #---> alterar (apresentar em m/s)

    D = -g/(6.8**2)
    
    y[0] = 2.5    #---> alterar (apresentar em m)

    vx[0] = v0*np.cos(ang0)
    vy[0] = v0*np.sin(ang0)



    for i in range(t.size-1):
        vv = np.sqrt(vx[i]**2+vy[i]**2)
    
        ax = -D*vv*vx[i]
        ay = g-D*vv*vy[i]
        
        vx[i+1] = vx[i] + ax * dt
        vy[i+1] = vy[i] + ay * dt
    
        x[i+1] = x[i] + vx[i] * dt
        y[i+1] = y[i] + vy[i] * dt
        if y[i+1] < 0:
            break;

    t = t[:i+2]
    vx = vx[:i+2]
    vy = vy[:i+2]
    x = x[:i+2]
    y = y[:i+2]

    angle += dphi
    alcanceArr.append(x[-1])
    
max_index = alcanceArr.index(max(alcanceArr))
print(alcanceArr[max_index])   #--> print do angulo máximo
print(angleArr[max_index])      #-->print do alcance máximo