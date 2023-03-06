import matplotlib.pyplot as plt
import numpy as np

M = np.array([0.15, 0.20, 0.16, 0.11, 0.25, 0.32, 0.40, 0.45, 0.50, 0.55])
T = np.array([1.21, 1.40, 1.26, 1.05, 1.60, 1.78, 2.00, 2.11, 2.22, 2.33])

#a (representar os dados)

x= M
y= T

plt.scatter(x, y)
plt.xlabel('M (Kg)')
plt.ylabel('T (s)')
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
#R: Nào é linear

logM = np.log(M)
logT = np.log(T)

x = logM
y = logT

plt.scatter(x, y)
plt.xlabel('M (Kg)')
plt.ylabel('T (s)')
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

#R: É linear



x = M
y = T**2

plt.scatter(x, y)
plt.xlabel('M (Kg)')
plt.ylabel('T**2 (s)')
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

# É um bom ajuste pois r**2 aproxima se de 1

####d

K = 2*np.pi*()


#a (representar os dados)

x= M
y= T

plt.scatter(x, y)
plt.xlabel('M (Kg)')
plt.ylabel('T (s)')
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