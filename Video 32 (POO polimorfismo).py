#cambio de tipo de objeto o comportamiento dependiendo del contexto

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")


def desplazamientoVehiculo(vehiculo): # <-- implementando polimorfismo (similar a aplicar una interfaz en java)
    vehiculo.desplazamiento()

ve1 = Camion()
desplazamientoVehiculo(ve1)

ve1 = Moto()
desplazamientoVehiculo(ve1)

ve1 = Coche()
desplazamientoVehiculo(ve1)