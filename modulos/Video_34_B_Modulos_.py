"""
archivos con extención py o pyc (python compilado) ó archivo escrito totalmente en c CPython
que posee sus propios espacios de nombres, variables, funciones, clases y submodulos
Utilidad: organización y reutilización de codigo (modularización y reutilización)
Por defecto el llamado del módulo se hace desde la misma ubicación de donde se está llamando
de lo contrarío buscará en el syspath (directorio de instalación de python)
La solución puede ser el uso de paquetes

Paquetes: Directorios donde se almacenarán módulo relacionados entre sí
La creación del paquete consiste en crear una carpeta cuyo interior contendrá un archivo __init__.py
"""

#import Video_34_A_Modulos_ # <-- se tendría que usar el nombre del módulo por delante de la función
from Video_34_A_Modulos_ import * # <-- se usaría todo lo contenido en el módulo o se puede ser explicitos en la función que se necesita

sumar(1,4)
restar(1,4)
multiplicar(13,4)

