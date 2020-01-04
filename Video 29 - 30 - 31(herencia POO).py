#clase padre
class Vehiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar (self):
        self.enmarcha = True
    
    def acelerar (self):
        self.acelera = True
    
    def frenar (self):
        self.frena = True

    def estadoVehiculo(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

#Clase moto heredando propiedad de vehiculo (se coloca entre parentesis)
class Furgoneta(Vehiculo):
    
    def carga(self,carga):
        self.carga = carga

        if self.carga == True:
            return "La furgoneta está cargada"
        else:
            return "La furgoneta está vacia"

#Clase moto heredando propiedad de vehiculo (se coloca entre parentesis)
class Moto(Vehiculo):
    
    __caballito = ""

    def haceCaballito(self):
        self.__caballito = "Acción de realizar caballito"

    def estadoVehiculo(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha,
        "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.__caballito)

class VehiculosElectricos():

    __autonomia = "100"

    def __init__(self): # <-- El constructor se toma en cuenta hasta cuando se crea una objeto de la clase del constructor
        self.__autonomia = "200"

    def cargarEnergia(self):
        self.cargando = True
        print("Cargado Energía")
        print("Autonomía: ", self.__autonomia)

#herencia múltiple
class BicicletaElectrica(Vehiculo,VehiculosElectricos):
    pass


moto = Moto("Honda", "2019")
moto.haceCaballito()
moto.estadoVehiculo()

print("--------------------------------------")

furgoneta = Furgoneta("Renault","Kangoo")
furgoneta.arrancar()
furgoneta.estadoVehiculo()
print(furgoneta.carga(True))

print("--------------------------------------")

bicicleta = BicicletaElectrica("Orbea","HX10030")
bicicleta.acelerar()
bicicleta.estadoVehiculo()
bicicleta.cargarEnergia()



