import pandas as pd

#Leo el archivo Excel y lo convierto en DataFrame
archivo = pd.read_excel("Tabla1.xlsx")

#Al DataFrame lo vuelvo un diccionario de listas
data = archivo.to_dict("list")

#Guardo cada columna en una variable
equipos = data["Equipo"]
goles_favor = data["Goles a favor"]
goles_contra = data["Goles en contra"]

#Recorremos todos los equipos
for i in range(len(equipos)):

    #Calculo la diferencia de gol
    diferencia = goles_favor[i] - goles_contra[i]

    #Muestro el nombre del equipo y su diferencia de gol
    print(equipos[i], "-> Diferencia de gol:", diferencia)