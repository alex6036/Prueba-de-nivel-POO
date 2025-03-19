from superclases.vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, marca, modelo, tipo):
        super().__init__(color, ruedas)
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo

    def __str__(self):
        return f"Bicicleta(color={self.color},ruedas={self.ruedas}, marca={self.marca}, modelo={self.modelo},tipo={self.tipo})"
    
    def __name__(self):
        return self.__class__.__name__
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.color}, {self.ruedas}, {self.marca}, {self.modelo}, {self.tipo})"
    
    def catalogarBicicletas(bicicletas):
        for bicicleta in bicicletas:
            print(type(bicicletas).__name__, bicicleta) 
       
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")
    
    def arrancar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está lista para rodar.")

    def frenar(self):
        print(f"La bicicleta {self.marca} {self.modelo} está frenando.") 