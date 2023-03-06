#Um corpo de massa 1 kg move-se num oscilador harmónico forçado. Se a posição de
#equilíbrio for a origem do eixo 𝑥𝑒𝑞 = 0 m, o oscilador harmónico tem a energia potencial
#𝐸𝑝 =1/2*𝑘*𝑥**2
#e exerce no corpo a força 𝐹𝑥= −𝑘 𝑥
#O oscilador é amortecido pela força −𝑏V𝑥 e sujeito à força externa 𝐹0 cos(wft) . 
# Considere 𝑘 =1 N/m, 𝑏 = 0.05 kg/s, 𝐹0 = 7.5 N e 𝜔𝑓 = 1.0 rad/s.
#e) Calcule a energia mecânica. É constante ao longo do tempo?

import numpy as np
import matplotlib.pyplot as plt


dt=0.0001
tf=300
n=int(tf/dt+0.1)

t=np.linspace(0,tf,n)

xi = 4          #Dados do problema
vi = 0
k = 1
m = 1
xeq = 0
b = 0.05
f0 = 7.5
wf = 1

v = np.empty(n)     #Criar Vetores
x = np.empty(n)
a = np.empty(n)
Em = np.empty(n)

v[0] = vi       #Inicializar vetores
x[0] = xi

for i in range(n-1):
    a[i] = (-k/m)*x[i] - (b/m)*v[i] + (f0/m)*np.cos(wf*t[i])    #Acelaração
    v[i+1] = v[i] + a[i] * dt   #Velocidade
    x[i+1] = x[i] + v[i+1]*dt   #Posição
    Em[i] = (0.5*k*(x[i]**2)) + (0.5*m*(v[i]**2))     #Energia Mecanica

Em[-1] = (0.5*k*(x[-1]**2)) + (0.5*m*(v[-1]**2))        #Completar vetor
plt.figure()
plt.plot(t,Em,label='Ex 7')
plt.ylabel('Energia')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()