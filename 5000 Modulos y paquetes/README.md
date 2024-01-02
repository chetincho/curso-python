# Módulos y paquetes 

Los modulos y paquetes son librerìas adicionales al código base de Python que aportan funcionalidades extras. Dichos modulos y paquetes estan compuestos por funciones.

Los módulos son archivos en Python que pueden contener una o varias funciones, mientras que los paquetes son un conjunto de módulos compuesto por funciones relacionadas entre si que se guardan dentro de una misma carpeta. El uso de módulos y paquetes nos permiten mantener el orden en un proyecto así como también facilita la reutilización del código.

En Python para definir un paquete la carpeta debe contener un archivo de inicialización llamado `init`.

Las llamadas `liberías` en Python son paquetes que han sido desarrollado por terceros que nos permiten incrementar el alcance funcional del lenguaje y por ende de las aplicaciones desarrolladas en este.

Para poder utilizar una librería en Python en nuestro código primero la tenemos que importar, para ello utilizamos la palabra reservada `import` seguido del nombre de dicha librería.

Por ejemplo: `import datetime`
La librería `datetime` nos permite manipular fechas y horas.

Una vez importada una librería podemos utilizar las funciones contenidas en esta. En el archivo `5001_ejemplo_importacion.py` podes ver un ejemplo de importación y uso de la librería datetime.

¿Cómo crear un módulo en Python?
Para ejemplificar el uso de módulos en Python vamos a crear un módulo que nos permitirá calcular el área y el perímetro de un cuadrado.
En el archivo `ejemplo_crear_modulo.py` podes ver un ejemplo en acción.
Además vamos a crear un archivo llamado `5002_main.py` desde donde llamaremos al módulo que recién creamos.

Para llamar al módulo que nos perite calcular el área y el perímetro de un cuadrado lo podemos hacer de dos formas:
- Forma 1: `import ejemplo_crear_modulo` de esta forma importamos el módulo completo con todas sus funciones.
- Forma 2: `from ejemplo_crear_modulo import area_cuadrado, perimetro_cuadrado` de esta forma importamos el módulo detallando concretamente que funciones queremos utilizar.

¿Cómo crear un paquete en Python?
Paso 1: Vamos a crear una carpeta que haga alusión al conjunto de módulos y funciones que van a contener. En este caso vamos a crear un paquete para gestionar figuras geométricas.
Paso 2: Luego crearemos dentro de dicha carpeta el archivo `__init__.py`, este archivo le indica a Python que esta carpeta es un paquete y que sus archivos van a ser módulos.
Paso 3: Vamos a crear un archivo llamado `cuadrado.py` el cual va a contener las funciones ya desarrolladas `area_cuadrado` y `perimetro_cuadrado`, ademas vamos a crear un segundo archivo llamado `circulo.py` el cual va a contener las funciones `area_circulo` y `perimetro_circulo`.

Por último ahora vamos a hacer uso de las funciones contenidas en los módulos `circulo` y `cuadrado` del paquete `figuras_geometricas` para ello vamos a crear el archivo `5003_ejemplo_uso_paquetes.py` fuera de la carpeta `figuras_geometricas` y desde donde vamos a hacer uso de dichas funciones.

Para llamar a las fuciones utilizamos la palabra reservada `from` seguida del nombre de la carpeta la cual contiene los módulos, en este caso, `figuras_geometricas` seguido de un punto (.) y el nombre de la función.


<br>
<br>
<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Martin_Ferraguti-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/martin-ferraguti/)
