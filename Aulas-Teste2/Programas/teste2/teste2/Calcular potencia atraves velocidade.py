mass = 75 #peso
miu = 0.004 #resistencia u
Cres = 0.9 #Coeficiente Rar
A = 0.30 #area
dAr = 1.225 #Rar
g = 9.80

v = 30*1000/3600 #km/h

Rar = 0.5*Cres*A*dAr*(v**2)
N = mass*g
FAt = N*miu

P = (Rar + FAt)*v

print("A uma velocidade de {:.2f} m/s, o ciclista aplica uma potência de {:.2f} W.".format(v,P))