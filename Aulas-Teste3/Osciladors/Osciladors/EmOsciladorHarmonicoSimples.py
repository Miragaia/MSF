#Uma mola exerce uma força Fx=-kx(t) , em que k é a constante elástica da mola, num corpo de massa m.
#Considere k = 1 N/m e m = 1 kg.
#c) Calcule a energia mecânica. É constante ao longo do tempo?

import numpy as np
import matplotlib.pyplot as plt

dt=0.1
tf=100.00
n=int(tf/dt+0.1)

t=np.linspace(0,tf,n)

vi = 0          #Velocidade Inicial
xi = 4          #Posição Inicial
k = 1           #Constante élastica
m = 1           #Massa

v = np.empty(n) #Criar Vetores
x = np.empty(n)
a = np.empty(n)
Em = np.empty(n)

v[0] = vi       #Inicializar vetores
x[0] = xi

w = np.sqrt(k/m)    #Frequência angular

for i in range(n-1):
    a[i] = -(w**2)*x[i]             #w**2 = k Acelaração
    v[i+1] = v[i] + a[i] * dt       #Velocidade
    x[i+1] = x[i] + v[i+1]*dt       #Posição
    Em[i] = (0.5*k*(x[i]**2)) + (0.5*m*(v[i]**2))   #Energia mecanica

Em[-1] = (0.5*k*(x[-1]**2)) + (0.5*m*(v[-1]**2)) #Prencher último espaço do vetor

plt.figure()
plt.ylim(0,10)
plt.plot(t,Em,label='Ex 7')
plt.ylabel('Energia')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()