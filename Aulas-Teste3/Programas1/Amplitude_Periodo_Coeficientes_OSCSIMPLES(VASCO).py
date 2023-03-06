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

def abfourier(tp,xp,it0,it1,nf):
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( x cos nw) dt entre it0 e tt1
    # integracao numerica pelo aproximação trapezoidal
# input: matrizes tempo tp  
#        posição xp 
#        indices inicial it0
#        final   it1  (ao fim de um período)   
#        nf índice de Fourier
# output: af_bf e bf_nf  
    
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1-1]*np.sin(nf*ome*tp[it1-1])
    qt=xp[it0+1:it1-1]*np.sin(nf*ome*tp[it0+1:it1-1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

x0 = 4
v0 = 0

k = 1
m = 1

## Passo temporal para o Método de Euler
dt = 0.001 ##passo temporal
t0 = 0.00 ##tempo inicial
tf = 15.00 ##tempo final
N = np.int((tf-t0)/dt) ##Nº de passos a realizar
print("Número de passos: ", N)

## Criação de arrays de velocidade, posição e tempo com N lugares, para os N passos,
#  preenchidos por 0's. Caso a velocidade ou posição inicial seja diferente de 0, temos que fazer a correção.

## NOTA: Vx é constante s/ resistência do ar (igual a Vx0)
t = np.zeros(N+1)

ax = np.zeros(N+1)
vx = np.zeros(N+1)
x = np.zeros(N+1)

Em = np.zeros(N+1)

vx[0] = v0
x[0] = x0

## Ciclo que implementa o Método de Euler, e atualiza o array tempo para podemos fazer um plot
for i in range(N):
    t[i+1] = t[i] + dt

    ax[i] = -x[i]

    vx[i+1] = vx[i] + ax[i]*dt

    x[i+1] = x[i] + vx[i+1]*dt

    Em[i] = 0.5*m*vx[i]**2 + 0.5*k*x[i]**2

graph(t,x,"Força Elástica", "Tempo (s)", "Posição (m)")

## Cálculo dos máximos com recurso ao Polinómio de Lagrange. Permite calcular amplitude e mais tarde T
maxGraficos = []

for i in range(N):
    if x[i-1] < x[i] and  x[i+1] < x[i]:
        print('Success')
        maxt, maxx = maximo(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        if len(maxGraficos) == 0:
            print("A amplitude do movimento é {:.2f}m.".format(maxx))
        maxGraficos.append((maxt,maxx))

## Cálculo do período T
T = []
tAnt = 0
tNovo = 0
i = 0

for (tmax,max) in maxGraficos:
    i += 1
    if i > 1:
        T.append(abs(tmax-tNovo))
        tNovo, tAnt = tmax, tNovo
    else:
        tNovo, tAnt = tmax, tNovo

periodo = sum(T)/len(T)
print("O período do movimento é {:.3f}.".format(periodo))
plt.show()

## Gráfico da Energia Mecânica
graph(t,Em,"Energia Mecânica","t(s)","Em(J)")
plt.show()


## Determinação dos Coeficientes de Fourier
## Os valores it0 e it1 usados na função abfourier como parâmetros de entrada devem cobrir
## o valor de um periodo inteiro. Assim, deve ser usado um valor maior do que o da conta que está em baixo
print(periodo/dt)

a = np.zeros(20)
b = np.zeros(20)
n = np.zeros(20)

for i in range(20):
    n[i] = i
    a[i],b[i] = abfourier(t,x,0,6315,i)
    
plt.subplot(1,2,1)
graph(n,a,"Coeficiente de Fourier - an","an","n")
plt.subplot(1,2,2)
graph(n,b,"Coeficiente de Fourier - bn","bn","n")
plt.show()

a,b = abfourier(t,x,0,6315,1)

print("Os coeficientes de Fourier são, aproximadamente, a = {:.2f}, b = {:.2f}.".format(abs(a),abs(b)))