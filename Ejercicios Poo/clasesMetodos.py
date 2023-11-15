# Definición de la clase Pelicula
class Pelicula:
    def __init__(self, titulo, director, duracion):
        # Constructor (__init__) que inicializa los atributos título, director, y duración.
        self.titulo = titulo
        self.director = director
        self.duracion = duracion

    def reproducir(self):
        # Método reproducir que imprime un mensaje al reproducir la película.
        print(f"Reproduciendo {self.titulo} dirigida por {self.director} ({self.duracion} minutos).")

# Creación de una instancia de la clase Pelicula
pelicula1 = Pelicula("El Padrino", "Francis Ford Coppola", 175)

# Llamada al método reproducir en la instancia
pelicula1.reproducir()


# Definición de la clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, carrera):
        # Constructor (__init__) que inicializa los atributos nombre, edad, y carrera.
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def estudiar(self):
        # Método estudiar que imprime un mensaje sobre el estudiante y su carrera.
        print(f"{self.nombre} está estudiando {self.carrera}.")

# Creación de una instancia de la clase Estudiante
estudiante1 = Estudiante("Ana", 20, "Ingeniería Informática")

# Llamada al método estudiar en la instancia
estudiante1.estudiar()
