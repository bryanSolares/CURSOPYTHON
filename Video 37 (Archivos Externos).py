"""trabajando con archivos de texto, se utiliza módulo de python io
se trabaja para persistencia de datos
4 fases para guardar un archivo: creación -> apertura -> manipulación - cierre
"""

from io import open

archivotexto = open("archivo.txt","w") # <-- escritura a apartir del final
frase = "Estupendo día para programa en python"
archivotexto.write(frase)
archivotexto.close()

archivotexto = open("archivo.txt","r") # <-- lectura
#archivotexto.seek(11) # <-- situa al cursor a partir del número indicado de caracteres
#archivotexto.read(11) # <-- solo leerá hasta la posición indicada
texto = archivotexto.readlines() # <-- recupera información en una lista
archivotexto.close()
print(texto)

archivotexto = open("archivo.txt","a") # <-- para agregar
archivotexto.write("\nEsta es una nueva línea agregada")
archivotexto.close

archivotexto = open("archivo.txt","r+") # <-- lectura y escritura pero el curso a partir de inicio
archivotexto.write("\nEsta es una nueva línea agregada")
archivotexto.close
