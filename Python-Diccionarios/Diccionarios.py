# Diccionario para almacenar la información de los equipos
equipos = {}

# Función para agregar un equipo de cómputo con su ID, cargador y mouse
def agregar_equipo(id_equipo, cargador, mouse):
    # Verificar si el equipo ya existe en el diccionario
    if id_equipo in equipos:
        print("El equipo con ID {} ya existe.".format(id_equipo))
    else:
        equipos[id_equipo] = {'cargador': cargador, 'mouse': mouse, 'novedades': []}
        print("Equipo con ID {} agregado exitosamente.".format(id_equipo))

# Función para agregar una novedad a un equipo
def agregar_novedad(id_equipo, fecha, descripcion):
    if id_equipo in equipos:
        equipos[id_equipo]['novedades'].append({'fecha': fecha, 'descripcion': descripcion})
        print("Novedad agregada al equipo con ID {}.".format(id_equipo))
    else:
        print("El equipo con ID {} no existe.".format(id_equipo))

# Función para buscar un equipo por su ID y mostrar su información
def buscar_equipo(id_equipo):
    if id_equipo in equipos:
        equipo = equipos[id_equipo]
        print("ID del equipo: {}".format(id_equipo))
        print("Cargador: {}".format(equipo['cargador']))
        print("Mouse: {}".format(equipo['mouse']))
        print("Novedades:")
        for novedad in equipo['novedades']:
            print("- Fecha: {}, Descripción: {}".format(novedad['fecha'], novedad['descripcion']))
    else:
        print("El equipo con ID {} no existe.")

# Función para mostrar un menú interactivo
def mostrar_menu():
    while True:
        print("\nMenú:")
        print("1. Agregar equipo")
        print("2. Agregar novedad")
        print("3. Buscar equipo")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1/2/3/4): ")

        if opcion == '1':
            id_equipo = input("Ingrese el ID del equipo: ")
            cargador = input("Ingrese el cargador: ")
            mouse = input("Ingrese el mouse: ")
            agregar_equipo(id_equipo, cargador, mouse)
        elif opcion == '2':
            id_equipo = input("Ingrese el ID del equipo al que desea agregar una novedad: ")
            fecha = input("Ingrese la fecha de la novedad: ")
            descripcion = input("Ingrese la descripción de la novedad: ")
            agregar_novedad(id_equipo, fecha, descripcion)
        elif opcion == '3':
            id_equipo = input("Ingrese el ID del equipo que desea buscar: ")
            buscar_equipo(id_equipo)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if _name_ == "_main_":
    mostrar_menu()