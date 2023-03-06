import matplotlib.pyplot as plt
import numpy as np
import math
x=np.array([0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329])
y=np.array([0,1,2,3,4,5,6,7,8,9])
m,b = np.polyfit(x,y,1)
plt.scatter(x,y)
plt.plot(x,m*x+b)
plt.show()

#a) Não, uma vez que certas medições não são constantes como as outras ,ou seja, nao tocam na reta de regressão linear

SomaX2=0
SomaX=0
SomaY=0
SomaY2=0
SomaXY=0
N=10

for i in range (len(x)):
    SomaX+=x[i]
    SomaY+=y[i]
    SomaXY+= x[i]*y[i]
    SomaX2+=(x[i])**2
    SomaY2+=(y[i])**2

r=((N*SomaXY-(SomaX*SomaY))**2)/((N*SomaX2-(SomaX**2))*(N*SomaY2-(SomaY**2)))

dm= (abs(m))*(math.sqrt(((1/(r))-1)/(N-2)))
db= dm*math.sqrt((SomaX2)/N)

print("m= ",round(m,9))
print("b= ",round(b,9))
print("r2= ",round(r,9))
print("dm= ",dm)
print("db= ",db)

