import random

def sumar_y_restar() :
    print(f"La suma de {numero_1} y {numero_2} es: {numero_1+numero_2}")
    print(f"La resta de {numero_1} y {numero_2} es: {numero_1-numero_2}")


numero_1 = random.randint(-10,10)
numero_2 = random.randint(-10,10)


print(f"La variable numero_1 vale {numero_1} y la variable numero_2 vale {numero_2}")
sumar_y_restar()

print()