# imports
import numpy as np
import matplotlib.pyplot as plt


# máximo pelo polinómio de Lagrange
def maximo(xm1, xm2, xm3, ym1, ym2, ym3):
    xab = xm1 - xm2
    xac = xm1 - xm3
    xbc = xm2 - xm3

    a = ym1 / (xab * xac)
    b = -ym2 / (xab * xbc)
    c = ym3 / (xac * xbc)

    xmla = (b + c) * xm1 + (a + c) * xm2 + (a + b) * xm3
    xmax = 0.5 * xmla / (a + b + c)

    xta = xmax - xm1
    xtb = xmax - xm2
    xtc = xmax - xm3

    ymax = a * xtb * xtc + b * xta * xtc + c * xta * xtb
    return xmax, ymax


# an e bn pela série de Fourier
def abfourier(tp, xp, it0, it1, nf):
    # cálculo dos coeficientes de Fourier a_nf e b_nf
    #       a_nf = 2/T integral ( x cos nw) dt entre it0 e tt1
    # integracao numerica pelo aproximação trapezoidal
    # input: matrizes tempo tp
    #        posição xp
    #        indices inicial it0
    #        final   it1  (ao fim de um período)
    #        nf índice de Fourier
    # output: af_bf e bf_nf

    dt = tp[1] - tp[0]
    per = tp[it1] - tp[it0]
    ome = 2 * np.pi / per

    s1 = xp[it0] * np.cos(nf * ome * tp[it0])
    s2 = xp[it1] * np.cos(nf * ome * tp[it1])
    st = xp[it0 + 1:it1] * np.cos(nf * ome * tp[it0 + 1:it1])
    soma = np.sum(st)
    q1 = xp[it0] * np.sin(nf * ome * tp[it0])
    q2 = xp[it1 - 1] * np.sin(nf * ome * tp[it1 - 1])
    qt = xp[it0 + 1:it1 - 1] * np.sin(nf * ome * tp[it0 + 1:it1 - 1])
    somq = np.sum(qt)

    intega = ((s1 + s2) / 2 + soma) * dt
    af = 2 / per * intega
    integq = ((q1 + q2) / 2 + somq) * dt
    bf = 2 / per * integq
    return af, bf


# Gráficos
def graphnormal(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.plot(x, y, color='m')
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()


def graphbars(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.bar(x, y)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()


def graphpoints(x, y, title="Gráfico", xaxis="Eixo X", yaxis="Eixo Y"):
    plt.plot(x, y, color='red', marker="o")
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
    plt.grid()
    plt.title(title)
    plt.show()


def main():
    # Condições iniciais
    k = 1  # constante elástica
    m = 1  # massa
    v0 = 0  # velocidade inicial
    x0 = 4  # posição inicial

    # Passo temporal para o Método de Euler
    dt = 0.001  # passo temporal
    t0 = 0.00  # tempo inicial
    tf = 15.00  # tempo final
    n = np.int((tf - t0) / dt)  # nº de passos a realizar

    # Criar os arrays para o Método de Euler
    t = np.zeros(n + 1)
    ax = np.zeros(n + 1)
    vx = np.zeros(n + 1)
    x = np.zeros(n + 1)
    Em = np.zeros(n + 1)

    # Iniciar os arrays
    x[0] = x0
    vx[0] = v0

    # Método de Euler - Cromer
    for i in range(n):
        t[i + 1] = t[i] + dt

        ax[i] = -x[i]

        vx[i + 1] = vx[i] + ax[i] * dt

        x[i + 1] = x[i] + vx[i + 1] * dt

        Em[i] = .5 * m * vx[i] ** 2 + .5 * k * x[i] ** 2

    # Gráfico da Posição em função do tempo
    graphnormal(t, x, "Força Elástica", "Tempo (s)", "Posição (m)")

    # Calcular o máximo para obter a amplitude
    lmax = []  # lista com os máximos
    for i in range(n):
        if x[i - 1] < x[i] > x[i + 1]:
            tmax, xmax = maximo(t[i - 1], t[i], t[i + 1], x[i - 1], x[i], x[i + 1])  # Ponto do máximo
            lmax.append((tmax, xmax))

    # Amplitude
    print("A amplitude do movimento é {:.2f}m".format(lmax[0][1]))

    # Período
    count = 0
    ldif = []
    for i in range(len(lmax)):
        if i != 0:
            ldif.append(lmax[i][0] - lmax[count][0])
            count += 1

    T = sum(ldif) / len(ldif)
    print("O período do movimento é {:.2f}s".format(T))

    # Gráfico da Energia Mecânica em função do tempo
    graphpoints(t, Em, "Sistema Mola-Corpo", "Tempo (s)", "Energia Mecânica (J)")

    # Determinação dos Coeficientes de Fourier
    print(T / dt) # instante de tempo ao fim de um período

    a = np.zeros(20)    # array para os valores de an - cosseno
    b = np.zeros(20)    # array para os valores de bn - seno
    n = np.zeros(20)    # array para os valores de n - índice

    for i in range(20):
        n[i] = i
        a[i], b[i] = abfourier(t, x, 0, int(T / dt), i)

    # Gráfico an - cosseno
    graphbars(n, a, "Coeficiente de Fourier - an", "an", "n")

    # Gráfico bn - seno
    graphbars(n, b, "Coeficiente de Fourier - bn", "bn", "n")

    a, b = abfourier(t, x, 0, int(T / dt), 1)

    print("Os coeficientes de Fourier são, aproximadamente, a = {:.2f}, b = {:.2f}.".format(abs(a), abs(b)))


main()
