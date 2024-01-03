
ladocuadrado = 5

# Esta funcion realiza el cálculo y lo devuelve con la palabra
# reservada return.
def calcular_perimetro_cuadrado (lado: int) -> int :
    return lado * 4

print(f"El Perímetro del cuadrado con lado {ladocuadrado} es {calcular_perimetro_cuadrado(ladocuadrado)}")



# Esta funcion realiza el cálculo y lo muestra en pantalla sin retornar
# ningún valor.
def calcular_area_cuadrado (lado: int) -> None :
    print(f"El Area del cuadrado con lado {lado} es {lado * lado}")

calcular_area_cuadrado(ladocuadrado)
