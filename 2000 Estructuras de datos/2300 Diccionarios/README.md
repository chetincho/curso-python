# Diccionarios

Características:
* Para su definición se utilizan paréntesis ( ) y sus elementos se separan por comas (,)
* Una tupla almacena sus elementos de forma ordenada, es decir, los elementos mantienen el orden en el cual fueron declarados.
* Los elementos que componen una tupla pueden ser de distinto tipo.
* Las tuplas admiten elementos repetidos.
* Son inmutables, es decir, los valores que componen un tupla NO pueden ser modificados luego de que ésta ha sido creada. Esta es la principal característica la cual diferencia a una tupla de una lista.

Definición:
Esta es la sintaxis para definir una estructura de datos de tipo tupla, en este ejemplo puntual vamos a crear una tupla con el top 5 de los lenguajes de programación más utilizados en 2023:
`lenguajes = ("Python", "Java", "C#", "PHP", "Ruby")`
En el archivo **2201_introduccion_tuplas.py** podrás encontrar varios ejemplos de definiciones de tuplas.

Manipulación
* ¿Cómo accedemos a los elementos de una tupla?
Al igual que con las listas, las tuplas trabajan con índices, el primer elemento recibe el índice 0, el segundo 1 el tercero 2 y así sucesivamente. Por ende, para acceder al tercer elemento de la tupla lenguajes lo hacemos de la siguiente manera: 
`lenguajes[2]`

* Segmentos:
También podemos acceder a una porción de la tupla (segmento), esto lo hacemos de la siguiente manera:
`lenguajes[2:4]`
Donde 2 es el tercer elemento de la tupla y 4 es el último elemento -1 que deseamos mostrar, en este caso el resultado sería C# y PHP.

En el archivo **2202_introduccion_tuplas** podes ver dos ejemplos de consulta/acceso a elementos en la tupla lenguajes.

* Al principio dijimos que las tuplas son inmutables, es decir, que NO podemos modificar sus valores luego de que tupla fue definida.  Debido a esto las tuplas no posee definidas funciones del tipo append y extend.