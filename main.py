from subclases.coche import Coche
from subclases.bicicleta import Bicicleta
from subsubclases.camioneta import Camioneta
from subsubclases.motocicleta import Motocicleta
from lanzador import lanzador_main, catalogar

def mostrar_menu():
    print("Seleccione el tipo de vehículo:")
    print("1. Coche")
    print("2. Bicicleta")
    print("3. Camioneta")
    print("4. Motocicleta")
    print("5. Ordenar por tipo de ruedas")
    print("6. Salir")

def obtener_datos_vehiculo(tipo, vehiculos):
    if tipo == 1:
        color = input("Ingrese el color del coche: ")
        ruedas = int(input("Ingrese el numero de ruedas del coche: "))
        velocidad = int(input("Ingrese la velocidad del coche: "))
        cilindrada = int(input("Ingrese la cilindrada del coche: "))
        return Coche(color, ruedas, velocidad, cilindrada)
    elif tipo == 2:
        color = input("Ingrese el color de la bicicleta: ")
        ruedas = int(input("Ingrese el numero de ruedas de la bicicleta: "))
        marca = input("Ingrese la marca de la bicicleta: ")
        modelo = input("Ingrese el modelo de la bicicleta: ")
        tipo_bici = input("Ingrese el tipo de la bicicleta: ")
        return Bicicleta(color, ruedas, marca, modelo, tipo_bici)
    elif tipo == 3:
        color = input("Ingrese el color de la camioneta: ")
        ruedas = int(input("Ingrese el numero de ruedas de la camioneta: "))
        velocidad = int(input("Ingrese la velocidad de la camioneta: "))
        cilindrada = int(input("Ingrese la cilindrada de la camioneta: "))
        marca = input("Ingrese la marca de la camioneta: ")
        modelo = input("Ingrese el modelo de la camioneta: ")
        carga = int(input("Ingrese la carga de la camioneta: "))
        return Camioneta(color, ruedas, velocidad, cilindrada, marca, modelo, carga)
    elif tipo == 4:
        color = input("Ingrese el color de la motocicleta: ")
        ruedas = int(input("Ingrese el numero de ruedas de la motocicleta: "))
        marca = input("Ingrese la marca de la motocicleta: ")
        modelo = input("Ingrese el modelo de la motocicleta: ")
        tipo_moto = input("Ingrese el tipo de la motocicleta: ")
        velocidad = int(input("Ingrese la velocidad de la motocicleta: "))
        cilindrada = int(input("Ingrese la cilindrada de la motocicleta: "))
        return Motocicleta(color, ruedas, marca, modelo, tipo_moto, velocidad, cilindrada)
    elif tipo == 5:
        ruedas = int(input("Ingrese el número de ruedas para filtrar: "))
        catalogar(vehiculos, ruedas)
        return None
    else:
        return None

if __name__ == "__main__":
    vehiculos = []
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 6:
                break
            vehiculo = obtener_datos_vehiculo(opcion, vehiculos)
            if vehiculo:
                vehiculos.append(vehiculo)
                print(f"Vehículo creado: {vehiculo}")
            elif opcion == 5:
                print("Catalogación realizada.")
            else:
                print("Opción no válida, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
    lanzador_main()