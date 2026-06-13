import pandas as pd
import matplotlib.pyplot as plt

archivo = pd.read_excel("notas.xlsx")

notas = archivo["notas"]

plt.figure(figsize=(8, 5))

plt.hist(notas, bins=11)

plt.title("Distribución de notas")
plt.xlabel("Notas")
plt.ylabel("Cantidad de alumnos")

plt.savefig("Notas.png")
plt.show()