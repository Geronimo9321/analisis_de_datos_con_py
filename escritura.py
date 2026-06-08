import pandas as pd

estudiantes = {
    "Nombre": ["Juan", "Anabella", "Paul"],
    "Nota": [7, 10, 8]
}

df = pd.DataFrame(estudiantes)
df.to_excel("estudiantes.xlsx")

print("Archivo Excel generado correctamente.")