#uso de generadores
#estructuras que extraen valores de una función y se almacenan en objetos iterables

#tienen más eficiencia que las funciones normales
#Útiles con lista de valores infinitos


#FUNCIONA TRADICIONAL
def generaParesFuncion(limite):
    num = 1
    miLista = []
    
    while num < limite:
        miLista.append(num*2)
        num+=1
    
    return miLista

#GENERADOR
def generaParesGenerador(limite):  
    num = 1
    while num < limite:
        yield num*2
        num+=1
        
resultado = generaParesGenerador(10)

print(generaParesFuncion(10))

print(next(resultado))
print(next(resultado))
print(next(resultado))

#uso de YIELD FROM
print("###########################################################")
def devuelveCiudades(*ciudades): # el asterisco indica que se reciben número indeterminado de elementos y en forma de tupla
    for elemento in ciudades:
        #for subelemento in elemento: #-> forma tradicional          
            yield from elemento # es como implementar un bucle anidado
        
ciudades_devueltas = devuelveCiudades("Madrid","Barcelona","Bilboa","Viñas")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
    