# Set o Conjuntos

Características:
* Los sets o conjuntos son una colección de elementos ÚNICOS, es decir, los valores contenidos en un set no pueden esta repetidos. Si intentamos agregar un valor que ya esté presente en la estructura de datos el set directamente ignora la inserción.
* Su estructura no está ordenada.
* Los valores de un set pueden ser de distintos tipos.
* Para acceder a sus elementos no utilizamos índices, al ser valores únicos para acceder a un elemento en particular lo hacemos por utilizando el valor en si.
* Los valores contenidos en un set son inmutables, es decir, no podemos editar un valor luego de que el set ha sido definido.

Definición:
* Para definir un set utilizamos llaves y separamos con una coma cada elemento.

`numeros = {1,2,3}`
`idiomas = {"ingles", "español", "francés"}`

* Funciones disponibles para el tratamiento de sets.
    * Con add agregamos un nuevo valor a un set.
    * Con update podemos agregar "n" valores a un set, siempre y cuando no haya repetidos.
    * Con len obtenemos la cantidad de elementos contenidos en el set.
    * Con discard podemos eliminar un elemento del set.
    * Con remove, al igual que con discard, podemos eliminar un elemento del ser, con la diferencia que si el elemento no está presente en el set nos devuelve un error.
    * Con clear vaciamos un set.