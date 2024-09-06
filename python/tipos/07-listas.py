# listas
my_list = ["yonathan", 24, 24]
mi_otra_lista = [35, 64, 24, 21, 32]
print(my_list.count(24))  # cuenta cuantas veces se repite unelemento en una lista
print(mi_otra_lista)
print(len(mi_otra_lista))
mi_datos = ["yonathan", 24, 1.85]
print(mi_datos)

nombre, edad, altura = mi_datos
mi_datos.append("mi empresa")  # pa agregar un nuevo elemento al fdinal de la lista
mi_datos.insert(3, "athenas")  # pa agregar un nuevo elmento en la posicion que quieras
mi_datos.remove("athenas")  # pa eliminar un elemento de la lista
mi_datos.pop()  # elimina el ultimo itemm
del mi_datos[2]  # elimina el elemento del indice
mi_datos.reverse()
# sort() , ordena
print(mi_datos)
print(nombre)
