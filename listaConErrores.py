#1 punto (Crear listas y llenarlas solicitando datos al usuario por el teclado)
aprendices = []
edades = []

for i in range(3):
    nombres = input("Ingrese el nombre y apellido del aprendiz: ")
    edad = int(input("Ingrese la edad del aprendiz: "))
    aprendices.append(nombres)
    edades.append(edad)

#2 punto (imprimir las listas)
print("Lista de los aprendices: ", aprendices)
print("Lista de las edades de los aprendices: ", edades)

#3 punto (Muestre aprendiz con la mayor edad)
apeMayorEdad = edades.index(max(edades))  #el index se utiliza para la posicion 
aprendizMayorDeEdad = aprendices[apeMayorEdad]
print("El aprendiz con mayor edad de todos es: ", aprendizMayorDeEdad)

#4 punto (Inserte el nombre de la instructora en la posicion 1)
instru = "Adriana Lucia Rincon Forero"
aprendices.insert(1, instru)
print("Se a añadido a la lista el nombre de la instructora: ", instru)

#5 punto (Cuantos aprendices tienen 18 años)
aprendicesCon18Años = edades.count(18)
print("Hay", aprendicesCon18Años, "aprendices con 18 años")

#6 punto (Agregue un aprendiz al final de la lista)
nuevoAprendiz = "Bella Higinio"
aprendices.append(nuevoAprendiz)
print("nuevo aprendiz ingresado a la lista: ", nuevoAprendiz)

#7 punto (Borre el nombre de la instru de la lista)
aprendices.remove(instru)
print("El dato", instru, "se a eliminado correctamente")

#8 punto (Indique un dato a buscar en la lista de aprendices)
buscarDatoAprendiz = input("Ingrese un dato para buscar en la lista de aprendices: ")
if buscarDatoAprendiz in aprendices:
    print(buscarDatoAprendiz, "Si se encuentra en la lista de los aprendices.")
else:
    print(buscarDatoAprendiz, "No se encuentra en la lista de los aprendices.")

#9 punto (Muestre los primeros 10 aprendices de la lista)
print("Los primeros 10 aprendices en la lista son: ", aprendices[:10])

#10 punto (Muestre los ultimos 10 aprendices de la lista)
print("Los ultimos 10 aprendices en la lista son: ", aprendices[-10:])

#11 punto (Muestre del elemento 10 al elemento 20)
print("Los elementos del 10 al 20 en la lista son: ", aprendices[9:19])