import matplotlib.pyplot as plt
import numpy as np


g= 9.80
dt= 0.1
tf=4.0
t0= 0
n=np.int((tf-t0)/dt+0.1)
print('n = ',n)
t=np.zeros(n+1)
vy=np.zeros(n+1)
y=np.zeros(n+1)
g=9.80
v0y=0
y0=0
t[0]=t0
vy[0]=v0y
y[0]=y0



for i in range(n): # Método de Euler
    t[i+1]=t[i]+dt
    ax=g
    vy[i+1]=vy[i]+ax*dt
    y[i+1]=y[i]+vy[i]*dt

print(g*3,"\n")

print("Velocidades: \n")
for i in range(n):            #velocidades
    if(t[i+1]>3-2*dt and t[i+1]<3+2*dt):
        print(t[i],vy[i])
print("\n")
print("Posições: \n")
for i in range(n):             #posições
    if (t[i+1]>2-2*dt and t[i+1]<2+2*dt):
        print(t[i+1],y[i+1])

print("Y exato= ", 0.5*g*4)

x=[0.1,0.01,0.001]
y=[0.98,0.098,0]
plt.scatter(x,y)
plt.plot(x, y)
plt.show()

    




