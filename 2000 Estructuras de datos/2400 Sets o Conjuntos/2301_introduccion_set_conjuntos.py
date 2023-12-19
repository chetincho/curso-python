print()

# Así se define un Set o Conjunto, como se puede ver un set puede estar
# compuesto por valores de distinto tipo.
numeros = {1, 2, 3, 4, 5}
paises = {"Argentina", "Chile", "Brasil", "Paraguay"}
mi_set = {1, "Texto", 1.2, True}

print(f"Contenido del conjunto números: {numeros}")
print()

# Agregamos un nuevo elemento al conjunto 
numeros.add(6)
print(f"Asi queda el conjunto números luego de insertar el valor 6: {numeros}")
print()

# Esto es lo que sucede cuando queremos insertar un elemento repetido 
# a un set.
numeros.add(7)
numeros.add(7)
numeros.add(7)
print(f"Intentamos insertar el valor 7 tres veces, pero solo lo inserto una vez: {numeros}")
print()

# Así podemos insertar varios valores en un solo paso. Tener en cuenta que
# los valores deben estar contenido entre corchetes. Si intentamos insertar
# un valor repetido éste no se inserta.

paises.update(["Peru", "Cuba", "España", "España"])
print(f"Conjunto países: {paises}")
print()

# Con len sabemos la cantidad de elementos que posee un Conjunto
print(f"La cantidad de elementos del set países es: {len(paises)}")
print()

# Con discard podemos eliminar un elemento del set
numeros.discard(5)
print(f"Así queda el set números cuando quitamos el elementos 5: {numeros}")
print()

# Con clear vaciamos un set
paises.clear()
print(f"Asi queda el set cuando ejecutamos el comando clear: {paises}")
print()