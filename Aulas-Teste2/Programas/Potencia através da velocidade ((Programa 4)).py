mass = 75 #peso   ---> alterar(apresentar em kg)
miu = 0.004 #resistencia u  ---> alterar
Cres = 0.9 #Coeficiente Rar  ---> alterar
A = 0.30 #area     ---> alterar(apresentar em m**2)
dAr = 1.225 #Rar
g = 9.80

v = 30*1000/3600 #km/h  ---> alterar(apresentar em km/h)

Rar = 0.5*Cres*A*dAr*(v**2)
N = mass*g
FAt = N*miu

P = (Rar + FAt)*v

print("A uma velocidade de {:.2f} m/s, o ciclista aplica uma potência de {:.2f} W.".format(v,P))