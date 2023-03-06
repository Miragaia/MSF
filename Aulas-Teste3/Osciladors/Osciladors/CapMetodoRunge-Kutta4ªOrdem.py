#Implemente o método de Runge-Kutta de 4ª ordem para calcular a velocidade com que um
#volante de badmington atinge 2 s depois de ser largado. A velocidade terminal do volante é de
#6.80 m/s, e a aceleração é
#𝑎𝑦(t)=g-g/(vT**2)*|vy|*vy
#Compare o valor obtido com o valor exato, de acordo com a lei 𝑣𝑦 𝑡 = 𝑣𝑇*tanh(𝑔*𝑡/𝑣𝑇)

import numpy as np
import matplotlib.pyplot as plt

###################################################

def acelera(t,y,vy):            #Função da acelaração necessária para a função do método de Runge-Katta
    g = 9.8
    vt = 6.8
    ay = g - (g/(vt**2))*np.abs(vy)*vy
    return ay

def euler(pos, vel, ace, step):
    nextvel = vel + ace * step
    nextpos = pos + vel * step
    return nextpos, nextvel

def rk4(t,x,vx,acelera,dt):
    """
    Integração numérica de equação diferencial de 2ª ordem respeitante ao movimento
    acelera=dvx/dt=Força(t,x,vx)/massa      com vx=dx/dt   (acelera é uma função)
    input:  t = instante de tempo
            x(t) = posição
            vx(t) = velocidade
            dt = passo temporal 
    output: x(t+dt),vx(t+dt)
    """
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

###################################################

dt = 0.1
tf = 2
n=int(tf/dt+0.1)

t=np.linspace(0,tf,n)

y_rk4 = np.empty(n)     #Criar vetores
vy_rk4 = np.empty(n)
y_euler = np.empty(n)
v_euler = np.empty(n)

g = 9.8
vt = 6.8                    #Dados do problema

t0 = 0
y0 = 3
vy0 = 0

v_euler[0] = vy0        #Inicializar
y_euler[0] = y0
vy_rk4[0] = vy0
y_rk4[0] = y0
tem = t0
xet = y0
vye = vy0

for i in range(n-1):
    a_euler = acelera(0, 0, v_euler[i])
    y_euler[i+1], v_euler[i+1] = euler(y_euler[i], v_euler[i], a_euler, dt)

    ## ou y_rk4[i+1],vy_rk4[i+1] = (t[i],y_rk4[i],vy_rk4[i],acelera,dt)
    xet,vye=rk4(t[i],xet,vye,acelera,dt)        #Método de Runge-Kutta
    vy_rk4[i+1] = vye
    y_rk4[i+1] = xet

v_ana = vt*np.tanh((g*t)/vt)                #Velocidade analitica do problema 

#xet,vye=rk4(t[i],xet,vye,acelera,dt)    Para dar igual ás soluções pois eu fiz com n e n-1
#vy_rk4[i+1] = vye                       enquanto que o professor fez com n+1 e n
#y_rk4[i+1] = xet

print("Velocidade apartir do método de Runge-Kutta de 4ª ordem é",vy_rk4[-1])
print("Velocidade apartir do método analitico é",v_ana[-1])
print("Velocidade apartir do método euler é",v_euler[-1])

plt.figure()
plt.plot(t,vy_rk4,label="Método de Runge-Katta")
plt.plot(t,v_ana,label="Método analitico")
plt.plot(t,v_euler, label="Método Euler")
plt.legend()
plt.grid()

plt.show()