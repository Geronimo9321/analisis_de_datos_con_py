from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Mensajes de entrenamiento
mensajes = [
    "hola amigo como estas",
    "que tengas un excelente dia",
    "muchas gracias por tu ayuda",
    "me alegra hablar contigo",
    "eres una gran persona",

    "te odio",
    "eres insoportable",
    "no quiero verte nunca mas",
    "dejame en paz",
    "estoy muy enojado contigo"
]

# Etiquetas asociadas
etiquetas = [
    "amigable",
    "amigable",
    "amigable",
    "amigable",
    "amigable",

    "agresivo",
    "agresivo",
    "agresivo",
    "agresivo",
    "agresivo"
]

# Convertimos los textos en números
vectorizador = CountVectorizer()
X = vectorizador.fit_transform(mensajes)

# Entrenamos el modelo
modelo = MultinomialNB()
modelo.fit(X, etiquetas)

# Mensajes para probar
mensajes_prueba = [
    "hola que tal amigo",
    "muchas gracias",
    "te odio mucho",
    "dejame tranquilo",
    "eres una excelente persona"
]

# Realizamos las predicciones
for mensaje in mensajes_prueba:
    X_nuevo = vectorizador.transform([mensaje])
    prediccion = modelo.predict(X_nuevo)

    print("Mensaje:", mensaje)
    print("Clasificación:", prediccion[0])
    print()