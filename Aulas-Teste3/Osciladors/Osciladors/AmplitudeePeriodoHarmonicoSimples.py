#Uma mola exerce uma força Fx=-kx(t) , em que k é a constante elástica da mola, num corpo de massa m.
#Considere k = 1 N/m e m = 1 kg.
#b)Calcule a amplitude do movimento e o seu período, usando os resultados numéricos.

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
maximos = []
difTempos = []

v[0] = vi       #Inicializar vetores
x[0] = xi

w = np.sqrt(k/m)    #Frequência angular

for i in range(n-1):
    a[i] = -(w**2)*x[i]             #w**2 = k Acelaração
    v[i+1] = v[i] + a[i] * dt       #Velocidade
    x[i+1] = x[i] + v[i+1]*dt       #Posição

    if i>1 and x[i-1] < x[i] and  x[i+1] < x[i]:
        maxt, maxx = maximo(t[i-1],t[i],t[i+1],x[i-1],x[i],x[i+1])  #Retirar máximos
        maximos.append(maxx)
        difTempos.append(maxt)

Amplitude = sum(maximos)/len(maximos)   #Media dos máximos
print("Amplitude:", Amplitude)          

sumTempos = 0                           #Calcular o Período
for j in range(0, len(difTempos)-1):
    sumTempos += difTempos[j+1] - difTempos[j]

Período = sumTempos/(len(difTempos)-1)
print("Período: ", Período)