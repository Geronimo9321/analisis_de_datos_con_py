import matplotlib.pyplot as plt

#Marca de celulares
marcas = ["Apple", "Samsung", "Xiaomi", "Vivo", "OPPO", "Otros"]

#Participación de mercado (%)
cuota_mercado = [20, 19, 13, 9, 8, 31]

plt.pie(cuota_mercado, labels=marcas, autopct="%1.1f%%")

plt.title("Cuota global del mercado de smartphones")
plt.show()