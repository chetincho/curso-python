print()           # <--- dejamos un espacio para facilitar la lectura de los resultados en la terminal


nombre = "Ana"    # <- Así definimos una variable de tipo texto
edad = 20         # <- Así definimos una variable de tipo número entero
estatura = 1.65   # <- Así definimos una variable de tipo número decimal o flotante
es_mujer = True   # <- Así definimos una variable de tipo booleana
es_hombre = False
es_no_binario = False


# Ahora podemos mostrar en pantalla el contenido de una variable, para ello vamos a usar
# la función print junto con el decorador "f".
print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mido {estatura}")


print()


# Ahora vamos a cambiar los valores almacenados en cada variable
nombre = "Pedro"
edad = 25
estatura = 1.82
es_mujer = False
es_hombre = True
es_no_binario = False


# Prestemos especial atención a la línea 29 de nuestro código, para mostrar los 
# datos en pantalla tuvimos que repetir lo que escribimos en la línea 15. Recordemos esto.
print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mido {estatura}")


print()


# Como vimos en el archivo readme podemos conocer el tipo de datos de una variable
# para ello sumos la función type() 
print(f"La variable nombre es de tipo: {type(nombre)}")
print(f"La variable edad es de tipo: {type(edad)}")
print(f"La variable estatura es de tipo:  {type(estatura)}")
print(f"La variable es_hombre es de tipo: {type(es_hombre)}")


print()