
# Ejemplo de tipado 1: Podemos definir el tipo de dato de la variable
# y el valor todo en una misma linea
nombre: str = "Luis"

# Ejemplo de tipado 2: Primero definimos el tipo de datos y luego el valor
# asignado a la variable
apellido: str
apellido = "Rodriguez"

# Mas ejemplos de tipado en enteros y decimales:
edad: int = 35
altura: float = 1.75


# Tipado en Listas
paises: list = ["Argentina", "Chile", "Uruguay"]

    # Con el tipado en listas podemos definir el tipo de dato contenido
    # dentro de la lista
poblacion: list [str] = ["Argentina", 46044703, 10636.12]


# Tipado en Tuplas
paises: tuple = ("Argentina", "Chile", "Uruguay")

    # Con el tipado en tuplas podemos definir el tipo de cada uno 
    # de los elementos que integran la lista
poblacion: tuple [str, int, float] = ["Argentina", 46044703, 10636.12]

# Tipado en Diccionarios
paises: dict [str, int] = {"id": 344, 
                           "poblacion": 46044703}