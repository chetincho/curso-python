# Ciclo FOR

Permiten iterar sobre distintas estructuras de datos, repitiendo asi una serie de instrucciones por cada elemento contenido en dicha estructura.

Estructura:

`for elemento in estructura_de_datos :`
    `bloque de codigo con instrucciones identadas`

En el archivo `3201_introduccion_ciclo_for.py` tenes un ejemplo de un blucle for iterando sobre una cadena de texto.

Tenemos palabras reservadas en Python (`break` y `continue`) que nos permiten modificar el flujo de ejecucion de un ciclo.
* `break`: Nos permite terminar con la ejecucion de un ciclo, es decir, una vez alcanzado el punto break se interrumpe la ejecucion y se sale del ciclo for.
En el archivo `3202_introduccion_ciclo_for_break.py` tenes un ejemplo de un blucle for iterando sobre una cadena de texto donde si la cadena contiene una letra z entonces se interrumpe la ejecucion del ciclo.
* `continue`: Nos permite saltear o pasar al próximo elemento de la estructura evitando así la ejecución del resto de las líneas que se encuentran debajo de la palabra reservada continue.
En el archivo `3203_introduccion_ciclo_for_continue.py` tenes un ejemplo donde gracias a la palabra reservada continue quitamos las vocales de una cadena de texto ingresada por el usuario.

También podemos iterar en un rango de números desde hasta, para lograr esto usamos la palabra reservada `range`.
* Podemos especificar un punto límite: range(11), esto nos va a permitir itarar entre los números del 0 al 10
* También podemos especificar un rango definido: range(10,15), esto nos va a permitir iterar entre los número del 10 al 14.

<br>
<br>
<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Martin_Ferraguti-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/martin-ferraguti/)