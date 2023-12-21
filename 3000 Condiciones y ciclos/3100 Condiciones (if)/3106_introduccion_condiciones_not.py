import random

numero = random.randint(1,10)
print(f"El valor de la variable numero es: {numero}")
print()


print("----- EJEMPLO 1 -----")
valor = int(input(f"Ingrese un numero distinto de {numero}: "))
if not (valor == numero):
    print(f"Correcto: El valor {valor} es distinto de {numero}")
else:
    print(f"Error: El valor {valor} es igual a {numero}")


print()


print("----- EJEMPLO 2 -----")
valor = int(input(f"Ingrese un numero igual a {numero}: "))
if not (valor != numero):
    print(f"Correcto: El valor {valor} es igual a {numero}")
else:
    print(f"Error: El valor {valor} es distinto a {numero}")
