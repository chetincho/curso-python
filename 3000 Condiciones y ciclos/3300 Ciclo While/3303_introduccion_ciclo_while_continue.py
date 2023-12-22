print()

contador = 0

while contador <= 10 :
    
    if contador % 2 == 0 :
        contador = contador + 1
        continue
    else:
        print(f" El valor de la variable contador es: -> {contador} <-")
    
    contador = contador + 1

print()

# En este ejemplo el ciclo while se ve interrumpido con un break
# cuando la variable contador alcanza el valor 5.