print()
# Definimos un diccionario
agenda = {
            "nombre": "Juan Ignacio",
            "apellido": "Perez",
            "edad": 24,
            "nacionalidad": "Argentino",
            "fecha de nacimiento": "22/11/1984",
}

# Iteramos por el par clave valor
print("::: CICLO FOR EN UN DICCIONARIO :::")
for clave in agenda :
    print(f"{clave} : {agenda[clave]}")

print()

# Iteramos por los campos claves (keys), de esta forma se muestran solo las claves del diccionario
print("::: CICLO FOR ITERANDO POR CAMPOS CLAVE :::")
for clave in agenda.keys() :
    print(clave)

print()

# Iteramos por los campos de valor (values), de esta forma se muestran solo los valores asociados a cada clave
print("::: CICLO FOR ITERANDO POR CAMPOS VALOR :::")
for valores in agenda.values() :
    print(valores)

print()

# Iteramos por los campos clave y valor usando el par items
print("::: CICLO FOR ITERANDO POR LOS CAMPOS CLAVE Y VALOR :::")
for claves, valores in agenda.items() :
    print(f"Clave {claves} : Valor {valores}")

print()