import numpy as np

v0 = 130000/3600
vT = 100000/3600
t0 = 0
tf = 2
dt = 0.0001
n = int((tf-t0)/dt)
ang = np.radians(10)
m = 57/1000  #----> (apresentar em Kg)
d = 67/1000  #----> (apresentar em metros)
r = d/2
g = 9.8
omega = 100 #---> (rotação sobre o eixo z)
A = np.pi*(r**2)
dar = 1.225
mag = (0.5*A*dar*r)/m
D = g/(vT**2)

t = np.linspace(t0, tf, n)

x = np.empty(n+1)
x[0] = -10   #---> alterar (X inicial)
y = np.empty(n+1)
y[0] = 1     #---> alterar (Y inicial)
z = np.empty(n+1)
z[0] = 0      #---> alterar (Z inicial)

v = np.empty(n+1)
vx = np.empty(n+1)
vx[0] = v0 * np.cos(ang)
vy = np.empty(n+1)
vy[0] = v0 * np.sin(ang)
vz = np.empty(n+1)
vz[0] = 0

ax = np.empty(n+1)
ay = np.empty(n+1)
az = np.empty(n+1)

for i in range(n):
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)

    amx = -mag * omega * vy[i]
    amy = mag * omega * vx[i]

    ax[i] = -D*np.abs(v[i])*vx[i] + amx
    ay[i] = -g - D*np.abs(v[i])*vy[i] + amy
    az[i] = 0

    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt
    vz[i+1] = vz[i] + az[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt
    z[i+1] = z[i] + vz[i]*dt

for i in range(n):
    if y[i+1] < y[i]:
        print("Altura máxima: ", y[i])
        break

for i in range(n):
    if y[i+1]*y[i] < 0:
        print("Alcance: ", x[i])
        break