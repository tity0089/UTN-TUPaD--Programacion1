#cargue 5 productos en una lista•Mostrar la lista ordenada alfabéticamente•Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista=["pan","azucar","aceite","sal","huevos"]

alfabeticamente=sorted(lista)
print(alfabeticamente)

eliminar_producto=input("¿Que producto desea eliminar?")

if eliminar_producto in lista:
    lista.remove(eliminar_producto)
print("La lista actualizada es:", lista)    