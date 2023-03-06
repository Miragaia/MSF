import matplotlib.pyplot as plt
import numpy as np

t= np.array([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5])
s = np.array([0.1,1.4,1.7,6.5,7.7,10.4,19.5,26.1,26.5,45.9,52.5])

#a (representar os dados)

x= np.log(t)
y= np.log(s)

plt.scatter(x, y)
plt.xlabel('logt (s)')
plt.ylabel('logs (cm)')
plt.show()

#b (Calcular as somas das expressoes dos minimos quadráticos)

xy = x * y  # multiplicação ponto a ponto dos elementos da array
x2 = x * x
y2 = y * y

sx = x.sum()
sy = y.sum()
sxy = xy.sum()
sxx = x2.sum()
syy = y2.sum()

print("{:13}{:13}{:13}{:13}{:13}".format("Soma do x",
      "Soma do y", "Soma do x*y", "Soma de x^2", "Soma de y^2"))
print("{:<13}{:<13}{:<13}{:<13}{:<13}".format(sx, sy, sxy, sxx, syy))

#c (Calcular o declive, ordenada na origem, coeficiente de determinação 
#    ou correlação r**2)

npontos = x.size
n = npontos
rn = n*sxy-sx*sy
rd = (n*sxx-sx**2)*(n*syy-sy**2)
r2 = rn**2/rd
r = np.sqrt(r2)

m = (n*sxy-sx*sy)/(n*sxx-sx**2)
dm = abs(m)*np.sqrt((1/r**2-1)/(n-2))

bn = sxx*sy-sx*sxy
bd = n*sxx-sx**2
b = bn/bd
db = dm*np.sqrt(sxx/n)

print()
print("m +/-dm = {:0.8f} +/- {:0.8f}".format(m, dm))
print("b +/-db = {:0.8f} +/- {:0.8f}".format(b, db))
print("r2 = {:0.8f}".format(r2))