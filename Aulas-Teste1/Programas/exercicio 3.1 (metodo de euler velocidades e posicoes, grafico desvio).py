import numpy as np
import matplotlib.pyplot as plt

#a ( (velocidade) metodo de euler no intervalo de 0 a 4 e no instante 3seg)

v0 = 0
t0 = 0
tf = 4
g = -9.8
dt = 0.01  # nos é que escolhemos o valor, quanto maior o dt menos pontos no grafico nos teremos

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)
v = np.empty(n)  # cria uma lista com n valores vazia
v[0] = 0

for i in range(n-1):  # adicionar valor das velocidades a lista criado em np.empty
    v[i+1] = v[i] + dt*g

""" plt.plot(t, v, label="Aceleração")
plt.legend()
plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.show() """

for i in range(n-1):  # calcular o valor da velocidade em t=3s
    if ((t[i] > (3-dt) and t[i+1] < (3+dt))):
        print("dt, t, v = ", dt, t[i+1], v[i+1])
        
#b ( (posição) metodod e euler no intervalo de 0 a 3, posição no instate 2 seg)

v0 = 0
t0 = 0
tf = 3
g = -9.8
dt = 0.01  # nos é que escolhemos o valor, quanto maior o dt menos pontos no grafico nos teremos
y0 = 0      #diferente (posicao)


n = int((tf-t0)/dt)   
t = np.linspace(t0, tf, n)
v = np.empty(n)  # cria uma lista com n valores vazia
v[0] = 0
y = np.empty(n)  #diferente (posicao)
y[0] = 0         #diferente (posicao)

for i in range(n-1):  # adicionar valor das velocidades a lista criado em np.empty
    v[i+1] = v[i] + dt*g
    y[i+1] = y[i] + v[i] * dt   #diferente (posicao)

""" plt.plot(t, y, label="Posição em função do tempo")
plt.legend()
plt.xlabel("Tempo (S)")
plt.ylabel("Posição (m)")
plt.show() """

for i in range(n-1):  # calcular o valor da posição em t=2  #diferente (posicao)
    if ((t[i] > (2-dt) and t[i+1] < (2+dt))):
        print("dt, t, y = ", dt, t[i+1], y[i+1])

#c (grafico do desvio do valor aproximado e do exato)

a = -9.8
tf = 4
t0 = 0
dt = [0.01, 0.001, 0.0001]

desvio = np.empty(len(dt))

for j in range(len(dt)):
    n = int((tf - t0)/dt[j])
    t = np.linspace(t0, tf, n+1)
    v = np.empty(n+1)
    v[0] = 0
    y = np.empty(n+1)
    y[0] = 0

    for i in range(n):
        v[i+1] = v[i] + a * dt[j]
        y[i+1] = y[i] + v[i] * dt[j]

    for i in range(n):
        if (t[i] > (2-dt[j]) and t[i] < (2+dt[j])):
            print("dt, t, y =", dt[j], t[i], y[i])
            print("dt, t, y =", dt[j], t[i+1], y[i+1])
            desvio[j] = abs(-19.6 - y[i])

plt.xlabel("dt (s)")
plt.ylabel("desvio (m)")
plt.plot(dt, desvio)
plt.legend()
plt.show()