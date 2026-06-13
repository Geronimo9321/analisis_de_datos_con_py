import matplotlib.pyplot as plt

colores_sugus = ["Rojo", "Naranja", "Amarillo", "Verde", "Violeta"]
cantidad_personas = [5, 3, 2, 4, 1]

colores = ["red", "orange", "yellow", "green", "purple"]

plt.pie(cantidad_personas, labels=colores_sugus, colors=colores, autopct="%1.1f%%")

plt.title("Color favorito de caramelos Sugus")
plt.show()