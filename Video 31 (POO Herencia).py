class Persona():

    def __init__(self,nombre, edad, residencia):
        self.nombre = nombre
        self.edad = edad
        self.residencia = residencia

    def descripcion(self):
        print("NOMBRE: ",self.nombre, " EDAD: ", self.edad, " RESIDENCIA: ", self.residencia)


class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre, edad, residencia):
        super().__init__(nombre, edad, residencia) # <-- implementando herencia de constructor
        self.__salario = salario
        self.__antiguedad = antiguedad

    def descripcion(self):
        super().descripcion() # <-- implementando herencia de métodos desde super
        print("SALARIO: ", self.__salario, " ANTIGÜEDAD: ", self.__antiguedad)


antonio = Empleado(1400,"2 años","Antonio",24,"Guatemala")
antonio.descripcion()

manuel = Persona("Manuel",23,"Guatemala")
manuel.descripcion()

print(isinstance(antonio,Persona)) # <-- implementando isInstance (principio de sustitución)
print(isinstance(manuel,Empleado)) # <-- implementando isInstance (principio de sustitución)