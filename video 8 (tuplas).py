#lista inmutables (tuplas)
#Más rápidas, menos espacio, formatean String, Pueden utilizarce como clave en un diccionario (las listas no)
#los paréntesis son opcionales

#creación de tupla
mitupla = ("Hola","Mundo","Como","Estan",21223,False,3.53,"Hola")
print(mitupla)
print(mitupla[2])

#conversion de tupla a lista: () -> []
milista = list(mitupla)
print(milista)

#consersion de lista a tupla: [] -> ()
mitupla2 = tuple(milista)
print(mitupla2)

#comprobación de existencia en tupla
print("Hola" in mitupla2)

#comprobación de cuantas veces pueda existir un elemento en una tupla
print(mitupla2.count("Hola"))

#longitud de una tupla
print(len(mitupla2))

#creación de tupla unitaria
mitupla3 = ("Carlos",)
print(len(mitupla3))

#creación de tupla sin parentesis (empaquetado de tupla)
mitupla4 = "Pepe","Carlos",403,33,405.34
print(mitupla4)

#desempaquetado de tupla
mitupla5 = ("Pedro","Barrientos")
nombre, apellido = mitupla5
print(nombre)
print(apellido)