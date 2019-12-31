#uso de exepciones

def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplicacion(num1, num2):
    return num1*num2

def division(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre Cero")
        return "Operación Erronea"


try:
    numero1 = (int(input("Ingresa el primer valor: ")))
    numero2 = (int(input("Ingresa el segundo valor: ")))
    operacion = input("Ingresa el tipo de operación que deseas realizar (SUMA - RESTA - MULTI - DIVI)")

    if operacion == "SUMA":
        print(suma(numero1,numero2))
    elif operacion == "RESTA":
        print(resta(numero1,numero2))   
    elif operacion == "MULTI":
        print(multiplicacion(numero1,numero2))
    elif operacion == "DIVI":
        print(division(numero1,numero2))
    else:
        print("Opción no válida")
    
    print("Función ejecutada con éxito")

except ValueError:
    print("No se admiten valores que no sean numéricos")

