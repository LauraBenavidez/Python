# Definición de la clase Fruta
class Fruta:
    def sabor(self):
        # Método sabor de la clase Fruta (método abstracto).
        pass

# Definición de la clase Manzana que hereda de la clase Fruta
class Manzana(Fruta):
    def sabor(self):
        # Implementación del método sabor para una manzana.
        return "Dulce"

# Definición de la clase Limon que hereda de la clase Fruta
class Limon(Fruta):
    def sabor(self):
        # Implementación del método sabor para un limón.
        return "Ácido"

# Uso de polimorfismo
# Creación de instancias de Manzana y Limon
frutas = [Manzana(), Limon()]

# Iteración sobre la lista de frutas e impresión del sabor de cada fruta
for fruta in frutas:
    print(f"La fruta tiene un sabor {fruta.sabor()}.")

# Ejemplo 2

# Definición de la clase InstrumentoMusical
class InstrumentoMusical:
    def tocar(self):
        # Método tocar de la clase InstrumentoMusical (método abstracto).
        pass

# Definición de la clase Guitarra que hereda de la clase InstrumentoMusical
class Guitarra(InstrumentoMusical):
    def tocar(self):
        # Implementación del método tocar para una guitarra.
        return "Suena la guitarra."

# Definición de la clase Piano que hereda de la clase InstrumentoMusical
class Piano(InstrumentoMusical):
    def tocar(self):
        # Implementación del método tocar para un piano.
        return "Suena el piano."

# Uso de polimorfismo
# Creación de instancias de Guitarra y Piano
instrumentos = [Guitarra(), Piano()]

# Iteración sobre la lista de instrumentos e impresión del sonido de cada instrumento
for instrumento in instrumentos:
    print(instrumento.tocar())
