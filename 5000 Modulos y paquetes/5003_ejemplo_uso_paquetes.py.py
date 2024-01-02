from figuras_geometricas.cuadrado import area_cuadrado, perimetro_cuadrado
from figuras_geometricas.circulo import area_circulo, perimetro_circulo

lado = 4
area = area_cuadrado(lado)
perimetro = perimetro_cuadrado(lado)
print(f"El Cuadrado con lado {lado} posee un área de {area} y un perímetro de {perimetro}")


radio = 5
area = area_circulo(radio)
perimetro = perimetro_circulo(radio)
print(f"El Círculo con radio {radio} posee un área de {area} y un perímetro de {perimetro}")