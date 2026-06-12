import numpy as np
import matplotlib.pyplot as plt 

#Ejercicio 1
X = np.linspace(-1, 1, 100)
Y = np.absolute(X)

plt.plot(X, Y)
plt.show()

#Ejercicio 2
X = np.linspace(-5, 5, 100)
Y = np.exp(-(X**2)/2)

plt.plot(X, Y)
plt.show() 