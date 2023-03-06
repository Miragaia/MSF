import numpy as np
import matplotlib.pyplot as plt



dt=0.001
tf=400.0
n=np.int(tf/dt+0.1)
print('n',n)

tempo=np.empty(n+1)
x=np.empty(n+1)
vx=np.empty(n+1)
a=np.empty(n+1)
Em=np.empty(n+1)
	  
t0=0.
x0=3.0            
vx0= -2

tempo[0]=t0
vx[0]=vx0
x[0]=x0

k=1
m=1
b=0.05
F0=7.5
Wf=1
ampl=0
countMax=0
tMax=[]
periodo=[]

for i in range(n):
	tempo[i+1]=tempo[i]+dt
	a[i]=-(k/m)*x[i]-(b/m)*vx[i]+(F0/m)*np.cos(Wf*tempo[i])
	vx[i+1]=vx[i]+a[i]*dt
	x[i+1]=x[i]+vx[i+1]*dt

plt.title('Oscilador Harmónico Forçado Met Euler-Cromer')
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.grid()    
plt.plot(tempo,x)
plt.show()	
