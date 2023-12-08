"""
INTRODUCCION
============

En la programación, las variables hacen referencia a datos temporales que podemos usar en un programa.
En Python definimos las variables como un objeto que tiene un valor que es almacenado en memoria y que además puede cambiar con el tiempo.

.. Las variables las definimos con un nombre, ponemos un igual para indicar que asignaremos un valor y posteriormente definimos ese valor.

Los tipos de variables que se usan en todos los lenguajes de programación incluyendo a Python, 
  de las comillas identifica que estamos tratando con variables de tipo texto. En cuanto a las variables numéricas, tenemos los enteros y los decimales. Los enteros o int son números que no tienen una parte decimal o fracción, por ejemplo, la «edad». En Python no es necesario escribir algo adicional para identificar que estamos hablando de variables numéricas; únicamente es necesario el número. El otro tipo de variable numérica que tenemos es el decimal o flotante, por ejemplo, la «estatura». Es importante resaltar que los decimales en Python usan el punto como separador decimal. Finalmente, tenemos las variables booleanas. Estas solo pueden tener dos valores: verdadero o falso. Definiremos dos variables booleanas: «positivo», que tendrá un valor Verdadero, y «negativo», que tendrá un valor Falso. En Python escribimos estos dos valores en inglés con la primera letra en mayúscula, True para Verdadero y False para Falso. Los booleanos generalmente son utilizados para hacer comparaciones o condiciones. Python cuenta con una función especial que nos permite obtener el tipo de las variables u objetos con los que estemos trabajando. Esta es la función type. Si imprimimos el tipo de la variable «nombre» y posteriormente ejecutamos nuestro programa, obtendremos que la variable nombre es de tipo str, es decir, un string. Podemos repetir este proceso para las otras tres variables y obtendremos el tipo de cada una de ellas. Al volver a ejecutar nuestro programa, obtenemos nuevamente que el nombre es de tipo string, la edad es de tipo int, es decir, un número entero, la estatura es float, o un número flotante o decimal, y por último, la variable positivo es un bool, es decir, una variable booleana que puede tomar un valor positivo o un valor negativo. A lo largo del curso nos vamos a dar cuenta que las variables son una parte esencial del desarrollo Python, ya que las estaremos usando de manera continua en cada uno de nuestros programas.


"""

# Asi definimos una variable de tipo string o texto
nombre = "Ana"

# Si necesitamos almacenar un valor numerico entenro (sin decimales) lo hacemos de esta forma
edad = 20

# En caso que necesitemos almacenar un valor con si contenga una parte decimal lo hacemos de esta forma
estatura = 1.65

# Asi definimos una variable de tipo booleana
positivo = True
negativo = False

# Si queremos imprimir un texto en pantalla utilizando los valores alamcenados en las variables lo podemos hacer de esta forma
print(f"Hola, mi nombre es {nombre}, tengo {edad} años y mido {estatura}")

print("")

# tambien podemos saber de que tipo es una variable, para esto utilizaremos la funcion type
print(f"El tipo de dato de la variable nombre es: {type(nombre)}")
print(f"El tipo de dato de la variable edad es: {type(edad)}")
print(f"El tipo de dato de la variable estatura es: {type(estatura)}")
print(f"El tipo de dato de la variable positivo es: {type(positivo)}")
print(f"El tipo de dato de la variable negativo es: {type(negativo)}")

print("")