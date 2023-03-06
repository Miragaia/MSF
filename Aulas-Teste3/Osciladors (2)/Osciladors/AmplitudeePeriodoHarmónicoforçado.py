#Um corpo de massa 1 kg move-se num oscilador harmónico forçado. Se a posição de
#equilíbrio for a origem do eixo 𝑥𝑒𝑞 = 0 m, o oscilador harmónico tem a energia potencial
#𝐸𝑝 =1/2*𝑘*𝑥**2
#e exerce no corpo a força 𝐹𝑥= −𝑘 𝑥
#O oscilador é amortecido pela força −𝑏V𝑥 e sujeito à força externa 𝐹0 cos(wft) . 
# Considere 𝑘 =1 N/m, 𝑏 = 0.05 kg/s, 𝐹0 = 7.5 N e 𝜔𝑓 = 1.0 rad/s.
#b) Calcule a amplitude do movimento e o seu período no regime estacionário, usando os
#resultados numéricos.

import numpy as np
import matplotlib.pyplot as plt

#max e min

def maximo(xm1,xm2,xm3,ym1,ym2,ym3):  # máximo pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
    xmax=0.5*xmla/(a+b+c)

    xta=xmax-xm1
    xtb=xmax-xm2
    xtc=xmax-xm3

    ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xmax, ymax

def zerosv(xm1,xm2,xm3,ym1,ym2,ym3):  # raiz pelo polinómio de Lagrange
    xab=xm1-xm2
    xac=xm1-xm3
    xbc=xm2-xm3

    a=ym1/(xab*xac)
    b=-ym2/(xab*xbc)
    c=ym3/(xac*xbc)

    am=a+b+c
    bm=a*(xm2+xm3)+b*(xm1+xm3)+c*(xm1+xm2)
    cm=a*xm2*xm3+b*xm1*xm3+c*xm1*xm2

    xzero=(bm+np.sqrt(bm*bm-4*am*cm))/(2*am)
    if xm3 > xm1 and (xzero < xm1 or xzero > xm3): 
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)


    if xm1 > xm3 and (xzero < xm3 or xzero > xm1):
        xzero=(bm-np.sqrt(bm*bm-4*am*cm))/(2*am)

    xta=xzero-xm1
    xtb=xzero-xm2
    xtc=xzero-xm3
    yzero=a*xtb*xtc+b*xta*xtc+c*xta*xtb
    return xzero, yzero

#b)

dt=0.0001
tf=300
n=int(tf/dt+0.1)

t=np.linspace(0,tf,n)

xi = 4      #Dados do problema
vi = 0
k = 1
m = 1
xeq = 0
b = 0.05
f0 = 7.5
wf = 1

v = np.empty(n)     #Criar vetores
x = np.empty(n)
a = np.empty(n)
maximos = []
difTempos = []

v[0] = vi   #Inicializar vetores
x[0] = xi

for i in range(n-1):
    a[i] = (-k/m)*x[i] - (b/m)*v[i] + (f0/m)*np.cos(wf*t[i])    #Acelaração
    v[i+1] = v[i] + a[i] * dt   #Velocidade
    x[i+1] = x[i] + v[i+1]*dt   #Posição

    if i>1 and x[i-1] < x[i] and  x[i+1] < x[i] and t[i]>200:   #Fica estacionário apartir do segundo 200 +/- neste caso
        maxt, maxx = maximo(t[i-1],t[i],t[i+1],x[i-1],x[i],x[i+1])  #Tirar máximos
        maximos.append(maxx)
        difTempos.append(maxt)

Amplitude = sum(maximos)/len(maximos)   #Media dos máximos
print("Amplitude:", Amplitude)

sumTempos = difTempos[-1] - difTempos[0]

Período = sumTempos/(len(difTempos)-1)
print("Período: ", Período)