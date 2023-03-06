import matplotlib.pyplot as plt
import numpy as np

t= np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5])
s = np.array([0.121, 0.997, 2.55, 6.09, 9.31, 15.8, 17.1, 25.5, 26.5, 38.8, 41.9])

x= t
y= s

plt.scatter(x, y)
plt.xlabel('t (s)')
plt.ylabel('s (m)')
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

#########

x= np.log(t)
y= np.log(s)

plt.scatter(x, y)
plt.xlabel('log(t) (s)')
plt.ylabel('log(s) (m)')
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

##########




