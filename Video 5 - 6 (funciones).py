#Uso de funciones

#declaración de función
def mensaje():
    #cuerpo de funcion
    print("Estamos aprendiendo Python")
    print("Estamos aprendiendo una sintaxis básica")

#llamada de función
mensaje()


def suma():
    num1 = 5
    num2 = 7
    print(num1+num2)

def suma2(num1, num2):
    print(num1+num2)

suma2(2,6)

def suma3(num1,num2):
    resultado = num1+num2
    return resultado

print(suma3(123,123))