# Definición de la clase Computador
class Computador:
    def __init__(self, idEquipo, cargador, mouse, ambiente):
        # Inicializa un nuevo objeto Computador con atributos como ID, cargador, mouse y ambiente.
        self.idEquipo = idEquipo
        self.cargador = cargador
        self.mouse = mouse
        self.ambiente = ambiente
        self.novedades = []  # Lista para almacenar eventos especiales relacionados con el equipo.

    def agregarNovedad(self, fecha, descripcion):
        # Añade un nuevo evento especial al equipo con fecha y descripción dadas.
        self.novedades.append({'fecha': fecha, 'descripcion': descripcion})

    def mostrarInformacion(self):
        # Muestra la información del equipo, incluyendo atributos y eventos especiales.
        print(f"ID del equipo: {self.idEquipo}")
        print(f"Cargador: {self.cargador}")
        print(f"Mouse: {self.mouse}")
        print(f"Ambiente: {self.ambiente}")
        print("Novedades:")
        for novedad in self.novedades:
            print(f"- Fecha: {novedad['fecha']}, Descripción: {novedad['descripcion']}")

# Diccionario para almacenar instancias de la clase Computador
equipos = {}

def agregarEquipo(idEquipo, cargador, mouse, ambiente):
    # Agrega un nuevo equipo al sistema si no existe uno con el mismo ID.
    equipo = equipos.get(idEquipo)
    if equipo:
        print(f"El equipo con ID {idEquipo} ya existe.")
    else:
        equipos[idEquipo] = Computador(idEquipo, cargador, mouse, ambiente)
        print(f"Equipo con ID {idEquipo} agregado exitosamente.")

def buscarEquipo():
    # Solicita al usuario ingresar el ID del equipo y muestra la información del equipo si existe.
    idEquipo = input("Ingrese el ID del equipo a buscar: ")
    equipo = equipos.get(idEquipo)
    if equipo:
        print("Información del equipo:")
        equipo.mostrarInformacion()
    else:
        print(f"No se encontró el equipo con ID {idEquipo}.")

def mostrarEquiposConNovedades():
    # Muestra la información de los equipos que tienen novedades registradas.
    for idEquipo, equipo in equipos.items():
        if equipo.novedades:
            print(f"Equipo con ID {idEquipo} tiene novedades:")
            equipo.mostrarInformacion()

def eliminarEquipo():
    # Solicita al usuario ingresar el ID del equipo y elimina el equipo si existe.
    idEquipo = input("Ingrese el ID del equipo a eliminar: ")
    equipo = equipos.pop(idEquipo, None)
    if equipo:
        print(f"Equipo con ID {idEquipo} eliminado exitosamente.")
    else:
        print(f"No se encontró el equipo con ID {idEquipo}.")

def modificarEquipo():
    # Solicita al usuario ingresar el ID del equipo y realiza modificaciones si el equipo existe.
    idEquipo = input("Ingrese el ID del equipo a modificar: ")
    equipo = equipos.get(idEquipo)
    if equipo:
        # Solicita al usuario ingresar los nuevos valores y modifica el equipo.
        nuevo_cargador = input("Ingrese el nuevo cargador: ")
        nuevo_mouse = input("Ingrese el nuevo mouse: ")
        nuevo_ambiente = input("Ingrese el nuevo ambiente: ")
        equipo.cargador = nuevo_cargador
        equipo.mouse = nuevo_mouse
        equipo.ambiente = nuevo_ambiente
        print(f"Equipo con ID {idEquipo} modificado exitosamente.")
    else:
        print(f"No se encontró el equipo con ID {idEquipo}.")

def agregarAmbiente():
    # Solicita al usuario ingresar el ID del equipo y agrega un nuevo ambiente si el equipo existe.
    idEquipo = input("Ingrese el ID del equipo al que desea agregar ambiente: ")
    ambiente = input("Ingrese el nuevo ambiente: ")
    equipo = equipos.get(idEquipo)
    if equipo:
        equipo.ambiente = ambiente
        print(f"Ambiente agregado al equipo con ID {idEquipo}.")
    else:
        print(f"No se encontró el equipo con ID {idEquipo}.")

# Bloque principal
if __name__ == "__main__":
    while True:
        # Muestra el menú de opciones al usuario y realiza la acción correspondiente.
        print("\nMenú:")
        print("1. Agregar equipo")
        print("2. Agregar novedad")
        print("3. Buscar equipo")
        print("4. Mostrar equipos con novedades")
        print("5. Eliminar equipo")
        print("6. Modificar equipo")
        print("7. Agregar ambiente")
        print("8. Salir")

        opcion = input("Selecciona una opción (1/2/3/4/5/6/7/8): ")

        if opcion == "1":
            agregarEquipo()
        elif opcion == "2":
            idEquipo = input("Ingrese el ID del equipo: ")
            fecha = input("Ingrese la fecha de la novedad: ")
            descripcion = input("Ingrese la descripción de la novedad: ")
            if idEquipo in equipos:
                equipos[idEquipo].agregarNovedad(fecha, descripcion)
                print("Novedad agregada exitosamente.")
            else:
                print(f"No se encontró el equipo con ID {idEquipo}.")
        elif opcion == "3":
            buscarEquipo()
        elif opcion == "4":
            mostrarEquiposConNovedades()
        elif opcion == "5":
            eliminarEquipo()
        elif opcion == "6":
            modificarEquipo()
        elif opcion == "7":
            agregarAmbiente()
        elif opcion == "8":
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")
