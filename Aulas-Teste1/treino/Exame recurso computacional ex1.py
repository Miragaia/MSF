import matplotlib.pyplot as plt 
import numpy as np

a = np.array([3.522, 2.793, 2.098 , 1.681, 1.557, 1.089, 1.050, 0.896, 0.669, 0.640])
R = np.array([3.389, 3.924, 4.459, 4.993 , 5.528, 6.062, 6.597, 7.131, 7.666, 8.200])
###########
x=R
y=a

plt.scatter(x, y)
plt.xlabel('R (10**6 m)')
plt.ylabel('Y (m/s**2)')
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

###########

x=np.log(R)
y=np.log(a)

plt.scatter(x, y)
plt.xlabel('R (10**6 m)')
plt.ylabel('Y (m/s**2)')
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

##################

x=R**(-1.96)
y=a

plt.scatter(x, y)
plt.xlabel('R (10**6 m)')
plt.ylabel('Y (m/s**2)')
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

#R: realção a = (39 +/- 2) * R**(-1.96) + (0.04 +/- 0.05) # y = (m +/- dm) * x**(declive dos logs) + (b +/- db)
# é um bom ajuste pois r**2 se aproxima de 1