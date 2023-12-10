# Listas

Características:
* Para su definición se utilizan corchetes ([ ]) y sus elementos se separan por comas (,)
* Una lista almacena sus elementos de forma ordenada, es decir, los elementos mantienen el orden en el cual fueron declarados/definidos.
* Los elementos que componen una lista pueden ser de distinto tipo.
* Admite elementos repetidos.
* Son mutables, es decir, los valores que componen una lista pueden ser modificados luego de que ésta ha sido creada.

Definición:
Esta es la sintaxis para definir una estructura de datos de tipo lista, en este ejemplo puntual almacenamos el top 5 de los lenguajes de programación más utilizados en 2023:
`lenguajes = ["Python", "Java", "C#", "PHP", "Ruby"]`
Te invito a revisar el archivo **2101_introduccion_listas.py** donde encontrarás varios ejemplos de definiciones de listas.


Manipulación
* ¿Cómo accedemos a los elementos de una lista?
Es simple, las listas trabajan con índices, el primer elemento recibe el índice 0, el segundo 1 el tercero 2 y así sucesibamente. Por ende, para acceder al tercer elemento de la lista lenguajes lo hacemos de la siguiente manera: 
`lenguajes[2]`

* Segmentos:
Tambien podemos acceder a una porción de la lista (semento), esto lo hacemos de la siguiente manera:
`lenguajes[2:4]`
Donde 2 es el tercer elemento de la lista y 4 es el último elemento -1 que deseamso mostrar, en este caso el resultado sería C# y PHP.

En el archivo **2102_introduccion_listas** podes ver dos ejemplos de consulta/acceso a elementos en la lista lenguajes.

* Anteriormente dijimos que una las listas son mutables, es decir, que podemos modificar sus valores luego de que lista fue definida. Para ello el pimer paso es acceder al valor y luego utilizando el signo igual (=) asignar el nuevo valor. En este ejemplo vamos a reempalzar el valor C# por Rust.
`lenguajes[2] = "Rust"`

En el archivo **2103_introduccion_listas.py** te dejo un ejemplo.

* Por ultimo nos queda insertar nuevos elementos a una lista. Lo podemos hacer de dos maneras:
1. Utilizando la funcion extend:
`lenguajes.extend(["SQL", "Go", "C#"])`
El resultado es el siguiente: `['Python', 'Java', 'Rust', 'PHP', 'Ruby', 'SQL', 'Go', 'C#']`
2. Utilizando la funcion append:
`lenguajes.append(["SQL", "Go", "C#"])`
El resultado es el siguiente: `['Python', 'Java', 'C#', 'PHP', 'Ruby', ['SQL', 'Go', 'C#']]`

Vemos que el resultado de usar extend y append es ligeramente distinto
 extend: `['Python', 'Java', 'Rust', 'PHP', 'Ruby', 'SQL', 'Go', 'C#']`
 append: `['Python', 'Java', 'C#', 'PHP', 'Ruby', ['SQL', 'Go', 'C#']]`

Con `extend` incorporamos elementos al final de la lista.
Con `append` los elementos se incorporan a la lista como una sublista, o lista anidada.

Para acceder a un elemento dentro de una lista anidada debemos parametrizar dos indices, el primer indice hacer referencia al a la sublista, el segundo indice hacer referencia al elemento que queremos consultar de la sublista. En nuestro caso para la lista `['Python', 'Java', 'C#', 'PHP', 'Ruby', ['SQL', 'Go', 'C#']]` si queremos consultar el elemento "Go" lo hariamos de la siguiente forma:
`lenguajes[5][1]`