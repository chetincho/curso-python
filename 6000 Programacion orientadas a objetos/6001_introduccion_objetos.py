
# Aca definimos la Clase Empleado
class ClaseEmpleado:
    
    # Asi definimos los atributo de clase
    sindicalizado = False

    # Asi definimos los atributo de instancia
    def __init__(self, nombre, apellido, puesto):
        self.nombre = nombre
        self.apellido = apellido
        self.puesto = puesto

    # Aca definimos dos métodos, uno para cambiar de puesto y otro
    # para cambiar la situacion de sindicalizado
    def cambiar_de_puesto(self, puesto):
        self.puesto = puesto
    
    def sindicalizar(self, sindicalizado):
        self.sindicalizado = sindicalizado


# Así definimos un objeto de tipo ClaseEmpleado 
objeto_empleado = ClaseEmpleado("Juan", "Perez", "Vendedor")

# Asi mostramos en pantalla el tipo de la variable objeto_empleado
print(f"El tipo de la variable objeto_empleado es: {type(objeto_empleado)}")

# Asi mostramos en pantalla los valores asignados a cada uno de los atributos del objeto 
print(f"El nombre del empleado es: {objeto_empleado.nombre}")
print(f"¿Ek¿l empleado se encuentra sindicalizado?: {objeto_empleado.sindicalizado}")

print("-"*10)

# Asi mostramos en pantalla los valores asignados a cada uno de los atributos del objeto 
print(f"El puesto de {objeto_empleado.nombre} es {objeto_empleado.puesto}")
objeto_empleado.cambiar_de_puesto("Gerente")
print(f"El nuevo puesto de {objeto_empleado.nombre} es {objeto_empleado.puesto}")
