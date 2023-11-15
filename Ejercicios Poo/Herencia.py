# Definición de la clase Animal
class Animal:
    def __init__(self, nombre):
        # Constructor (__init__) que inicializa el atributo nombre.
        self.nombre = nombre

    def hacerSonido(self):
        # Método hacer_sonido de la clase Animal (método abstracto).
        pass

# Definición de la clase Perico que hereda de la clase Animal
class Perico(Animal):
    def hacerSonido(self):
        # Implementación del método hacer_sonido para un perico.
        return f"{self.nombre} dice: ¡Hola, soy un perico!"

# Definición de la clase Gato que hereda de la clase Animal
class Gato(Animal):
    def hacerSonido(self):
        # Implementación del método hacer_sonido para un gato.
        return f"{self.nombre} dice: Miau, miau."

# Uso de la herencia
# Creación de instancias de Perico y Gato
perico1 = Perico("Paco")
gato1 = Gato("Tom")

# Llamada al método hacer_sonido en las instancias y se imprime el resultado
print(perico1.hacerSonido())
print(gato1.hacerSonido())

# Ejemplo 2

# Definición de la clase AnimalTerrestre
class AnimalTerrestre:
    def __init__(self, nombre):
        # Constructor (__init__) que inicializa el atributo nombre.
        self.nombre = nombre

    def moverse(self):
        # Método moverse de la clase AnimalTerrestre.
        print(f"{self.nombre} se mueve por tierra.")

# Definición de la clase Tortuga que hereda de la clase AnimalTerrestre
class Tortuga(AnimalTerrestre):
    def __init__(self, nombre, caparazon):
        # Constructor (__init__) que inicializa el atributo caparazon llamando al constructor de la clase base.
        super().__init__(nombre)
        self.caparazon = caparazon

    def protegerse(self):
        # Método propio de la clase Tortuga que imprime cómo se protege la tortuga.
        print(f"{self.nombre} se protege con su caparazón.")

# Uso de la herencia
# Creación de una instancia de la clase Tortuga
tortuga1 = Tortuga("Torty", "Duro")

# Llamada a los métodos moverse y protegerse en la instancia
tortuga1.moverse()
tortuga1.protegerse()