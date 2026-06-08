import pandas as pd

archivo = pd.read_excel("Tabla1.xlsx")
data = archivo.to_dict("list")

equipos = data["Equipo"]
puntos = data["Puntos"]

max_puntos = max(puntos)
min_puntos = min(puntos)

indice_campeon = puntos.index(max_puntos)
indice_ultimo = puntos.index(min_puntos)

print("Campeón:", equipos[indice_campeon], "-", max_puntos, "puntos")
print("Último:", equipos[indice_ultimo], "-", min_puntos, "puntos")