# Crear una lista vacía llamada "aprendices" y otra llamada "edades"
aprendices = []
edades = []

# Llenar las listas solicitando datos por teclado
numeroAprendices = int(input("Cuántos aprendices deseas ingresar: "))
for i in range(numeroAprendices):
    nombre = input(f"Ingrese el nombre del aprendiz {i + 1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas
print("Lista de Aprendices:", aprendices)
print("Lista de Edades:", edades)

# Encontrar el aprendiz con la mayor edad
indimayorEdad = edades.index(max(edades))
print(f"El aprendiz con la mayor edad es {aprendices[indimayorEdad]} con {max(edades)} años.")

# Insertar el nombre de la instructora en la posición 1
nombreInstructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombreInstructora)

# Contar cuántos aprendices tienen 18 años
conteoEdad = edades.count(18)
print(f"Hay {conteoEdad} aprendices con 18 años.")

# Agregar un aprendiz "x" al final de la lista
aprendices.append("Leonardo")

# Borrar el nombre de la instructora de la lista
if nombreInstructora in aprendices:
    aprendices.remove(nombreInstructora)

# Indicar un dato a buscar en la lista de aprendices
datoBuscar = input("Ingrese un dato a buscar en la lista de aprendices: ")
if datoBuscar in aprendices:
    print(f"{datoBuscar} se encuentra en la lista de aprendices.")
else:
    respuesta=input(f"{datoBuscar} no se encuentra en la lista de aprendices. ¿Deseas agregarlo? (Si/No):")
    if respuesta=="Si":
        aprendices.append(datoBuscar)
        print(f"Se ha agregado {datoBuscar} a la lista de aprendices.")
    else:
     print(f"{datoBuscar} no se agrego a la lista de aprendices.")


# Mostrar los primeros 10 aprendices de la lista
print("Los primeros 10 aprendices son:", aprendices[:10])

# Mostrar los 10 últimos aprendices de la lista
print("Los 10 últimos aprendices son:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Del elemento 10 al elemento 20:", aprendices[9:19])