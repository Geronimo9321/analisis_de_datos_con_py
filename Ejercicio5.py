import pandas as pd
import matplotlib.pyplot as plt

amazon = pd.read_csv("AMAZON.csv")
google = pd.read_csv("GOOGLE.csv")

datos_amazon = amazon.to_dict("list")
datos_google = google.to_dict("list")

precios_amazon = datos_amazon["Open"]
precios_google = datos_google["Open"]

puntos_cruce = []

for i in range(1, len(precios_amazon)):
    ayer = precios_amazon[i-1] - precios_google[i]
    hoy = precios_amazon[i] - precios_google[i]

    if ayer * hoy < 0:
        puntos_cruce.append(i)

plt.figure(figsize=(12,6))

plt.plot(
    precios_amazon,
    label="AMAZON",
    linestyle="-"
)

plt.plot(
    precios_google,
    label="GOOGLE",
    linestyle="--"
)

for i in puntos_cruce:
    plt.scatter(
        i,
        precios_amazon[i],
        s=80
    )

plt.title("Cotización Amazon vs Google")

plt.xlabel("Días")

plt.ylabel("Precio de apertura")

plt.legend()

plt.grid(True)

plt.show()

print("Cantidad de cruces:", len(puntos_cruce))

print("Índices de cruce:", puntos_cruce)