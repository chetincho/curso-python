# Estructuras de datos

Las estructuras de datos son conjuntos o colecciones de elementos que nos permiten guardar datos de manera ordenada
Por ejemplo, hasta ahora si queriamos almacenar infromacion sobre una persona lo podiamos hacer definiendo una variable por cada valor que queriamos guardar ej.

nombre = "Ana"
apellido = "Perez"
ciudad = "Buenos Aires"
altura = 1.60
edad = 20
es_argentina = True

Un programa utiliza cientos de variables para funcionar, seria muy dificil construir programas si por cada elemento de la relaidad que queremos que represente nuestros software debieramos declarar una variabel, para esto se utilizan las estructuras de datos.

Como dijimos una estructura de datos es un conjunto de elementos, en Python tenemos 4 estructuras de datos basicas cada una de ellas tiene sus propias caracteristicas y funcionalidades. Debemos concerlas para saber cuando usar cada una de ellas segun el caso.

Importante: Decimos que una estructura de datos es mutable cuando podemos modefiicar sus elementos despues de haber sido creadas.

Tipos de estructuras de datos
1. Listas
    Definicion: mi_lista = [elemento1, elemento2, elemento3, ..., elementon]
    Puede contenier elementos duplicados

2. Tuplas
    Definicion: mi_tupla = (elemento1, elemento2, elemento3, ..., elementon)
    Puede contenier elementos duplicados

3. Diccionarios
    Definicion: mi_diccionarios = {
                                      clave1: valor1
                                      clave2: valor2
                                      clave3: valor3
                                      claven: valorn
                                  }
    No puede contener valores clave duplicados.

4. Sets o conjuntos
    Definicion: mi_set = {elemento1, elemento2, elemento3, ..., elementon}
    No Puede contenier elementos duplicados
