class DATOS:
    def __init__(self, nombre, edad, rh, eps, enfermedad):
        self.Nombre = nombre
        self.Edad = edad
        self.RH = rh
        self.EPS = eps
        self.Enfermedad = enfermedad

def ingresar_datos():
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    rh = input("Ingrese el tipo de RH: ")
    eps = input("Ingrese la EPS: ")
    enfermedad = input("Ingrese la enfermedad: ")
    return DATOS(nombre, edad, rh, eps, enfermedad)

if __name__ == "__main__":
    lista_datos = []

    while True:
        opcion = input("Desea ingresar datos? (s/n): ").lower()
        if opcion == 'n':
            break
        elif opcion == 's':
            datos = ingresar_datos()
            lista_datos.append(datos)
        else:
            print("Opción no válida. Por favor, ingrese 's' para sí o 'n' para no.")

    nombre_buscar = input("Ingrese el nombre para buscar: ")

    for datos in lista_datos:
        if datos.Nombre == nombre_buscar:
            print("\nDatos encontrados para", nombre_buscar)
            print("Nombre:", datos.Nombre)
            print("Edad:", datos.Edad)
            print("RH:", datos.RH)
            print("EPS:", datos.EPS)
            print("Enfermedad:", datos.Enfermedad)
            break
    else:
        print("No se encontraron datos para el nombre ingresado.")
        