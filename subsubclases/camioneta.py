from subclases.coche import Coche


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, marca, modelo, capacidad_carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.marca = marca
        self.modelo = modelo
        self.capacidad_carga = capacidad_carga

    def __str__(self):
        return f"Camioneta(color={self.color}, ruedas={self.ruedas}, velocidad={self.velocidad}, cilindrada={self.cilindrada}, marca={self.marca}, modelo={self.modelo}, capacidad_carga={self.capacidad_carga})"
    
    def __name__(self):
        return self.__class__.__name__
        
    def catalogar(vehiculos):
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {vehiculo}")

    def cargar(self):
        print("La camioneta está cargada")
    
    def descargar(self):
        print("La camioneta está descargada")
    
    def arrancar(self):
        print("Arrancando la camioneta")
    
    def frenar(self):
        print("Frenando la camioneta")