# Módulos y paquetes 

Los modulos y paquetes son librerìas que aportan funcionalidades adicionales a las originales de Python.
Dichos modulos y paquetes estan compuestos por funciones.

Modulos: Son archivos en python que pueden contener una o varias funciones.
Paquetes: Son carpetas que contienen modulos. Para la definicion de un paquete debe haber una archivo de inicializacion el cual se cnoce como init en la carpeta.

El uso de modulos y paquetes nos permiten mantener el orden y la reutilizacion del codigo.

IMPORTACION:
Importar una libreria nos permite usar las funciones contenidas en esta.
Para importar una libreria utilizamos la palabra reservada "import" seguido del nombre de la libreria.

`import <nombre_libreria>`
`import datetime`
fecha_hora_actual = datetime.datetime.now()



from datetime import datetime
fecha_hora_actual = datetime.now()