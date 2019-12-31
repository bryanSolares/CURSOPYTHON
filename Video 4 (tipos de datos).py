#TIPOS DE DATOS
#NUMERICOS = Enteros (int), COMA FLOTANTE (float), COMPLEJOS
#TEXTOS
#BOLEANSO = True - False

#TIPOS DE OPERADORES
#->ARITMETICOS: +, -, *, /, %, **(exponente), // (division entera)
#->COMPARACION: ==, !=, <, >, >=, <=
#->LOGICOS: AND, OR, NOT
#->ASIGNACION: =, +=, -=, *=, /=, %=, **=, //=
#->ESPECIALES: IS, ISNOT, IN, NOT IN

primerNumero = 10
segundoNumero = 3
print("Uso de módulo -------> " + str(primerNumero%segundoNumero))

print("Uso de Potencia -------> " + str(primerNumero**segundoNumero))

print("Uso de división entera -------> " + str(primerNumero//segundoNumero))

print(type("Nombre"))
print(type('Nombre'))
print(type(5))
print(type(5.45))

#uso de tres dobles comillas

variable = """Es un 
mensaje 
con varios saltos 
de línea"""

print(variable)

#USO DE CONDICIONAL
numero1 = 5
numero2 = 7

if numero1 < numero2:
    print("Primer número mayor que el segundo")
else:
    print("Segundo número es mayor que el primero")


