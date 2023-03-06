import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

#execricio 2

#alinea a

t= np.linspace(0,4,1000)
vT=6.8
g=9.8
yT=(vT**2/g)*np.log(np.cosh(g*t/vT))
vinst = vT*np.tanh(g*t/vT)
ainst = g/np.cosh(g*t/vT)**2
plt.plot(t, yT)
plt.plot(t,vinst)
plt.plot(t,ainst)
plt.show()

#alinea b

t = sym.Symbol('t', real= True, posittive= True)
vT = sym.Symbol('vT', real=True, positive= True)
g = sym.Symbol('g', real= True, positive= True)
vI= sym.diff((vT**2/g * (sym.log(sym.cosh(g*t/vT)))),t,1)
vI2= sym.simplify(vI)
print('velocidade instantanea: ',vI2)

#alinea c

aI= sym.diff((vT**2/g * (sym.log(sym.cosh(g*t/vT)))),t,2)
aI2= sym.simplify(aI)
print('aceleraçâo instantanea: ',aI2)

#alinea d

ayT = g - ( g/ vT**2)*vI*sym.abs(vI)



