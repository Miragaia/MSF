import numpy as np
import math
import matplotlib.pyplot as plt

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


dt=0.001
tf=40.00
n=np.int(tf/dt+0.1)

t=np.linspace(0,tf,n)

print(n)

x=np.empty(n);
v=np.empty(n);
ep=np.empty(n);
et=np.empty(n);


k=1
m=1
w2=k/m
Xeq=1.5

#condicoes iniciais
ep0=0.75#Et-- 

x0=np.sqrt(Xeq**2+np.sqrt(ep0*2/k))
v0=0
x[0]=x0
v[0]=v0


countMaximos=0
maxTotal=0
difTempos=[]
maximos=[]

for i in range (0,n-1):
    a=-2*w2*(x[i]**2-Xeq**2)*x[i]
    v[i+1]=v[i]+a*dt
    x[i+1]=x[i]+v[i+1]*dt #euler-cromer
    ep[i]=0.5*k*(x[i]**2-Xeq**2)**2
    et[i]=ep[i]+0.5*m*v[i]**2
    
    if i>1 and x[i-1] < x[i] and  x[i+1] < x[i]  :    # para máximo
        # print('sucess',i, y[i-1], y[i], y[i+1])
        maxt, maxx=maximo(t[i-1], t[i], t[i+1], x[i-1], x[i], x[i+1])
        maximos.append(maxx)
        difTempos.append(maxt)

# print(math.sin(math.radians(90)))
countMaximos=len(maximos)
Amplitude=sum(maximos)/countMaximos #media
print("Amplitude: ",Amplitude)

sumTempos=0

# #calculo do periodo
for j in range(0,countMaximos-1):
	sumTempos+=difTempos[j+1]-difTempos[j]

Periodo=sumTempos/(countMaximos-1) #Faz a media

print("Periodo: ",Periodo, "s")
print("Frequência: ",1/Periodo, "hz")


    
# print(np.diff(t[np.round(ep,4)== 0]))
# print(t[np.round(ep,5)== 0])
#ultimo ponto
ep[n-1]=0.5*k*(x[n-1]**2-Xeq**2)**2
et[n-1]=ep[n-1]+0.5*m*v[n-1]**2

plt.figure()
plt.plot(x,ep)
plt.ylabel('Energia Potencial (J)')
plt.xlabel( 'x (m)' )
plt.grid()

plt.show()

plt.figure()
plt.plot(x,et)
plt.ylabel('Energia Total (J)')
plt.xlabel( 'x (m)' )
# plt.ylim(0,10)
plt.grid()
plt.show()

plt.figure()
plt.plot(t,x)
plt.ylabel('x (m)')
plt.xlabel( 't (s)' )
# plt.ylim(0,10)
plt.grid()
plt.show()