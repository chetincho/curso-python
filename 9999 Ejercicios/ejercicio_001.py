"""
Ejercicio 001
En funcion de una palabra ingresada por el usuario repetirla la cantidad de veces que el usuario decida
"""

# Presentación: este bloque de código suelo repetirlo en todos los ejercicios, lo hago simplemente por una
# cuestión estética para mostrar los resultados de la resolución al problema con la consola en blanco.
import os
os.system('cls')

print("======================")
print("   ejercicio_001.py   ")
print("======================")
print()

# --- Resolución --- #
palabra = input("Ingresa una palabra: ")
repetir = int(input("¿Cuantas veces queres que se repita tu palabra?: "))

palabra = palabra * repetir

print()
print(f"Resultado: {palabra}")