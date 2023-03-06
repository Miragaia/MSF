import numpy as np
import matplotlib.pyplot as plt

t0 = 0
tf = 1
dt = 0.01
n = int((tf-t0)/dt)
v0 = 100000/3600  #---> alterar(apresentar em km/h)
vT = 100000/3600  #---> alterar(apresentar em km/h)
ang = np.radians(10) #---> alterar angulo
g = 9.8
m = 57/1000   #---> alterar(apresentar em kg)
D = g/(vT**2)

t = np.linspace(t0, tf, n)

x = np.empty(n)
x[0] = 0
y = np.empty(n)
y[0] = 0

v = np.empty(n)
vx = np.empty(n)
vx[0] = v0 * np.cos(ang)
vy = np.empty(n)
vy[0] = v0 * np.sin(ang)

aresx = np.empty(n)
ax = np.empty(n)
aresy = np.empty(n)
ay = np.empty(n)

Em = np.empty(n)
fun = np.empty(n)
int_trab_res = np.empty(n)

for i in range(n-1):
    v[i] = np.sqrt(vx[i]**2 + vy[i]**2)

    aresx[i] = -D*np.abs(v[i])*vx[i]
    ax[i] = aresx[i]
    aresy[i] = -D*np.abs(v[i])*vy[i]
    ay[i] = -g + aresy[i]

    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt

    Em[i] = 0.5*m*(v[i]**2) + m*g*y[i]

    fun[i] = m*aresx[i]*vx[i] + m*aresy[i]*vy[i]
    int_trab_res[i] = dt*((fun[0] + fun[i])/2 + np.sum(fun[1:i]))

v[n-1] = np.sqrt(vx[n-1]**2 + vy[n-1]**2)
Em[n-1] = 0.5*m*(v[n-1]**2) + m*g*y[n-1]

fun[n-1] = m*aresx[n-1]*vx[n-1] + m*aresy[n-1]*vy[n-1]
int_trab_res[n-1] = dt*((fun[0] + fun[n-1])/2 + np.sum(fun[1:n-1]))

for i in range(n):
    if i == 0:
        print("Instante 0:", int_trab_res[i])
    if t[i] < 0.4 < t[i+1]:  #---> alterar(apresentar em segundos)
        print("Instante 0.4:", int_trab_res[i])
    if t[i] < 0.8 < t[i+1]:  #---> alterar(apresentar em segundos)
        print("Instante 0.8:", int_trab_res[i])

plt.plot(t,int_trab_res)
plt.show()
