import numpy as np
import matplotlib.pyplot as plt


dt=0.001
tf=100.00
n=np.int(tf/dt+0.1)

t=np.linspace(0,tf,n)

print(n)

x=np.empty(n)
v=np.empty(n)
x0=4   ###mudar
v0=0   ###mudar
x[0]=x0
v[0]=v0

k=1   ###mudar
m=1   ###mudar
w2=k/m

for i in range (0,n-1):
	a=-w2*x[i]
	v[i+1]=v[i]+a*dt
	x[i+1]=x[i]+v[i+1]*dt #euler-cromer


plt.figure()
plt.plot(t,x)
# plt.plot(t,energia,label='W Res')
# plt.ylabel('x(m)')
# plt.xlabel( 't (s)' )
plt.grid()

plt.show()


#####diz valor no inicio do texto 