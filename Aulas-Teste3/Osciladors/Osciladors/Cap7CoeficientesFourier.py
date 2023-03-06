#Um corpo de massa 1 kg move-se num oscilador harmónico forçado. Se a posição de
#equilíbrio for a origem do eixo 𝑥𝑒𝑞 = 0 m, o oscilador harmónico tem a energia potencial
#𝐸𝑝 =1/2*𝑘*𝑥**2
#e exerce no corpo a força 𝐹𝑥= −𝑘 𝑥
#O oscilador é amortecido pela força −𝑏V𝑥 e sujeito à força externa 𝐹0 cos(wft) . 
# Considere 𝑘 =1 N/m, 𝑏 = 0.05 kg/s, 𝐹0 = 7.5 N e 𝜔𝑓 = 1.0 rad/s.
#f) Calcule os coeficientes de Fourier do movimento do regime estacionário nas condições das
#alíneas a) e c). Que conclusões retira da lei do movimento do regime estacionário?

import numpy as np
import matplotlib.pyplot as plt

def abfourier(tp,xp,it0,it1,nf):
#
# cálculo dos coeficientes de Fourier a_nf e b_nf
#       a_nf = 2/T integral ( xp cos( nf w) ) dt   entre tp(it0) e tp(it1)
#       b_nf = 2/T integral ( xp sin( nf w) ) dt   entre tp(it0) e tp(it1)    
# integracao numerica pela aproximação trapezoidal
# input: matrizes tempo tp   (abcissas)
#                 posição xp (ordenadas) 
#       indices inicial it0
#               final   it1  (ao fim de um período)   
#       nf índice de Fourier
# output: af_bf e bf_nf  
# 
    dt=tp[1]-tp[0]
    per=tp[it1]-tp[it0]
    ome=2*np.pi/per

    s1=xp[it0]*np.cos(nf*ome*tp[it0])
    s2=xp[it1]*np.cos(nf*ome*tp[it1])
    st=xp[it0+1:it1]*np.cos(nf*ome*tp[it0+1:it1])
    soma=np.sum(st)
    
    q1=xp[it0]*np.sin(nf*ome*tp[it0])
    q2=xp[it1]*np.sin(nf*ome*tp[it1])
    qt=xp[it0+1:it1]*np.sin(nf*ome*tp[it0+1:it1])
    somq=np.sum(qt)
    
    intega=((s1+s2)/2+soma)*dt
    af=2/per*intega
    integq=((q1+q2)/2+somq)*dt
    bf=2/per*integq
    return af,bf

#a)

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

v = np.empty(n)     #Criar vetores
x = np.empty(n)
a = np.empty(n)

ind=np.transpose([0 for n in range(1000)])      #Para coeficientes de Fourier
countMax = 0
afo = np.empty(15)
bfo = np.empty(15)

v[0] = vi           #Inicializar os vetores
x[0] = xi

for i in range(n-1):
    a[i] = (-k/m)*x[i] - (b/m)*v[i] + (f0/m)*np.cos(wf*t[i])    #Acelaração
    v[i+1] = v[i] + a[i] * dt   #Velocidade
    x[i+1] = x[i] + v[i+1]*dt   #Posição
    if i>1 and x[i-1] < x[i] and  x[i+1] < x[i] and t[i]>200:   #Fica estacionário apartir do segundo 200 +/- neste caso
        countMax +=1
        ind[countMax] = int(i)

#Tirar e mostrar coeficientes de Fourier

t0 = ind[countMax-1]
t1 = ind[countMax]
for i in range(15):
    af, bf=abfourier(t,x,t0,t1,i)
    afo[i] = af
    bfo[i] = bf

ii = np.linspace(0,14,15)    
plt.figure()
plt.ylabel("| a_n |")
plt.xlabel('n')
plt.bar(ii,np.abs(afo))
plt.grid()
plt.show() 

plt.figure()
plt.ylabel("| b_n |")
plt.xlabel('n')
plt.bar(ii,np.abs(bfo))
plt.grid()
plt.show() 