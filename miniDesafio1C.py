import pandas as pd

# Leemos el archivo Excel
archivo = pd.read_excel("Tabla1.xlsx")

# Ordenamos la tabla por puntos de mayor a menor
archivo = archivo.sort_values(by="Puntos", ascending=False)

# Convertimos el DataFrame ordenado a diccionario
data = archivo.to_dict("list")

# Guardamos las columnas en variables
equipos = data["Equipo"]
puntos = data["Puntos"]
goles_favor = data["Goles a favor"]
goles_contra = data["Goles en contra"]

print("Equipos con más de 20 puntos:\n")

# Recorremos los equipos ya ordenados
for i in range(len(equipos)):

    # Verificamos si tiene más de 20 puntos
    if puntos[i] > 20:

        # Calculamos la diferencia de gol
        diferencia = goles_favor[i] - goles_contra[i]

        # Mostramos el resultado
        print(equipos[i], "- Puntos:", puntos[i], "- Diferencia de gol:", diferencia)