# Volante de badmington - velocidade
# Método de Runge Kutta 4ª ordem

import numpy as np
import matplotlib.pyplot as plt

def acelera(t,x,vx):  
    ax=g-g/vt**2*np.abs(vx)*vx 
    return ax

def rk4(t,x,vx,dt):
    # Modificado
    ax1=acelera(t,x,vx)
    c1v=ax1*dt
    c1x=vx*dt
    ax2=acelera(t+dt/2.,x+c1x/2.,vx+c1v/2.)
    c2v=ax2*dt
    c2x=(vx+c1v/2.)*dt			# predicto:  vx(t+dt) * dt
    ax3=acelera(t+dt/2.,x+c2x/2.,vx+c2v/2.)
    c3v=ax3*dt
    c3x=(vx+c2v/2.)*dt
    ax4=acelera(t+dt,x+c3x,vx+c3v)
    c4v=ax4*dt
    c4x=(vx+c3v)*dt      
    xp=x+(c1x+2.*c2x+2.*c3x+c4x)/6.
    vxp=vx+(c1v+2.*c2v+2.*c3v+c4v)/6.
    return xp,vxp

dt=0.5  
tf=2.0   ##Velocidade que "objeto" atinge x segundos após ( ###mudar o valor pelo x)
n=np.int(tf/dt+0.1)
print('dt:',dt, "n:",n)

tempo=np.zeros(n+1)
xrk4=np.zeros(n+1)
vxrk4=np.zeros(n+1)
vxe=np.zeros(n+1)

g=9.80
vt=6.80   ##Velocidade terminal do "objeto" ###mudarr
	  
t0=0.
x0=3.               
vx0=0.    ###Velocidade Inicial (se largado igual a 0) ###mudar
print('t,x,vx = ',t0,x0,vx0)
tempo[0]=t0
vxrk4[0]=vx0
xrk4[0]=x0
tem=t0
xet=x0
vxet=vx0
print('tem,xet,vxet = ',t0,x0,vx0) 
for i in range(n):
    xet,vxet=rk4(tem,xet,vxet,dt)
    tem=tem+dt
    tempo[i+1]=tem
    vxrk4[i+1]=vxet
    xrk4[i+1]=xet      
    vxe[i+1]=vxe[i]+(g-g/vt**2*np.abs(vxe[i])*vxe[i])*dt   # Metodo de Euler
    
te=np.linspace(t0,tf,100)
ve=vt*np.tanh(g*te/vt)
tet=2
vet=vt*np.tanh(g*tet/vt)
print('t=',tet, 's')
print('v=',vet, 'm/s')

plt.grid()    
plt.plot(tempo,vxrk4, label="Runge-Kutta")
plt.plot(te,ve, label = "Teórico")
plt.plot(tempo,vxe, label="Euler")
plt.xlabel("tempo(s)")
plt.ylabel("velocidade(m/s)")
plt.legend()
plt.show()


###objetivo é calcular velocidade num certo instante-->