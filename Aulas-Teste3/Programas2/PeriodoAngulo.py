import numpy as np
import matplotlib.pyplot as plt
import math


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
    
dt=0.001
tf=20.00
n=np.int(tf/dt+0.1)

t=np.linspace(0,tf,n)

teta=np.empty(n);
omega=np.empty(n);
acelAngular=np.empty(n);


teta0graus=30 #1 



teta0=math.radians(teta0graus)
omega0=0
teta[0]=teta0
omega[0]=omega0

L=1
g=9.8


countMaximos=0
maxTotal=0
difTempos=[]
maximos=[]


for i in range (0,n-1):
	acelAngular[i]=-(g/L)*math.sin(teta[i]);
	omega[i+1]=omega[i]+acelAngular[i]*dt
	teta[i+1]=teta[i]+omega[i+1]*dt #euler-cromer
	
	if i>1 and teta[i-1] < teta[i] and  teta[i+1] < teta[i]  :    # para máximo
        # print('sucess',i, y[i-1], y[i], y[i+1])
		maxt, maxx=maximo(t[i-1], t[i], t[i+1], teta[i-1], teta[i], teta[i+1])
		maximos.append(maxx)
		difTempos.append(maxt)

print(math.sin(math.radians(90)))
countMaximos=len(maximos)		
Amplitude=sum(maximos)/countMaximos #media
print("Amplitude: ",Amplitude)

sumTempos=0

# #calculo do periodo
for j in range(0,countMaximos-1):
	sumTempos+=difTempos[j+1]-difTempos[j]

Periodo=sumTempos/(countMaximos-1) #Faz a media

print("Periodo: ",Periodo)
print("Periodo Analitico para pequenas oscilações: ",2*math.pi*math.sqrt(L/g))


plt.figure()
plt.plot(t,np.degrees(teta))
# plt.plot(t,energia,label='W Res')
plt.ylabel('$\Theta$(º)')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()