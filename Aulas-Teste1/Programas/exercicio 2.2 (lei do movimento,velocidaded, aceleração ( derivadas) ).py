import numpy as np
import matplotlib.pyplot as plt
import sympy as sym
from cmath import sqrt

#a (lei do movimento)
vT = 6.80
g = 9.8

t = np.linspace(0, 4, 100)  #defeniçao do tempo (0 aos 4 segundos)
y = ((vT**2)/g)*np.log(np.cosh((g*t)/vT)) # lei do movimento

plt.plot(t, y)
plt.grid()
plt.show()

#b (velocidade instantanea(derivada da lei do movimento))

t = sym.Symbol("t")
v = sym.Symbol("v")
vt = sym.Symbol("vt")
g = sym.Symbol("g")
D = sym.Symbol("D")

D = sym.Derivative((((vT**2)/g)*sym.log(sym.cosh((g*t)/vT))), t, evaluate=True)
D_simplificado = sym.simplify(D)
print("Função da velocidade: ", D_simplificado)

tempo = np.linspace(0, 4, 200)
funcao = 6.8*np.tanh(9.8*tempo/6.8)
plt.plot(tempo, funcao)
plt.grid()
plt.show()

#c (aceleração instantanea (derivada das velocidades))

D = sym.Derivative((vT*sym.tanh(g*t/vT)), t, evaluate=True)
Ds = sym.simplify(D)
print(D)
print("Aceleracao em funçao do tempo: ", Ds)

tempo = np.linspace(0, 4, 200)

formula = 9.8/np.cosh(9.8*tempo/6.8)**2
plt.plot(tempo, formula)
plt.grid()
plt.show()

#d (formula da aceleração com os valores do exercicio)

tempo = np.linspace(0, 4, 20)

funcao = 9.8/np.cosh(9.8*tempo/6.8)**2

expression = 10 - 10 / 6.8 ** 2 * \
    (6.8*np.tanh(10*tempo/6.8)) * (6.8*np.tanh(10*tempo/6.8))

plt.plot(tempo, expression)
plt.plot(tempo, funcao, "o")
plt.grid()
plt.show()

#e (queda com e sem resistencia do ar)

y0 = 20
g = 9.8
vT = 6.8

t = (np.arccosh(np.e**(y0*g/vT**2)))*vT/g

print("O tempo com a resitência é: ", t)

ts = sqrt((2*y0)/g)

print("O tempo sem resistencia é: ", ts)

#f

