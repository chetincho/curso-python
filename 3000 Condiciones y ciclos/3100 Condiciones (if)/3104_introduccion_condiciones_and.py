import random

numero_1 = random.randint(1,7)
numero_3 = random.randint(7,14)

print(f"El valor de numero_1 es: {numero_1}")
print(f"El valor de numero_3 es: {numero_3}")

numero_2 = int(input(f"Para GANAR ingrese un valor mayor que {numero_1} pero menor que {numero_3}: "))


if (numero_2 > numero_1) and (numero_2 < numero_3) :
    print(f"GANASTE: {numero_2} es mayor que {numero_1} y menor que {numero_3}")
else :
    print("PERDISTE")