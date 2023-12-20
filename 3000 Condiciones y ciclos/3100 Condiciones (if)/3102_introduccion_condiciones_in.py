import random

numero = random.randint(1,10)
conjunto = {1, 2, 3, 4, 5}

print("----- EJEMPLO 1 -----")
print(f"La variable numero contiene el valor: {numero}")
print(f"El conjunto esta compuesto por los valores: {conjunto}")


if numero in conjunto :
    print(f"El valor {numero} esta presente en el conjunto {conjunto}")
else :
    print(f"El valor {numero} NO esta presente en el conjunto {conjunto}")





print("----- EJEMPLO 2 -----")
texto = input("Escriba una frase: ")
letra = input("Ingrese una letra de la a a la z: ")


if letra in texto :
    print(f"La letra: {letra} esta presente en el texto: {texto}")
else :
    print(f"La letra: {letra} NO esta presente en el texto: {texto}")
