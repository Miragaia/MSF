import numpy as np
import matplotlib.pyplot as plt

def max_numen(x0, x1, x2, y0, y1, y2):
    qo1 = (x0-x1)*(x0-x2)   
    qo2 = (x1-x0)*(x1-x2)
    qo3 = (x2-x0)*(x2-x1)
    a_0 = y0/ qo1
    b_0 = y1/ qo2    
    c_0 = y2/ qo3
    
    a = ((x2+x1)*y0)/qo1
    b = ((x2+x0)*y1)/qo2
    c = ((x0+x1)*y2)/qo3
    
    xmax = (a_0+b_0+c_0)/(a+b+c)*0.5
    
    xta=xmax-x0
    xtb=xmax-x1
    xtc=xmax-x2

    ymax=a_0*xtb*xtc+b_0*xta*xtc+c_0*xta*xtb
    return xmax, ymax

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
tf=40.00
n=np.int(tf/dt+0.1)

t=np.linspace(0,tf,n)

print(n)

x=np.empty(n);
v=np.empty(n);
ep=np.empty(n);
et=np.empty(n);


k=1.8
m=0.5
w2=k/m
Xeq=0

#condicoes iniciais
ep0=3 #Energia total menor que 4 

x0=2.5#np.sqrt(Xeq**2+np.sqrt(ep0*2/k))
v0=3.0
x[0]=x0
v[0]=v0



for i in range (0,n-1):
	a=-2*w2*(x[i]**2-Xeq**2)*x[i]
	v[i+1]=v[i]+a*dt
	x[i+1]=x[i]+v[i+1]*dt #euler-cromer
	if ep[i]<4:
		ep[i]=0.5*k*(x[i]**2-Xeq**2)**2 #energia potencial
	et[i]=ep[i]+0.5*m*v[i]**2 #energia total
	
    
#print(np.diff(t[np.round(ep,4)== 0]))
#print(t[np.round(ep,5)== 0])
#ultimo ponto
ep[n-1]=0.5*k*(x[n-1]**2-Xeq**2)**2
et[n-1]=ep[n-1]+0.5*m*v[n-1]**2
# print(ep[n-1])
print(et[n-1])
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
#plt.ylim(0,10)
plt.grid()
plt.show()

plt.figure()
plt.plot(t,x)
plt.ylabel('x (m)')
plt.xlabel( 't (s)' )
# plt.ylim(0,10)
plt.grid()
plt.show()
