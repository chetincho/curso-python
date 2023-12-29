# Funciones

Son bloques de código independientes cuyo objetivo es realizar una tarea específica.

Ventajas del uso de funciones:
- Nos permiten organizar el codigo en partes pequeñas.
- Esto facilita el entendimineto y la usabilidad y reutilizacion del codigo.
- nos ayuda a evitar repetir instrucciones en distintas partes de nuestro programa.

Estructura: Asi definimos una funcion
`def nombre_de_la_funcion() :`
    `bloques_de_codigo_identado`


Llamdo a la funcion: Asi invocamos a la funcion creada
`nombre_de_la_funcion()`

En Python tenemos dos tipo de funciones:
- Built-in functions: Son funciones nativas, que ya vienen con Python y realizan tareas comunes necesarias para construir software, por ej, print()
- User-defined functions: Son las funciones que como desarrolladores creamos para nuestros programa 

En el archivo `4001_introduccion_funciones.py` podes ver un ejemplo de una user-defined function que nos permite obtener el resultado de sumar y restar dos numeros generados de forma aleatoria.

Cuando trabajamos con funciones las variables pueden ser de dos tipos:
- Locales: Son aquellas que se definen dentro del bloque de ionstruccioens que forman la funcion. Solo pueden ser usadas dentro de la funcion y nunca por fuera.

- Globales: A diferencia de las locales pueden usarse en ucalquier parte del codigo. Por lo general se declaran en mayusculas, las podemos usar dentro y fura de las funciones

Los parametros son los valores que una funcion puede resivir para resolver un problema, se definen dentro de los parentesis y se pasan en el orden en el cual construimos nuestra funcion.
Los parametros se caracterizan por llegar a la funcion con un valor el cual es utilizado para realizar un calculo y este valor puede salir modificado o no de dicha funcion.

En el archivo 4002_introduccion_funciones_parametros.py podes ver un ejemplo de una funcion que utiliza paramtros para resolver la cantidad de veces que debe mostrar un simbolo en pantalla.

Muchas veces necesitamos deolver un valor al proceso principal, para ello usamos la instruccion return que nos permite devolver valores producto de su procesamineto interno, en el archivo 4003_introduccion_funciones_retornar_valores.py podes ver un ejemplo de una funcion que retorna datos luego de procesarlos

Documentacion de las funciones (docstring):