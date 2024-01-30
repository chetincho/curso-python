# Programación Orientadas a Objetos (POO)

La POO es un paradigma de programación que utiliza los conceptos `clases` y `objetos` para organizar y estructurar el código.

Definamos cada uno de estos conceptos:
- Clases: Una clase es un molde el cual nos permite crear objetos. Las clases contienen y definen atributos, tambien conocido como propiedades, y métodos, tambien conocido como funciones.
- Objetos: Un objeto es una INSTANCIA de una clase, esta es la definición formal, dicho en otra palabras, podemos pensar en un objeto como una VARIABLE que toma como modelo a la clase para generar una copia de esta.

Si lo pensamos un poco cuando definimos una variable, por ejemplo de tipo entera (int), estamos definiendo que dicha variable pertenece a la clase int la cual tiene:
- Ciertos atributos, es decir propiedades, por ej: solo puede almacenar numeros y no letras o símbolos.
- Responde a ciertos metodos, o funciones, por ej: podemos sumar, restar, etc.

Lo mismo sucede con los objetos. Cuando definimos un objeto estamos definiendo una variable la cual es de un tipo o clase en particular.

Dependiendo de la clase a la cual asociemos nuestra varible u objeto serán los atributos (propiedades) o métodos (funciones) que tenga disponible dicho objeto.

Ahora bien, ¿porque es importante la POO?, o mejor dicho, ¿de que nos sirve?. La POO llegó para permitirnos definir y modelar "un problema de la vida real" el cual no podría ser modelado con el simple uso de variables de tipo str, int, bool, etc, etc. Aca entra en juego el concepto de `abstracción`.

Veamos un ejemplo de `abstraccion`, vamos a crear la clase "Empleado" para ello utilizamos la palabra reservada `class` seguido del nombre de la clase en formato UpperCamelCase, es decir, en formato título con la primera letra en mayúscula sin separadores acompañado al final por dos puntos (:).

`class Empleado:`

Como te comente mas arriba una clase define atributos, también conocido como las propuiedades o caractrísticas de un objeto.
Hay dos tipos de atributos
- Atributos de Clase: Son aquellos que se definen denro de la clase, todos los objetos que se crean a partir de la clase poseen estos atributos con el valor que hayamos definido.
- Atributos de Instancia: Son aquellos que se definene en el constructor de la clase y su valor son exclusivo de cada objeto que se crea a partir de dicha clase.

Continuemos definiendo los atributos de la clase Empleado.

`class ClaseEmpleado:`
    
`    # Asi definimos los atributo de clase`
`    sindicalizado = False`

`    # Asi definimos los atributo de instancia`
`    def __init__(self, nombre, apellido, puesto):`
`        self.nombre = nombre`
`        self.apellido = apellido`
`        self.puesto = puesto`

Ahora vamos a definir un objeto (variable) de tipo Empleado.

`objeto_empleado = ClaseEmpleado()`

Una vez definida la variable podemos confirmar su tipo utilizando la funcion type:

`print(type(objeto_empleado))`

Esta linea de codigo nos va a devolver el tipo de la variable `objeto_empleado`, es decir, `<class '__main__.ClaseEmpleado'>`

Esta variable `objeto_empleado` de tipo `ClaseEmpleado` ahora posee características propias representadas por el valor que tienen sus atributos.

Por ejemplo:
`objeto_empleado = ClaseEmpleado("Juan", "Perez", "Vendedor")`

Si observamos, los atributos son pasados a la clase en el mismo orden en el cual fueron definidos `def __init__(self, nombre, apellido, puesto)`

Si queremos mostrar el valor de cada uno de los atributos de la clase loa vmos a hacer de la siguiente manera:

`objeto.atributo` es decir `objeto_empleado.nombre`

Para utilizar los metodos contenidos en el objeto lo hacemos de la siguiente manera:

`objeto.nombre_metodo(atributos, si los necesita)` es decir `objeto_empleado.cambiar_de_puesto("Gerente")`

::::::::::::: Me quede en herencia de Python ::::::::::::::::

<br>
<br>
<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Martin_Ferraguti-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/martin-ferraguti/)
