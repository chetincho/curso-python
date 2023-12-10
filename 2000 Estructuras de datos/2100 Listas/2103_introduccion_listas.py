print()

lenguajes = ["Python", "Java", "C#", "PHP", "Ruby"]
print(lenguajes)
print()


# De esta forma modificamos un valor de una lista.
lenguajes[2] = "Rust"
print(lenguajes)
print()

# Incorporacion de valores a una lista usando la funcion extend
lenguajes.extend(["SQL", "Go", "C#"])
print(lenguajes)
print()

# Volvemos a definir la lista como estaba originalmente
lenguajes = ["Python", "Java", "C#", "PHP", "Ruby"]
print(lenguajes)
print()

# Incorporacion de valores pero esta vez con la funcion append
lenguajes.append(["SQL", "Go", "C#"])
print(lenguajes)
print()

# De esta forma consultamos un valor de una sublista
print(lenguajes[5][1])
print()

# Tambien lo podemos hacer de esta forma dado que la sublista es el ultimo
# elemento de la lista principal
print(lenguajes[-1][1])
print()
