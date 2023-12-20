# Importo la librería random para poder hacer uso de sus funciones
import random

# Gracias a la librería random y su función randint genero números aleatorios
# entre 1 y 10 y los almaceno en las variables numero_1 y numero_2
numero_1 = random.randint(1,10)
numero_2 = random.randint(1,10)


print(f"El valor de numero_1 es: {numero_1}")
print(f"El valor de numero_2 es: {numero_2}")


if numero_1 == numero_2 :
    print("numero_1 y numero_2 son iguales")
elif numero_1 < numero_2 :
    print("numero_1 es menor que numero_2")
else :
    print("numero_1 es mayor que numero_2")