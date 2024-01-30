"""
Ejercicio 000
Dividir una cadena de texto ingresada por el usuario en subcadenas y almacenar todo en una lista
"""

# Presentación: este bloque de código suelo repetirlo en todos los ejercicios, lo hago simplemente por una
# cuestión estética para mostrar los resultados de la resolución al problema con la consola en blanco.
import os
os.system('cls')

print("======================")
print("   ejercicio_000.py   ")
print("======================")
print()

# --- Resolución --- #
cadena = input("Ingrese una cadena de texto: ")
lista_subcadenas = cadena.split()

print()
print(f"Subcadenas: {lista_subcadenas}")