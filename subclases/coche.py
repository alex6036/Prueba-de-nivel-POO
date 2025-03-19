from superclases.vehiculo import Vehiculo
class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
		return "color {}, {} km/h, {} ruedas, {} cc".format(self.color, self.velocidad, self.ruedas, self.cilindrada)
	
	def catalogar(vehiculos):
		for vehiculo in vehiculos:
			print(f"{vehiculo.__class__.__name__}: {vehiculo}")