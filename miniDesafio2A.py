import pandas as pd

archivo = pd.read_excel("Datos.xlsx")

notas = archivo["Quimica"]

promedio = sum(notas) / len(notas)

print("Promedio:", promedio)