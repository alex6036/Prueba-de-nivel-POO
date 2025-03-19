from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from lanzador import  lanzador_main, catalogar

def mostrar_menu():
	print("Seleccione el tipo de vehículo:")
	print("1. Coche ")
	print("2. Bicicleta")
	print("3. Camioneta")
	print("4. Motocicleta")
	print("5. Ordenar por tipo de ruedas")
	print("6. Salir")

def obtener_datos_vehiculo(tipo):
	if tipo == 1:
		# Obtener datos específicos para Coche
		color = input("Ingrese el color del coche: ")
		ruedas = input("Ingrese el numero de ruedas del coche: ")
		velocidad = input("Ingrese la velocidad del coche: ")
		cilindrada = input("Ingrese la cilindrada del coche: ")
		vehiculo.append(Coche(color, ruedas, velocidad, cilindrada))
		return Coche(color, ruedas, velocidad, cilindrada)
	elif tipo == 2:
		# Obtener datos específicos para Bicicleta
		color = input("Ingrese el color de la bicicleta: ")
		ruedas = input("Ingrese el numero de ruedas de la bicicleta: ")
		marca = input("Ingrese la marca de la bicicleta: ")
		modelo = input("Ingrese el modelo de la bicicleta: ")
		tipo = input("Ingrese el tipo de la bicicleta: ")
		
		return Bicicleta(color, ruedas, marca, modelo, tipo)
	elif tipo == 3:
		# Obtener datos específicos para Camioneta
		color = input("Ingrese el color de la camioneta: ")
		ruedas = input("Ingrese el numero de ruedas de la camioneta: ")
		velocidad = input("Ingrese la velocidad de la camioneta: ")
		cilindrada = input("Ingrese la cilindrada de la camioneta: ")
		marca = input("Ingrese la marca de la camioneta: ")
		modelo = input("Ingrese el modelo de la camioneta: ")
		carga = input("Ingrese la carga de la camioneta: ")
		
		return Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, carga)
	elif tipo == 4:
		# Obtener datos específicos para Motocicleta
		color = input("Ingrese el color de la motocicleta: ")
		ruedas = input("Ingrese el numero de ruedas de la motocicleta: ")
		marca = input("Ingrese la marca de la motocicleta: ")
		modelo = input("Ingrese el modelo de la motocicleta: ")
		tipo = input("Ingrese el tipo de la motocicleta: ")
		velocidad = input("Ingrese la velocidad de la motocicleta: ")
		cilindrada = input("Ingrese la cilindrada de la motocicleta: ")
		
		return Motocicleta(color, ruedas, marca, modelo, tipo, velocidad, cilindrada)
	
	elif tipo == 5:
		# Ordenar por tipo de ruedas
		ruedas = int(input("Ingrese el número de ruedas para filtrar: "))
		catalogar(vehiculos=[], ruedas=ruedas)
		return None

	else:
		return None

if __name__ == "__main__":
	while True:
		mostrar_menu()
		opcion = int(input("Seleccione una opción: "))
		if opcion == 6:
			break
		vehiculo = obtener_datos_vehiculo(opcion)
		if vehiculo:
			print(f"Vehículo creado: {vehiculo}")
		else:
			print("Opción no válida, intente de nuevo.")
	lanzador_main()