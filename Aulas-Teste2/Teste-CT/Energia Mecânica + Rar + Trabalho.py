import numpy as np
import matplotlib.pyplot as plt

#Funções
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

dt = 0.001
tf = 5.00
n=int(tf/dt+0.1)
t=np.linspace(0,tf,n+1)

g = 9.8
x0 = 0
y0 = 0


vx0 = (100/3.6)*np.cos(np.radians(10)) 
vy0 = (100/3.6)*np.sin(np.radians(10))


vt = 100/3.6 #velocidade terminal 
vel0= 100/3.6
w = [0, 0, 0]
densAr = 1.225
r = 67/2/1000
m = 0.057

#vetores das posições
x = np.zeros(n+1)
y = np.zeros(n+1)

#vetores velocidades
vel=np.empty(n+1)
vx = np.zeros(n+1)
vy = np.zeros(n+1)

#vetores da aceleraçao
ax = np.zeros(n+1)
ay = np.zeros(n+1)

aresx = np.zeros(n+1)
aresy = np.zeros(n+1)


#vetores da energia, força de magnus 
EnergiaMec = np.zeros(n+1)
f = np.zeros(n+1)
int_trab_res=np.empty(n+1)

#definir as primeiras posiçoes ou velocidades dos vetores 
x[0] = x0
y[0] = y0
vx[0] = vx0
vy[0] = vy0

D=g/vt**2 #RESISTENCIA DO aR
#Método de Euler
for i in range(0,n):
    
     vel=np.sqrt(vx[i]**2+vy[i]**2)

     aresx[i]=-D*vel*vx[i]
     ax[i]=aresx[i]
     aresy[i]=-D*vel*vy[i]
     ay[i]=aresy[i]-g
     vx[i+1]=vx[i]+ax[i]*dt
     vy[i+1]=vy[i]+ay[i]*dt
     
     x[i+1]=x[i]+vx[i]*dt
     y[i+1]=y[i]+vy[i]*dt
     EnergiaMec[i]=0.5*m*vel**2+m*g*y[i]
     #pede o trabalho da força resistiva, logo so interessa essa parte da aceleração
     # W=integral(F dx)+integral(F dy)
     # dx é dado por vx*dt e dy=vy*dt
     #Assim: INTEGRACAO   W=Integral(  Fx vx + Fy * vy) dt
     #Força segundo X: segunda lei de Newton Fx=m*ax e Fy=m*ay (apenas as resistivas)

     f[i]=m*aresx[i]*vx[i]+m*aresy[i]*vy[i]
     int_trab_res[i]=dt*((f[0]+f[n])*0.5+np.sum(f[1:n-1])) #INTEGRACAO

     if (t[i]<0.4 and t[i+1]>0.4):
         stringPrint=str(t[i])+" "+str(w[i])
         print (stringPrint)
     if (t[i]<0.8 and t[i+1]>0.8):
         stringPrint=str(t[i])+" "+str(w[i])
         print (stringPrint)


#calcular o ultimo valor da energia:
vv=np.sqrt(vx[i+1]**2+vy[i+1]**2)
EnergiaMec[i+1]=0.5*m*vt**2+m*g*y[i+1]

#Calcular o ultimo valor do trabalho:
f[i+1]=m*aresx[i+1]*vx[i+1]+m*aresy[i+1]*vy[i+1]
int_trab_res[i+1]=dt*((f[0]+f[n])*0.5+np.sum(f[1:n-1]))

plt.figure()
plt.plot(t,int_trab_res,label='W Res')
plt.ylabel('W_Res (J)')
plt.xlabel( 't (s)' )
plt.grid()

print(EnergiaMec[0])
print(EnergiaMec[int(0.4/dt)])
print(EnergiaMec[int(0.8/dt)])


print(int_trab_res[0])
print(int_trab_res[int(0.4/dt)])
print(int_trab_res[int(0.8/dt)])


