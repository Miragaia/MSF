import numpy as np
import matplotlib.pyplot as plt


g=9.80
v0y=10  ###mudar
y0=0    ###mudar
t=0

vy=10-g*t
y=10*t-(1/2)*g*(t**2)

#altura maxima a v=0
t=10/g
ymax=10*t-(1/2)*g*(t**2)
print("altura maxima t=",t)
print("altura maxima y=",ymax)

#instante que a bolacha acaba o movimento
t=0
t=10*2/g
print("instante que a bolacha acaba o movimento t=",t)



print("---------------------------------")
dt=0.01
tf=4.0
n=np.int(tf/dt+0.1)
print('n',n)



t=np.zeros(n+1)
vy=np.zeros(n+1)
ay=np.zeros(n+1)
y=np.zeros(n+1)

g=9.80      # m/s**2
vt=100*1000/3600  # m/s
vy0=10      # m/s
vy[0]=vy0
t[0]=00
y[0]=0


# b) 
tm=vy0/g
ym=vy0*tm-0.5*g*tm**2
# c)
tsolo=vy0*2/g
print('tm, ym, tsolo = ',tm,ym,tsolo)
# d) 
for i in range(n):
    t[i+1]=t[i]+dt
    vv=np.abs(vy[i])
    dres=g/vt**2
    #ay[i]=-g     # para teste
    ay[i]=-g-dres*vv*vy[i]
    vy[i+1]=vy[i]+ay[i]*dt       
    y[i+1]=y[i]+vy[i]*dt    

#for i in range(n):
#    if t[i+1] > 1-5*dt and  t[i+1] < 1+5*dt:
#        print(t[i+1],x[i+1],vx[i+1],vx[i+1]*3600/1000)
        
for i in range(n):
    if vy[i+1] > 0-0.0005  and  vy[i+1] < 0+0.0005:
        print('altura máxima: ',t[i+1],y[i+1],vy[i+1],vy[i+1]*3600/1000)      
        
for i in range(n):
    if y[i+1] < 0.1  and  y[i+1] > -0.1:
        print('solo: ',t[i+1],y[i+1],vy[i+1],vy[i+1]*3600/1000)      
#
#
#for i in range(n5):
#    t5[i+1]=t5[i]+dt/2
#    vx5[i+1]=vx5[i]+g*dt/2       
#    x5[i+1]=x5[i]+vx5[i]dt/2   # +1/2*g*dt*2       


fig, ax1 = plt.subplots(1)
#ax.set_xticks(np.arange(-5, 20,1))
ax1.set_xlabel( 't (s)' )
ax1.set_ylabel( 'y(t) (m/s)' )
ax1.plot(t,y)
#ax1.plot(t,vx)
#ax1.plot(t,x,'o',label='met Euler dt=0.01 s')
#ax1.plot(ta,xa,label='Exato')
plt.legend()
plt.grid()
ax1.set_title( 'Subida e queda dda bola Vt=100 km m/s' )
#plt.savefig('QuedaVolanteTeste-2.5-y_data.png',bbox_inches="tight")