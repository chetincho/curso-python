# Ciclos y Listas

Podemos usar ciclos for o while para recorrer una lista, la seleccion de un ciclo u otro dependera de las necesidades de cada desarrollador.



Estructura:

`while condicion_sobre_la_cual_iteramos :`
    `bloque de codigo con instrucciones identadas`

Una vez que dicha condicion deja de cumplirse se acaba la ejecucion del ciclo. En el archivo `3301_introduccion_ciclo_while.py` tenes un ejemplo de un ciclo while clásico.

Al igual que con los ciclos for podemos utilizar las palabras reservadas (`break` y `continue`) que nos permiten modificar el flujo de ejecucion de un ciclo.
* `break`: Nos permite terminar con la ejecucion de un ciclo, es decir, una vez alcanzado el punto break se interrumpe la ejecucion y se sale del ciclo.
En el archivo `3302_introduccion_ciclo_while_break.py` tenes un ejemplo del uso de la palabra reservada break.

* `continue`: Nos permite saltear o pasar al próximo elemento de la estructura evitando así la ejecución del resto de las líneas que se encuentran debajo de la palabra reservada continue.
En el archivo `3303_introduccion_ciclo_while_continue.py` tenes un ejemplo donde gracias a la palabra reservada continue solo se muestran en pantalla los numeros pares contenidos del 0 al 10.