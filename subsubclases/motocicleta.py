from subclases.bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self,color, ruedas, marca, modelo, tipo, velocidad, cilindrada):  
        super().__init__(color, ruedas, marca, modelo, tipo)
        self.cilindrada = cilindrada
        self.velocidad = velocidad

    def __name__(self):
        return self.__class__.__name__

    def __str__(self):
        return f"Motocicleta(color={self.color}, ruedas={self.ruedas}, marca={self.marca}, modelo={self.modelo}, tipo={self.tipo}, velocidad={self.velocidad}, cilindrada={self.cilindrada})"

    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")

    def arrancar(self):
        print("Arrancando la motocicleta")

    def pedalear(self):
        print("Las motocicletas no se pedalean")