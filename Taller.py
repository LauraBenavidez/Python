# Crear una lista vacía llamada "aprendices" y otra llamada "edades"
aprendices = []
edades = []

# Llenar las listas solicitando datos por teclado
num_aprendices = int(input("Cuántos aprendices deseas ingresar: "))
for i in range(num_aprendices):
    nombre = input(f"Ingrese el nombre del aprendiz {i + 1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas
print("Lista de Aprendices:", aprendices)
print("Lista de Edades:", edades)

# Encontrar el aprendiz con la mayor edad
indice_mayor_edad = edades.index(max(edades))
print(f"El aprendiz con la mayor edad es {aprendices[indice_mayor_edad]} con {max(edades)} años.")

# Insertar el nombre de la instructora en la posición 1
nombre_instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombre_instructora)

# Contar cuántos aprendices tienen 18 años
conteo_18_anios = edades.count(18)
print(f"Hay {conteo_18_anios} aprendices con 18 años.")

# Agregar un aprendiz "x" al final de la lista
nuevo_aprendiz = "AprendizX"
aprendices.append(nuevo_aprendiz)

# Borrar el nombre de la instructora de la lista
if nombre_instructora in aprendices:
    aprendices.remove(nombre_instructora)

# Indicar un dato a buscar en la lista de aprendices
dato_a_buscar = input("Ingrese un dato a buscar en la lista de aprendices: ")
if dato_a_buscar in aprendices:
    print(f"{dato_a_buscar} se encuentra en la lista de aprendices.")
else:
    print(f"{dato_a_buscar} no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista
print("Los primeros 10 aprendices son:", aprendices[:10])

# Mostrar los 10 últimos aprendices de la lista
print("Los 10 últimos aprendices son:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Del elemento 10 al elemento 20:", aprendices[9:19])