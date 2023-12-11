print()

# Así se define un set o conjunto
numeros = {1,2,3}
idiomas = {"ingles", "español", "frances"}
print()

# Intentamos añadir un valor ya existente en el set numeros
print(f"El contenido del set numeros es: {numeros}")
numeros.add(1)
print(f"Luego de volver a intentar añadir el valor 1 asi quedo el set: {numeros}")
print()

# Si necesitamos añadir varios valores a un set usamos la funcion update
print(f"El contenido del set numeros es: {numeros}")
numeros.update([1,4,5,5,5,5,5,6])
print(f"Con update intentamos añadir valores nuevos y repetidos, asi quedo el set: {numeros}")
print()

# Si necesitamos saber cual es la cantidad de elementos de un set usamos len
print(f"La cantidad de elementos del set numeros es: {len(numeros)}")
print()

# Si necesitamos quitar un valor del set podemos usar la funcion discard
print(f"El contenido del set numeros es: {numeros}")
numeros.discard(4)
print(f"Con discard eliminamos el valor 4, asi queda el set: {numeros}")
print()

# Tambien podemos la funcion remove para quitar un valor del 
# set, pero a diferencia de discard si el elemento no forma parte del
# set la funcion nos va a dar error
print(f"El contenido del set numeros es: {numeros}")
numeros.remove(3)
print(f"Con discard eliminamos el valor 4, asi queda el set: {numeros}")
print()

# Por ultimo si queremos vaciar un set lo hacemos utilizando la funcion
# clear
print(f"El contenido del set numeros es: {numeros}")
numeros.clear()
print(f"Luego de ejecutar la funcion clear asi queda el contenido el set numeros: {numeros}")
print()