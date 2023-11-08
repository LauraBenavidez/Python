# Definición de una función llamada "saludar" que imprime "saludo"
def saludar():
    print("saludo")

# Definición de una función llamada "retornarnumero" que devuelve 1
def retornarnumero():
    return 1

# Llamada a la función "saludar" (imprime "saludo" pero no se captura el valor de retorno)
saludar()

# Llamada a la función "retornarnumero" y se verifica si devuelve 1
if retornarnumero() == 1:
    print("devolvió un uno")
else:
    print("No devolvió un uno")

# Definición de una función llamada "raiz" que calcula la raíz cuadrada de un número y la imprime
def raiz(value):
    return value ** (1/2)

print(f'La raíz cuadrada es: {raiz(4)}')

# Definición de una función llamada "validarsiexiste" que verifica si un objeto es verdadero o falso
def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

# Llamada a "validarsiexiste" con el argumento 1 (imprime "1 is True")
validarsiexiste(1)

# Definición de una función llamada "compra" con parámetros marca, cantidad y valor
# Retorna un diccionario con información sobre una compra
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Llamada a "compra" con parámetros posicionales
print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')

# Llamada a "compra" con parámetros nominales
print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')

# Definición de una función llamada "compra" con un valor por defecto para "valor"
# Retorna un diccionario con información sobre una compra
def compra(marca, cantidad, valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Llamada a "compra" con un solo argumento (se utiliza el valor por defecto para "valor")
print(f'Lo comprado fue: {compra("AMD", 3)}')

# Definición de una función llamada "lista" que modifica una lista pasada como argumento
def lista(arg, result=[]):
    result.append(arg)
    print(result)

# Llamada a "lista" con un argumento y una lista vacía
lista('domingo', [])

# Ejercicio: Modificar la lista resultante con los días de la semana restantes
lista('lunes', [])  # Agrega 'lunes' a la lista
lista('martes', [])  # Agrega 'martes' a la lista
lista('miercoles', [])  # Agrega 'miercoles' a la lista
lista('jueves', [])  # Agrega 'jueves' a la lista
lista('viernes', [])  # Agrega 'viernes' a la lista

# Definición de una función llamada "listalimpia" que modifica una lista pasada como argumento de manera segura
def listalimpia(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

# Llamadas a "listalimpia" con argumentos (cada llamada crea una lista nueva)
listalimpia("a")  # Crea una lista con "a" y la imprime
listalimpia("b")  # Crea otra lista con "b" y la imprime
listalimpia("c")  # Crea una tercera lista con "c" y la imprime

# Funciones anónimas "lambda" - Ejemplo 1: contar palabras en una cadena
numero_palabras = lambda t: len(t.strip().split())
print(numero_palabras("hola, esto es una prueba con lambda"))  # Imprime la cantidad de palabras

# Funciones anónimas "lambda" - Ejemplo 2: operador lógico AND
operadorand = lambda x, y: x & y
for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operadorand(i, j)}")  # Imprime el resultado de la operación AND
