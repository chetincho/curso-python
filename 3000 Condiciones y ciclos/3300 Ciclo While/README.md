# Ciclo WHILE

Nos permite ejecutar una o mas instrucciones mientras se cumpla una condición.

Estructura:

`while condicion_sobre_la_cual_iteramos :`
    `bloque de codigo con instrucciones identadas`

Una vez que dicha condicion deja de cumplirse se acaba la ejecucion del ciclo.

Al igual que con los ciclos for podemos utilizar las palabras reservadas en Python (`break` y `continue`) que nos permiten modificar el flujo de ejecucion de un ciclo.
* `break`: Nos permite terminar con la ejecucion de un ciclo, es decir, una vez alcanzado el punto break se interrumpe la ejecucion y se sale del ciclo.
En el archivo `XXXXXXXXXXXXXXXXXXXX.py` ..................













En el archivo `3201_introduccion_ciclo_for.py` tenes un ejemplo de un blucle for iterando sobre una cadena de texto.

* `continue`: Nos permite saltear o pasar al próximo elemento de la estructura evitando así la ejecución del resto de las líneas que se encuentran debajo de la palabra reservada continue.
En el archivo `3203_introduccion_ciclo_for_continue.py` tenes un ejemplo donde gracias a la palabra reservada continue quitamos las vocales de una cadena de texto ingresada por el usuario.

También podemos iterar en un rango de números desde hasta, para lograr esto usamos la palabra reservada `range`.
* Podemos especificar un punto límite: range(11), esto nos va a permitir itarar entre los números del 0 al 10
* También podemos especificar un rango definido: range(10,15), esto nos va a permitir iterar entre los número del 10 al 14.