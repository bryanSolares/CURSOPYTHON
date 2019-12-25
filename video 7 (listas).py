#Uso de listas

lista = ["Elemento 1",1,35,"Elemento 2",False,3.56]

print(lista[:])
print(lista[2])

#llamada de datos que genera excepción
#print(lista[10])

#cuando se colocan indices negativos python inicial el conteo desde el final hasta el indice indicado, inicial el conteo desde -1
print(lista[-1])

#accediendo a porciones de una lista
print(lista[0:3])
print(lista[2:4])
#abreviendo cuando se inicia desde cero
print(lista[:3])
print(lista[2:])

#agregando una dato a la vez a la lista, al final de ésta
lista.append("Sandra")
print(lista)

#agregando una dato en un punto intermidio de la lista de acuerdo al indice indicado
lista.insert(2,"Carlos")
print(lista)

#agregando varios elementos a la vez
lista.extend(["Roberto","Ana","Lucia","Roberto"])
print(lista)

#devuelve indice de acuerdo a un elemento preguntado (siempre devuelve el indice del primer elemento encontrado)
print(lista.index("Roberto"))

#comprobar si un elemento está o no en una lista
print("Roberto" in lista)
print("Pepe" in lista)

#eliminación de elementos (elimina el primer elemento encontrado)
lista.remove("Roberto")
lista.remove(False)
print(lista)

#eliminación de último elemento en lista
lista.pop()
print(lista)

#unificación de listas
lista2 = ["Juanito","Pedrito"]
print(lista+lista2)

#repetidor de lista o multiplicador de lista
print(lista*2)

#averiguar tamaño de una lista
print(len(lista))

