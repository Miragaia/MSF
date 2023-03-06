import math

import matplotlib.pyplot as plt

import numpy as np

import sympy as sym


#a)

tempo = 1
dt = 0.001
N = int(tempo/dt)
g = 9.8
t = np.linspace(0,1,1000)

m = 0.057                   #Massa do objeto
ax = np.empty(N)            #Criar vetores
ay = np.empty(N)
vx = np.empty(N)            
vy = np.empty(N)
x = np.empty(N)
y = np.empty(N)
Em = np.empty(N)
v = np.empty(N)

vk = (100 * 1000)/3600      #Velocidade inicial em km/h

vt = vk                     #Neste caso pois a velocidade terminal é igual á velocidade inicial

vx[0] = vk * np.cos(np.deg2rad(10))     #Velocidade do eixo dos x (se o angulo for de 10º com a horizontal)
vy[0] = vk * np.sin(np.deg2rad(10))     #Velocidade do eixo dos y (se o angulo for de 10º com a horizontal)
x[0] = 0
y[0] = 0

for i in range(N-1):
    dres=g/vt**2                        #Fórmula da Resistência
    v[i] = np.sqrt(vx[i]**2+vy[i]**2)   #Fórmula para a velocidade
    ax[i]=-dres*v[i]*vx[i]              #Acelaração em x
    ay[i]=-g-dres*v[i]*vy[i]            #Acelaração em y
    vx[i+1] = vx[i] + ax[i] * dt        #Velocidade em x
    vy[i+1] = vy[i] + ay[i] * dt        #Velocidade em y
    x[i+1] = x[i] + vx[i] * dt          #Posição x
    y[i+1] = y[i] + vy[i] * dt          #Posição y
    Em[i] = m*g*y[i] + 0.5 * m * v[i]**2    #Fórmula Energia Mecanica
    if (t[i]<0.4 and t[i+1]>0.4):           #Encontrar a energia mecanica em t=0.4s 
        stringPrint = str(t[i])+" "+str(Em[i])
        print(stringPrint)     #---> (segundos, Em)
    if (t[i]<0.8 and t[i+1]>0.8):           #Encontrar a energia mecanica em t=0.8s
        stringPrint = str(t[i])+" "+str(Em[i])
        print(stringPrint)     #---> (segundos, Em)


Em[-1] =  m*g*y[-1] + 0.5 * m * v[-1]**2 #Dar valor ao último valor da lista
plt.grid()
plt.xlabel("Tempo")
plt.ylabel("Em")
plt.plot(t,Em)
plt.show()