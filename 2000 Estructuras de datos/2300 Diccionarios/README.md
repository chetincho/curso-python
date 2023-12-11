# Diccionarios

Características:
* Almacenan informacion en pares de datos llamados clave y valor donde cada valor corresponde a una llave.
* Las llaves no pueden repetirse, pero los valores si.
* Se definen entre llanes  {} declarando cada par de clave valor separados ambos con un dos puntos :

datos_personales =  {
                        nombre: "Ana"
                        apellido: "Perez"
                        edad: 20
                        altura: 1.60
                        nacionalidad: "Argentina"
                    }
* Para acceder a un valor lo hacemos por la llave.

datos_personales["nombre"] = Ana
* POdemos añadir valores declarando para ello el nuevo par llave valor

datos_personales["fecha_nacimineto"] =  22/11/1984

* No podemos tener dos llaves iguales, las llaves son unicas

* Podemos modificar un valor de una llave.
* Los valores pueden ser otras estructuras de datos

datos_personales["ideomas"] = ["inglres", "español", "frances"]

* funciones:
    items: devuelve una tapla con los pares llave valor
    keys: deveulve una lista con las llaves del diccionario
    values: devuelve una lista con los valores del diccionario


`lenguajes[2:4]`
