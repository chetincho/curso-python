print()

cadena_de_texto = (input("Ingrese un texto: "))
cadena_de_texto.lower()
print()

for letra in cadena_de_texto :
    
    # Si la cadena de texto ingresada contiene una vocal se saltea
    # la ejecución del ciclo for
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u" :
        continue

    print(f"-> {letra} <-")
