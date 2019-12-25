#creación de diccionario = HashMap en java

midiccionario = {"Alemania":"Belín","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
midiccionario2 = {2:3434,3:"Guatemala","Belleza":23.3434}
print(midiccionario)
print(midiccionario2)

#accediendo a un elemento de acuerdo a una clave
print(midiccionario["Francia"])

#añadir elemento a diccionario
midiccionario["Italia"] = "Lisboa"
print(midiccionario)

#modificar elemento a partir de una clave (los valores se reescriben no se admiten claves duplicadas)
midiccionario["Italia"] = "Roma"
print(midiccionario)

#eliminación de elementos
del(midiccionario["Reino Unido"])
print(midiccionario)

#usar lista para claves
lista = ["Guatemala","El Salvador","Honduras"]
midicc = {lista[0]:"guatemala",lista[1]:"el salvador",lista[2]:"honduras"}
print(midicc)
print(midicc["Guatemala"])

#diccionario almacenando lista
midiccionario3 = {23:"Jordan", "Nombre: ": "Bryan Solares","Edad: ":24,"Anillos":[1991,1992,1993,1996,1997,1998]}
print(midiccionario3)
print(midiccionario3["Anillos"])

#subdiccionarios
midiccionario3 = {23:"Jordan", "Nombre: ": "Bryan Solares","Edad: ":24,"Anillos":{"Temporadas":[1991,1992,1993,1996,1997,1998]}}
print(midiccionario3)
print(midiccionario3["Anillos"]["Temporadas"])
print(midiccionario3["Anillos"].values())

#devuelve claves, valores, longitud
print(midiccionario3.keys())
print(midiccionario3.values())
print(len(midiccionario3))