import numpy as np
import matplotlib.pyplot as plt



dt=0.001
tf=100.00
n=np.int(tf/dt+0.1)

t=np.linspace(0,tf,n)

x=np.empty(n);
v=np.empty(n);
em=np.empty(n);
x0=2.5
v0=3.0
x[0]=x0
v[0]=v0

k=1.8
m=1	
w2=k/m

countMaximos=0
maxTotal=0
difTempos=[]
maximos=[]


for i in range (0,n-1):
	a=-w2*x[i]
	v[i+1]=v[i]+a*dt
	x[i+1]=x[i]+v[i+1]*dt #euler-cromer
	em[i]=0.5*k*x[i]**2+0.5*m*v[i]**2



#calcular o ultimo ponto
em[n-1]=0.5*k*x[n-1]**2+0.5*m*v[n-1]**2

print(em[n-1])
plt.figure()
plt.plot(t,em)

plt.ylabel('Em(J)')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()


plt.figure()
plt.plot(t,x)

plt.ylabel('x(m)')
plt.xlabel( 't (s)' )
plt.grid()

plt.show()