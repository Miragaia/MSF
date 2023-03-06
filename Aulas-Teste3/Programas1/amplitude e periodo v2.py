# Oscilador de Harmónico Forçado
# Método de Euler-Cromer

import numpy as np
import matplotlib.pyplot as plt



# def maximo(xm1,xm2,xm3,ym1,ym2,ym3):
#     xab=xm1-xm2
#     xac=xm1-xm3
#     xbc=xm2-xm3

#     a=ym1/(xab*xac)
#     b=-ym2/(xab*xbc)
#     c=ym3/(xac*xbc)

#     xmla=(b+c)*xm1+(a+c)*xm2+(a+b)*xm3
#     xmax=0.5*xmla/(a+b+c)

#     xta=xmax-xm1
#     xtb=xmax-xm2
#     xtc=xmax-xm3

#     ymax=a*xtb*xtc+b*xta*xtc+c*xta*xtb
#     return xmax, ymax



dt=0.001
tf=400.0
n=np.int(tf/dt+0.1)
print('n',n)

tempo=np.empty(n+1)
x=np.empty(n+1)
vx=np.empty(n+1)
a=np.empty(n+1)
enec=np.empty(n+1)
	  
t0=0.
x0=4.0            
vx0=0.0

tempo[0]=t0
vx[0]=vx0
x[0]=x0

k=1
m=1
b=0.05
F0=7.5
Wf=1
W0 = np.sqrt(k/m)
ampl=0
countMax=0
tMax=[]
periodo=[]

for i in range(n):
	tempo[i+1]=tempo[i]+dt
	a[i]=-(k/m)*x[i]-(b/m)*vx[i]+(F0/m)*np.cos(Wf*tempo[i])
	vx[i+1]=vx[i]+a[i]*dt
	x[i+1]=x[i]+vx[i+1]*dt
	if tempo[i]>200 and x[i-1] < x[i] >  x[i+1] :
		#maxx, maxy=maximo(tempo[i-1], tempo[i], tempo[i+1], x[i-1], x[i], x[i+1])
		maxy=x[i]
		ampl=ampl+maxy
		countMax=countMax+1
		tMax.append(tempo[i])
		


amplAverage=ampl/countMax

sumTempos=0
countMaximos=len(tMax)
#calculo do periodo

#Periodo=(tMax[-1]-tMax[0])/(countMax-1)   #tMax[-1] é o ultimo indice de tMax

for j in range(0,countMaximos-1):
	sumTempos+=tMax[j+1]-tMax[j]

Periodo=sumTempos/(countMaximos-1) #Faz a media



amp_teo = (F0/m)/np.sqrt((Wf**2-W0)**2+(b*Wf/m)**2)
print('Amplitude ',amplAverage)
print('Amplitude_teo ',amp_teo)
print('Periodo ',Periodo)

	




plt.title('Oscilador Harmónico Forçado Met Euler-Cromer')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid()    
plt.plot(tempo,x)
plt.show()
