# Type hinting

El concepto Type hinting hace referencia a lo que se conoce en los lenguajes de programación como Tipado. El tipado determina cómo son declaradas las variables del lenguaje de programación.

El tipado puede ser ESTÁTICO o DINÁMICO.
- Tipado Estático: Aquí los errores de tipos de datos son validados ANTES de que el código sea ejecutado, es decir, en tiempo de compilación.
En este tipo de lenguaje el tipo de dato de una variable se declara expresamente en el código fuente de nuestro programa. Un ejemplo de lenguajes de tipado estático con Java y C.

- Tipado Dinámico: Aquí el tipo de dato de una variable se valida en tiempo de ejecución, es decir, el error aparece cuando nuestro programa ya esta corriendo. A diferencia del tipado estático no hay una declaración expresa de cuál es el tipo de datos de una variable. Un ejemplo de lenguajes de tipado dinámico son JavaScript y Python.

El type hinting es una solución que nos permite tratar el código escrito en Python como si fuese de tipado estático.

Con type hinting podemos:
- Declarar el tipo de una variable tanto dentro como fuera de una función.
- Definir el tipo de variable que esperamos en una función así como también el tipo de datos retornado.

Por último contamos con la librería `mypy` la cual nos permite verificar el tipado antes de que el código sea ejecutado, esto nos permite tratar a Python como un lenguaje de tipado estático.

Al utilizar type hinting declaramos junto con la variable el tipo de datos de la misma, esto es conocido como anotaciones. Las anotaciones no tienen efecto cuando se ejecuta el código. En el archivo `9101_variables_type_hinting.py` podes ver un ejemplo de tipado de variables.

En el archivo `9102_funciones_type_hinting.py` podemos ver un ejemplo del uso de type hinting en la definición de funciones. En este caso la definición de los tipos se hace en la misma linea donde se declara el nombre de la función. Junto con la definición del tipo de datos de los parámetros podemos definir el tipo de datos devuelto por la función, esto lo hacemos con la anotación `-> int :`. En el caso que la función no devolviera ningún valor lo definimos de la siguiente manera `-> None :`



 
<br>
<br>
<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Martin_Ferraguti-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=101010)](https://www.linkedin.com/in/martin-ferraguti/)
