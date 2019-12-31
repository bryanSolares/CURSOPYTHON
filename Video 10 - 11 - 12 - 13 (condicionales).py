#Uso de condicionales

print("Programa de evalución de notas de alumnos")

notaAlumno = input("Introduce un nota para la valuación")

def evaluacion(nota):
    valoracion = "Aprobado"
    
    if nota < 5:
        valoracion = "suspenso"
    return valoracion

print(evaluacion(int(notaAlumno)))

##################################################################

print("Programa de verificación de edades")

edad = int(input("Ingresa tu edad"))

if edad < 18:
    print("No estás autorizado")      
elif edad > 80:
    print("No es una edad valida")
else:
    print("Estás autorizado")  


##################################################################

edad = 7

if 0<edad<100:
    print("Edad correcta")
else:
    print("Edad incorrecta")

if edad < 100 and edad > 0:
    print("Edad correcta")
else:
    print("Edad incorrecta")
    
salarioPresidente = int(input("Introduce salario presidente"))
print("Salario presidente: " + str(salarioPresidente))

salarioDirector = int(input("Introduce salario Director"))
print("Salario presidente: " + str(salarioPresidente))

salarioJefeAre = int(input("Introduce salario Jefe de Area"))
print("Salario presidente: " + str(salarioPresidente))

salarioAdministrativo = int(input("Introduce salario Administrativo"))
print("Salario presidente: " + str(salarioPresidente))

if salarioAdministrativo<salarioJefeAre<salarioDirector<salarioPresidente:
    print("Todo funciona correctamente")
else:
    print("Algo anda mal")
    
##################################################################

distancia = int(input())
hermanos = int(input())
salario = float(input())

if distancia > 40 and hermanos > 2 and salario <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
    

if distancia > 40 and hermanos > 2 or salario <= 20000:
    print("Tienes derecho a beca")
else:
    print("No tienes derecho a beca")
    
    
##################################################################

asignatura = input()

if asignatura.lower() in ("Sistemas","Software","Testing","Hardware").lower():
    print("Asignatura aprobada")
else:
    print("Asignatura no aprobada")
