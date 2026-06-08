import pandas as pd

def promedio_alumno(tabla, indice):

    alumno = tabla.loc[indice]
    promedio = (alumno["Quimica"] + alumno["Matematica"] + alumno["Fisica"]) / 3
    return promedio 

archivo = pd.read_excel("Datos.xlsx")
print(promedio_alumno(archivo, 0))