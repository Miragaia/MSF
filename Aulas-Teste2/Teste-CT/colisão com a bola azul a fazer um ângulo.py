import numpy as np      #colisão com a bola azul a fazer um ângulo de 𝜙 = 35°
import matplotlib.pyplot as plt
con=np.pi/180.
phi=35 #ANGULO
theta=90.-phi
phi=phi*con
theta=theta*con
det=-np.cos(theta)*np.sin(phi)-np.sin(theta)*np.cos(phi)
vaz=-np.sin(phi)/det
vam=-np.cos(phi)/det
v2=vaz**2+vam**2
print('det, vaz, vam, vaz**2 + vam**2 = ', det,vaz,vam,v2)
a=np.array([[np.cos(theta), np.cos(phi)], [np.sin(theta), -np.sin(phi)]]) #VELOCIDADE BOLA 1 POS COLISAO
b=np.array([1,0]) #VELOCIDADE BOLA 2 POS COLISAO
x = np.linalg.solve(a, b)
print(x)
