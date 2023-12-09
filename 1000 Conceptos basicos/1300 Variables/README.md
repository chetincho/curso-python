# Variables
Una variable es un objeto el cual nos permite almacenar temporalmente un valor en la memoria del computador, dicho valor además puede cambiar durante la ejecución del programa.

Para definir una variable necesitamos 3 componentes:
    - un nombre
    - el signo igual
    - un valor
Por ejemplo, a continuación definimos una variable llamada "nombre" la cual almacena el valor Ana.

` nombre = "Ana"`


Las variables pueden ser de tipo:
* String o texto. Ej: "Ana"
    ` nombre = "Ana"`
* Números enteros. Ej: 20
    ` edad = 20`
* Números decimales o flotantes. Ej: 1.60 (importante, el separador decimal en Python es el punto "." y no la coma ",")
    ` altura = 1.65`
* Booleanos. Ej: True o False (importante, notar que tanto la palabra reservada true y false se escriben con la primera letra en mayúsculas)
    ` es_mujer = True`
    ` es_hombre = False`
    ` es_no_binario = False`

Por último Python nos da una función la cual nos permite conocer el tipo de una variable, estamos hablando de la función type(). Veamos cómo funciona la función type en el archivo **1301_variables.py**