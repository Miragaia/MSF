import numpy as np
import matplotlib.pyplot as plt
import math

def graph(x,y,title = "Gráfico", xaxis = "Eixo X", yaxis = "Eixo Y"):
    plt.plot(x,y,'o')

    plt.xlabel(xaxis)
    plt.ylabel(yaxis)

    plt.grid()

    plt.title(title)

# máximo pelo polinómio de Lagrange
def maximo(xm1,xm2,xm3,ym1,ym2,ym3): 
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

# raiz pelo polinómio de Lagrange
def zerosv(xm1,xm2,xm3,ym1,ym2,ym3):  
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

x0 = 0
y0 = 0

v0x = 0.5 #v inicial
v0y = 0

g = 9.80 
P = 0.48*745.7 #manter *745.7 se for cv se for W apagar
m = 12
miu = 0.01
Cres = 0.9
A = 0.50
dAr = 1.225

## Passo temporal para o Método de Euler
dt = 0.001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 200 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

## NOTA: Vx é constante s/ resistência do ar (igual a Vx0)
t = np.zeros(N+1)

ax = np.zeros(N+1)
ay = np.zeros(N+1)

vx = np.zeros(N+1)
vy = np.zeros(N+1)
vv = np.zeros(N+1)

x = np.zeros(N+1)
y = np.zeros(N+1)

vx[0] = v0x
vy[0] = v0y


x[0] = x0
y[0] = y0

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    vv[i] = math.sqrt(vx[i]**2 + vy[i]**2)

    ay[i] = 0
    ax[i] = P/(m*vv[i]) - (0.5*Cres*A*dAr*(vv[i]**2))/m - miu*g

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt

    x[i+1] = x[i] + vx[i]*dt
    y[i+1] = y[i] + vy[i]*dt

## Gráfico Velocidade * Tempo
graph(t,vv, "Velocidade * Tempo", "Tempo (s)", "Velocidade (m/s)")
plt.show()


## Cálculo da velocidade terminal: Usar um instante de tempo em que v seja vt, conforme visualizado no gráfico anterior
for i in range(N):
    if t[i+1] > 120-dt and  t[i+1] < 120+dt:
        vt = vx[i+1]
        print('A velocidade terminal é de {:.2f} m/s.'.format(vt))
        break

## Alínea b)
Vtarget = 0.9*vt

for i in range(N):
    if vv[i+1] > Vtarget-dt and  vv[i+1] < Vtarget+dt:
        print('O ciclista demora {:.2f}s até atingir 0.9 da velocidade terminal.'.format(t[i+1]))
        break

## Alínea c)
for i in range(N):
    if x[i+1] > 2000-2*dt and  x[i+1] < 2000+2*dt:
        print('O ciclista demora {:.2f}s até percorrer 2km.'.format(t[i+1]))
        break





