#Diccionarios:

# Un diccionario en Python es una estructura de datos que almacena pares clave-valor. Se puede crear un diccionario vacío con llaves o inicializado con valores.
# Puedes acceder a los elementos de un diccionario utilizando la notación de corchetes o el método .get().
# Para agregar datos a un diccionario después de crearlo, puedes utilizar el método .update().
# Puedes iterar a través de un diccionario utilizando técnicas como for i, j in diccionario.items(), for i in diccionario.keys(), y for j in diccionario.values().
# Puedes realizar operaciones en un diccionario, como crear uno nuevo utilizando una comprensión de diccionario o imprimir números en orden inverso. También, puedes borrar elementos de un diccionario con la declaración del.
# Los diccionarios son una estructura de almacenamiento de pares clave-valor.

#Funciones:

# Las funciones en Python permiten agrupar código y evitar la repetición.
# Una función se define con la palabra clave def seguida del nombre de la función y paréntesis.
# Las funciones pueden tener parámetros que se pasan como argumentos cuando se llama a la función.
# Las funciones pueden tener un valor de retorno utilizando la palabra clave return.
# Se pueden utilizar parámetros por defecto en una función para proporcionar valores predeterminados a los argumentos.
# Para evitar problemas con parámetros mutables, es recomendable utilizar una lista o diccionario vacío como valor por defecto en lugar de un valor mutable directo.
# Las funciones anónimas, también conocidas como funciones lambda, son funciones sin nombre que se definen en una sola línea y pueden recibir cualquier número de parámetros.
# Aquí hay algunos ejemplos de cómo definir una función en Python:
# Este resumen proporciona una visión general de los conceptos presentados en el código. Los ejemplos ayudan a ilustrar cómo trabajar con diccionarios y funciones en Python.
#EJEMPLOS
# Crear un diccionario vacío e inicializado con valores
diccionario_vacio = {}
diccionario = {'nombre': 'Sandra', 'edad': 44}

# Acceder a los elementos de un diccionario
print(diccionario['nombre'])
print(diccionario.get('nombre', 'No existe'))

# Agregar datos a un diccionario después de creado
calificaciones = {}
calificaciones.update({"Rosa": 3.7, "German": 4.8})

# Iterar a través de un diccionario
calificaciones = {
    'Sandra': 5.0,
    'Adriana': 5.0,
    'Mauricio': 4.5,
    'Jose': 2.5
}

for nombre, nota in calificaciones.items():
    print(nombre, nota)

# Operaciones en diccionarios
dicaleatorio = {x: x ** 2 for x in (2, 4, 6)}
print(dicaleatorio)

#FUNCIONES 
# Definir una función
def saludar():
    print("¡Hola!")

def retornarnumero():
    return 1

# Llamar a funciones
saludar()
resultado = retornarnumero()

if resultado == 1:
    print("La función devolvió un uno")
else:
    print("La función no devolvió un uno")

# Funciones con parámetros
def raiz(value):
    return value ** (1/2)

print(f'La raíz cuadrada es: {raiz(4)}')

def validarsiexiste(obj):
    if obj:
        print(f"{obj} es verdadero")
    else:
        print(f"{obj} es falso")

validarsiexiste(1)

# Funciones con parámetros posicionales
def compra(marca, cantidad, valor):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor_total': valor * cantidad
    }

print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')

# Funciones con parámetros nominales
def compra(marca, cantidad, valor):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor_total': valor * cantidad
    }

print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')

# Parámetros por defecto
def compra(marca, cantidad, valor=2500000):
    return {
        'marca': marca,
        'cantidad': cantidad,
        'valor_total': valor * cantidad
    }

print(f'Lo comprado fue: {compra("AMD", 3)}')

# Funciones anónimas (lambda)
numero_palabras = lambda texto: len(texto.strip().split())
print(numero_palabras("Hola, esto es una prueba con lambda"))

operador_and = lambda x, y: x & y

for i in range(2):
    for j in range(2):
        print(f"{i} & {j} = {operador_and(i, j)}")
