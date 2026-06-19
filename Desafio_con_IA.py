import numpy as np

#Datos para el ejercicio
Alturas = [180, 162, 168, 175, 193, 187, 157, 176, 169, 163, 200, 172, 182]
Pesos = [100, 70, 74, 82, 110, 95, 57, 73, 72, 71, 120, 84, 90]

#Modelo Lineal
coef_grado1 = np.polyfit(Alturas, Pesos, 1)
modelo_grado1 = np.poly1d(coef_grado1)

coef_grado2 = np.polyfit(Alturas, Pesos, 2)
modelo_grado2 = np.poly1d(coef_grado2)

#Modelo de grado 20
coef_grado20 = np.polyfit(Alturas, Pesos, 20)
modelo_grado20 = np.poly1d(coef_grado20)

#Alturas a evaluar
alturas_prueba = [150, 170, 190]

#Predicción
print("Predicciones de peso según la altura\n")

for altura in alturas_prueba:

    peso_grado1 = modelo_grado1(altura)
    peso_grado2 = modelo_grado2(altura)
    peso_grado20 = modelo_grado20(altura)

    print(f"Altura: {altura} cm")
    print(f"Peso estimado (Grado1): {peso_grado1:.2f} kg")
    print(f"Peso estimado (Grado2): {peso_grado2:.2f} kg")
    print(f"Peso estimado (Grado20): {peso_grado20:.2f} kg")
    print("-" * 40)

#Las aproximaciones de grado 1 y grado 2 generan resultados similares y coherentes con la relación entre altura y peso. 
#En cambio, la aproximación de grado 20 produce valores absurdos, como 33174 kg para una altura de 150 cm. 
#Esto ocurre porque el modelo se sobreajusta a los datos de entrenamiento (overfitting), intentando pasar exactamente por todos los puntos disponibles. 
#Como consecuencia, la curva presenta oscilaciones exageradas y pierde capacidad para generalizar, por lo que no resulta adecuada para predecir datos nuevos.