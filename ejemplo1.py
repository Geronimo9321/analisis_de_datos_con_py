import matplotlib.pyplot as plt
import numpy as np

Edad = [0, 10, 20, 30, 40, 50, 60, 70, 80]
Peso = [3, 40, 75, 87, 92, 90, 87, 82, 78]
a, b, c = np.polyfit(Edad, Peso, 2)
X = []
Y = []

for x in range(min(Edad), max(Edad) + 1):
    X.append(x)
    y = a * x**2 + b * x + c
    Y.append(y)

plt.plot(X, Y, color='red')
plt.scatter(Edad, Peso, color='blue', marker='o')
plt.title("Reslación entre edad y peso")
plt.xlabel("Edad (años)")
plt.ylabel("Peso (kg)")
plt.grid(True)
plt.show()