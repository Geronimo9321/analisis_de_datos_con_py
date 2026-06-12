import numpy as np
import matplotlib.pyplot as plt

#Genero 100 puntos entre -1 y 1
X = np.linspace(-1, 1, 100)

#Calculo el valor absoluto de cada punto
Y = np.absolute(X)

#Grafico
plt.plot(X, Y)

plt.show()