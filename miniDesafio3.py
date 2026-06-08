import pandas as pd

archivo = pd.read_excel("Datos.xlsx")

aprobados = archivo[archivo["Matematica"] >= 6]

total_notas = (
    sum(aprobados["Quimica"]) +
    sum(aprobados["Matematica"]) +
    sum(aprobados["Fisica"])
)

cantidad_notas = len(aprobados) * 3
promedio_general = total_notas / cantidad_notas

print("Promedio general:", promedio_general)