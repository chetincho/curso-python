print()

cadena_de_texto = input("Ingrese un texto: ")
print()

for letra in cadena_de_texto :
    
    # Si la cadena de texto ingresada contiene una letra "z" se interrumpe
    # la ejecución del ciclo for
    if letra == "z" or letra == "Z" :
        break   

    print(f"-> {letra} <-")
