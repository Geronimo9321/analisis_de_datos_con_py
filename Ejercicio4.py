import pandas as pd
import matplotlib.pyplot as plt

archivo = pd.read_csv("BTC.csv")
datos = archivo.to_dict("list")
valores = datos["Open"]

maximo = max(valores)
indice_maximo = valores.index(maximo)

fecha_maxima = archivo["Date"][indice_maximo]

plt.figure(figsize=(12,6))

plt.plot(valores)

plt.scatter(indice_maximo, maximo, s=100)
plt.annotate(
    f"Máximo: {maximo}",
    (indice_maximo, maximo)
)

plt.title("Valor de apertura de Bitcoin")
plt.xlabel("Días")
plt.ylabel("Precio (USD)")
plt.grid(True)

plt.show()

print("Valor máximo:", maximo)
print("Fecha:", fecha_maxima) 
