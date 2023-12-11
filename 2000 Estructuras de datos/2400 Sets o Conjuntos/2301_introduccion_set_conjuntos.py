print()

# Así se define un diccionario
datos_personales = {
        "nombre": "Ana",
        "apellido": "Perez",
        "edad": 20,
        "altura": 1.60,
        "nacionalidad": "Argentina",
        "pais_de_residencia": "Argentina",
                   }
print(f"Este es el diccionario definido: {datos_personales}")
print()


# Para acceder al valor contenido en la clave nombre lo hacemos 
# de la siguiente manera
print(f"El nombre del usuario es: {datos_personales['nombre']}")
print()

# Para modificar el valor Ana primero accedemos al dato por medio de la
# clave y luego utilizando el signo igual asociamos el nuevo valor
datos_personales["nombre"] = "Lorena"
print(f"Modificamos el valor Ana por el nuevo valor: {datos_personales['nombre']}")
print()

# Si queremos incorporar un nuevo dato al diccionario lo hacemos 
# definiendo un nuevo par clave/valor
datos_personales["fecha_de_nacimiento"] = "22/11/1984"
print(f"Volvemos a mostrar el diccionario completo, esta vez con los nuevo valores: {datos_personales}")
print()

# En caso que lo necesitemos, los valores de un diccionario pueden ser
# otra estructura de dato como una tupla, una lista o incluso otro diccionario
datos_personales["ideomas"] = ["ingles", "español", "francés"]
print(f"Volvemos a mostrar el diccionario completo, esta vez con los nuevo valores: {datos_personales}")
print()

# Resultado de la función items
print(datos_personales.items())
print()

# Resultado de la función keys
print(datos_personales.keys())
print()

# Resultado de la función values
print(datos_personales.values())
print()