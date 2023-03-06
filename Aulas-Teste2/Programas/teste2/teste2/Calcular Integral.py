import numpy as np

t0 = 0.00 ##ponto inicial
tf = 2.00 ##ponto final
N = 21 ##Nº de passos a realizar (numero de fatias + 1)
dt = ((tf-t0)/(N-1))
print("Número de passos: ", N)

x = np.zeros(N+1)
f = np.zeros(N)

for i in range(N):
    x[i+1] = x[i] + dt
    f[i] = (x[i]**3)/4 #valor do integral

## Resolução
i = dt*((f[0] + f[N-1])*0.5 + np.sum(f[1:N-1])) ##Deve-se usar N-1 uma vez que este é o numero de fatias no calculo do integral
print("O integral dado é {}, com dt = {}.".format(i, dt))