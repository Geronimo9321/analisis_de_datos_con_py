import numpy as np
import matplotlib.pyplot as plt 

#Genero 100 puntos entre -5 y 5
X = np.linspace(-5, 5, 100)

#Aplico la fórmula
Y = np.exp(-(X**2)/2)

#Grafico
plt.plot(X, Y)

plt.show()