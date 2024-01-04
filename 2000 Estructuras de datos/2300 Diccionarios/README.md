# Diccionarios

Características:
* Los diccionarios almacenan información en pares de datos llamados clave y valor, donde cada valor le corresponde una y solo una clave.
* Las claves no pueden repetirse, pero los valores sí, es decir, las claves son ÚNICAS, pero un valor puede repetirse dentro de la estructura de un diccionario. 
* Son estructuras de datos mutables, es decir, pueden cambiar luego de haber sido definidas.

Definición:
Los diccionarios se definen entre llanes {} declarando cada par clave/valor separados ambos con dos puntos (:) y cada par de elementos se separa por una coma.

`datos_personales =  {`
                        `nombre: "Ana",`
                        `apellido: "Perez",`
                        `edad: 20,`
                        `altura: 1.60,`
                        `nacionalidad: "Argentina"`
                        `pais_residencia: "Argentina"`
                    `}`

Manipulación:
* Para acceder a un valor dentro de un diccionario lo hacemos por medio de la clave a la cual está asociado dicho valor. para acceder al valor "Ana" lo hacemos de la siguiente manera.
`datos_personales["nombre"]`

* Para editar un valor primero accedemos al diccionario con su clave y a continuación utilizando el signo igual (=) asociamos el nuevo valor para dicha clave.
`datos_personales["nombre"] = "Lorena"`

* También podemos añadir nuevos elementos a un diccionario, para ello solo basta con definir un nuevo par clave/valor.
`datos_personales["fecha_nacimiento"] =  22/11/1984`

* Al igual que en las listas y tuplas los valores pueden estar contenidos en otras estructuras de cálculo.
`datos_personales["idiomas"] = ["inglés", "español", "francés"]`

* Por ultimo los diccionarios poseen las siguientes funciones:
    - items: devuelve una tupla por cada par clave/valor del diccionario.
    - keys: devuelve una lista conteniendo únicamente las claves del diccionario.
    - values: devuelve una lista conteniendo únicamente los valores del diccionario.

Te dejamos un ejemplo de definición y manipulación de diccionarios en el archivo **2301_introduccion_diccionarios.py**.

<br>
<br>
<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Martin_Ferraguti-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/martin-ferraguti/)