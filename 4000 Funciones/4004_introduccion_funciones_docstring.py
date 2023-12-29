

def calculadora_avanzada(numero_1, numero_2, simbolo) :
    """Calcula ecuaciones básicas: suma, resta, multiplicación y división
    
    Esta función recibe 3 parametros, dos numéricos y uno de tipo string
    donde se informa el símbolo de la ecuación

    Args:
        numero_1 (int): numero 1
        numero_2 (int): numero 2
        simbolo (str): [+,-,*,/]
    
    Returns:
        El valor de la ecuación en función del símbolo parametrizado
    """
    if simbolo == "+" :
        resultado = numero_1 + numero_2
        operacion = "suma"

    if simbolo == "-" :
        resultado = numero_1 - numero_2
        operacion = "resta"
    
    if simbolo == "*" :
        resultado = numero_1 * numero_2
        operacion = "multiplicacion"
    
    if simbolo == "/" :
        if numero_2 == 0 :
            operacion = "Error division por 0"
            resultado = "Error"
        else :
            resultado = numero_1 / numero_2
            operacion = "division"
    
    return f"El resultado de {operacion} entre {numero_1} y {numero_2} es {resultado}"


numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))
simbolo = input("Ingrese un símbolo [ + - * / ]: ")

print(calculadora_avanzada(numero_1, numero_2, simbolo))