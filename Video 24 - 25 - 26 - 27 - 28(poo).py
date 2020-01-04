class Coche():

    def __init__(self): # <---- constructor de una clase
        self.__largoChasis = 400 # <--- __nombrevariable = encapsulamiento de variables (private en java)
        self.__anchoChasis = 200
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        
        if self.__enmarcha:
            chequeo = self.__chequeoInterno()

        if (self.__enmarcha and chequeo == True):
            return "El coche está en movimiento"
        elif (self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo no podemos arrancar."
        else:
            return "El coche está estacionado"

    def estado(self):
        print("***** Estado *****")
        print(self.__largoChasis)
        print(self.__anchoChasis)
        print(self.__ruedas)
        print(self.__enmarcha)

    def __chequeoInterno(self): # <-- encapsulación de método (java método private)
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"

        if (self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False



micoche = Coche()
print(micoche.arrancar(False))
micoche.estado()

print("**********************")

micoche2 = Coche()
print(micoche2.arrancar(True))
micoche2.estado()