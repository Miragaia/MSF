import matplotlib.pyplot as plt
import numpy as np

#a (reta que mais se aproxima das medições)
D = np.array([0.00, 0.735, 1.1363, 1.739, 2.805,
              3.814, 4.458, 4.955, 5.666, 6.329])
T = np.arange(0, 10, 1)

aprox = np.polyfit(T, D, 1)
print(aprox)

#b (grafico log-log, dependencia entre quantidades)
t = [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]
e = [0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7]

plt.plot(np.log(t), np.log(e), 'o')
a = np.polyfit(np.log(t), np.log(e), 1)

t = np.linspace(np.log(t[0])*0.9, np.log(t[-1])*1.1, 100)
plt.plot(t, a[0]*t+a[1])

plt.show()

#c (grafico semilog (d) a depender de (t))
d = [9.676, 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119]
t = np.arange(0, 50, 5)

plt.semilogy(t, d)

plt.ylim([0, 10])

plt.xlim([0, 50])

plt.show()