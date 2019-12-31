#Uso de bucles
import math as m

#bucle for

for i in [1,2,3]:
    print("Hola Mundo")
    
for i in ["uno","dos","tres",3]:
    print("Hola Mundo " + str(i), end="  ") #end hara que no hayan saltos de líneas o espacios en blanco o lo que sea que se indique en los parentesis del end

for i in "solares.josue@outlook.com":
    if i=="@" and i == ".":
        print(i,end="")
        
for i in range(5):
    print(f"valor de la variable {i}") #notación especial, función de tipo f
        
for i in range(5,20,2): #valor inicial, valor final, valor de cada salto
    print(f"valor de la variable {i}") #notación especial, función de tipo f

email = input("Ingresa un correo electrónico: ")

for i in range(len(email)):
    if email[i] == "@":
        print("Correo válido")
    else:
        print("Correo inválido")
        

##############################################################################################
#USO BUCLE WHILE

i = 1

while i <= 45:
    print(f"Imprimiendo {i}")
    i+=1
    
edad = int(input("Ingrese una edad "))
intentos = 0
while edad < 0 or edad > 100:
    print("Ha ingresado un edad negativa o invalida")
    edad = int(input("Ingrese una edad "))
    intentos += 1
    raizCuadrada = m.sqrt(edad)
    
    if intentos == 10:
        print(f"Raiz cuadrada: {raizCuadrada}")
        break;
    
    
#################################################################################
#USO CONTINUE, PASS, ELSE

for letra in "python":
    if letra == "h":
        continue # ignora las instrucciones que está seguidas del continue
    print(letra)
    
nombre = "pildoras informaticas"
contador = 0
for letra in nombre:
    if letra == " ":
        continue
    contador+=1
    
#pass devuelve nulo
class miclase:
    pass #para implementar más tarde


email = input("Ingresa tu correo electrónico")
for letra in email:
    if letra == "@":
        break;
else:
    print(letra)