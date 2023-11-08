# Declaración de un diccionario vacío
diccionario = {}

# Diccionario inicializado con valores
Diccionario = {'nombre': 'Sandra', 'edad': 44}

# Acceder a los elementos de un diccionario
print(Diccionario['nombre'])  # Imprime el valor asociado a la clave 'nombre'
print(Diccionario.get('nombre', 'No existe'))  # Imprime el valor de 'nombre' o 'No existe' si la clave no está

# Agregar datos al diccionario después de creado
calificaciones = {'nombre': 'Sandra', 'notafinal': 5.0}
calificaciones.update({"Rosa": 3.7, "German": 4.8})  # Agrega nuevos elementos al diccionario

# Técnicas de iteración
for clave, valor in calificaciones.items():
    print(clave, valor)  # Itera sobre las claves y valores del diccionario e imprime cada par

# Técnicas de iterar los diccionarios
print("Técnicas por clave")
for clave in calificaciones.keys():
    print(clave)  # Itera sobre las claves del diccionario e imprime cada clave

print("Iterar por valor")
for valor in calificaciones.values():
    print(valor)  # Itera sobre los valores del diccionario e imprime cada valor

# Utilizando la función zip
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

for nombre, edad in zip(nombres, edades):
    print(f'Tu nombre es {nombre} y tu edad {edad}.')  # Combina las listas 'nombres' y 'edades' e imprime los pares

# Operaciones sobre los diccionarios
dicaleatorio = {x: x**2 for x in (2, 4, 6)}
print(dicaleatorio)  # Crea un nuevo diccionario con valores al cuadrado

# Imprimir números en reversa
print("Números en reversa")
for i in reversed(range(1, 10, 2)):
    print(i)  # Imprime números en orden inverso

# Borrar un elemento del diccionario
del calificaciones['Rosa']  # Elimina la clave 'Rosa' del diccionario
for clave, valor in calificaciones.items():
    print(clave, valor)  # Imprime el diccionario actualizado después de la eliminación
