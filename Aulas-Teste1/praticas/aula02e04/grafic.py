import matplotlib.pyplot as plt
x=[222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0]
y=[2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0]
plt.scatter(x,y)
plt.show()

for i in x:
    soma= x[i]+y[i]