# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 16:12:10 2022

@author: migue
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# exercicio 1

#alinea a
lmA= np.linspace(0,100,10)
x= 70*lmA
plt.plot(lmA,x)

#alinea b
xA0=0
vA= (70*1000)/3600 # O limite de velocidade é de 40 km/h
a= 2.0

t= np.linspace(0, 100,10)
vB = (1/2)*a*(t**2)
plt.plot(t,vB)
plt.show
tencontro = (2*vA)/a
xencontro = vA*tencontro
print(' tempo de encontro :',tencontro)
print('encontrom-se em: ',xencontro)








    



