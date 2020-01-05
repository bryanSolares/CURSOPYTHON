"""
instalación local del paquete que permite llamar sus funciones sin modificar rutas de busqueda
crear un archivo llamado: setup.py = contiene descripción del paquete a distribuir
nombre paquete, versión, descripción, autor, etc.

para crear el paquete ir a la ruta del setup, abrir consola y ejecutar: python setup.py sdist
para instalar, abrir consola en ubicacion de paquete y ejecutar: pip3 install nombrepaquete.tar.gz
para desintalar, abrir consola y ejecutar: pip3 unistall nombrepaquete.tar.gz

estructura de setup.py

setup(
    name = "PaqueteCalculos",
    version = "1.0",
    description = "Uso de funciones avanzadas de matematicas",
    author = "Bryan Solares",
    author_email = "solares.josue@outlook.com",
    url = "www.makibiway.com",
    packages = ["calculos_video_35","calculos_video_35.avanzados_35"] #sumamente importante
)
"""