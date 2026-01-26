import matplotlib.pyplot as plt
from random import random
x = [80, 50, 70]
y = [90, 100, 60]
a = random()
l = 0.00002
epochs = 1001
y_pred=[]
for i in range(epochs):
    a_diff = 2*176*a-1672/5
    a = a - l * a_diff
for i in range(3) :
    y_pred.append(a*x[i])
plt.scatter(x, y)
plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)])
plt.show()
plt.scatter(x, y)
plt.plot([min(x), max(x)], [min(y_pred), max(y_pred)])
plt.show()
