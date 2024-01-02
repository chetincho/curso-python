import ejemplo_modulo
from ejemplo_modulo import area_cuadrado, perimetro_cuadrado

lado = 5

area = area_cuadrado(lado)
perimetro = perimetro_cuadrado(lado)

print(f"El Cuadrado con lado {lado} posee un área de {area} y un perímetro de {perimetro}")