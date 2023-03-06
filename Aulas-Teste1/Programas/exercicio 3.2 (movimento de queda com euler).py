import numpy as np
import matplotlib.pyplot as plt


dt = 0.01
tf = 4.0
n = int(tf/dt+0.1)

t = np.empty(n)
vy = np.empty(n)
ay = np.empty(n)
y = np.empty(n)

g = 9.80
vt = 100/3.6
vy0 = 10
vy[0] = vy0
t[0] = 0
y[0] = 0

for i in range(n-1):  # Calular as equações de acordo com a resistencia do ar
    t[i+1] = t[i]+dt
    vv = np.abs(vy[i])
    dres = g/vt**2
    ay[i] = -g-dres*vv*vy[i]  # formula no formulario
    vy[i+1] = vy[i]+ay[i]*dt
    y[i+1] = y[i]+vy[i]*dt


for i in range(n-1):  # A altura é maxima quando v=0
    if vy[i+1] > 0-0.1 and vy[i+1] < 0+0.1:
        print(
            f'altura máxima - tempo: {t[i+1]}; posição: {y[i+1]}; velocidade (m/s): {vy[i+1]};')

for i in range(n-1):  # Chega ao solo quando y=0
    if y[i+1] < 0.1 and y[i+1] > -0.1:
        print(
            f'Chegada ao solo - tempo: {t[i+1]}; posição: {y[i+1]}; velocidade (m/s): {vy[i+1]};')


plt.plot(t, y)
plt.xlabel('Tempo (s)')
plt.ylabel('Posição (m)')
plt.title('Queda da bola com resistencia do ar')
plt.show()