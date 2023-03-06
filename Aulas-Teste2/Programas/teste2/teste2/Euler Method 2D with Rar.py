# imports
import numpy as np
import matplotlib.pyplot as plt


def main():
    # imput
    dt = 0.001  # passo temporal
    tf = 1.0  # instante final
    t0 = 0  # instante inicial
    n = np.int((tf - t0) / dt + 0.1)  # numero de passos

    # iniciar os arrays com o tempo, a velocidade e a posição e a aceleração
    t = np.zeros(n + 1)
    vx = np.zeros(n + 1)
    vy = np.zeros(n + 1)
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    ax = np.zeros(n+1)
    ay = np.zeros(n+1)

    # condições iniciais
    g = 9.8  # aceleração gravítica
    alpha = np.deg2rad(10)  # angulo com a horizontal
    v0 = 100 / 3.6  # velocidade inicial
    vt = 100*1000/3600 # velocidade terminal
    D = g/vt**2 #calculo do D para a resistência do ar
    t[0] = t0  # instante inicial
    vx[0] = v0 * np.cos(alpha)  # velocidade inicial eixo x
    vy[0] = v0 * np.sin(alpha)  # velocidade inicial eixo y
    x[0] = 0  # posição inicial eixo x
    y[0] = 0  # posição inicial eixo y

    # Método de Euler
    for i in range(n):
        t[i + 1] = t[i] + dt  # alterar o instante

        vv = np.sqrt(vx[i]**2 + vy[i]**2) # intensidade do vetor velocidade

        ay[i] = -( g + (D*vy[i]*vv)) # alterar a aceleração eixo y
        ax[i] = -D*vx[i]*vv # alterar a aceleração eixo x

        vy[i+1] = vy[i] + ay[i]*dt # alterar a velocidade eixo x
        vx[i+1] = vx[i] + ax[i]*dt # alterar a velocidade eixo y

        x[i + 1] = x[i] + vx[i] * dt  # alterar a posição eixo x
        y[i + 1] = y[i] + vy[i] * dt  # alterar a posição eixo y

    # print gráfico da altura em distância percorrida do tempo
    plt.plot(x, y, color='m')
    plt.ylabel("Altura (m)")
    plt.xlabel("Distância Percorrida (m)")
    plt.grid()
    plt.show()

    # descobrir o máximo vy = 0
    maximo = 0
    tmax = 0
    for i in range(vy.size):
        if y[i-1] < y[i] and y[i+1] < y[i]:
            maximo = y[i]
            tmax = t[i]
    print("A altura máxima atingida pela bola foi {:.2f}m, no instante {:.2f}s.".format(maximo, tmax))

    # descobrir o alcance y = 0
    alcance = 0
    talc = 0
    for i in range(y.size):
        if y[i]*y[i-1] < 0:
            alcance = x[i]
            talc = t[i]
    print("O alcance da bola foi {:.2f}m e demorou {:.2f}s até o atingir.".format(alcance, talc))

main()