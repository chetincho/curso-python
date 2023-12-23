

def mostrar_simbolos(signo_mas, signo_menos, signo_multiplicacion ) :
    print(" + " * signo_mas)
    print(" - " * signo_menos)
    print(" * " * signo_multiplicacion)


print("INGRESE LA CANTIDAD DE VECES QUE QUIERE QUE SE REPITA")
signo_mas = int(input("El signo + : "))
signo_menos = int(input("El signo - : "))
signo_multiplicacion = int(input("El signo * : "))


mostrar_simbolos(signo_mas, signo_menos, signo_multiplicacion)


print()