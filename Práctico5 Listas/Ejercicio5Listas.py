#Crear una lista de 8 estudiantes presentes en clase•Preguntar si quiere agregar un nuevo estudiante o eliminar uno existente.•Mostrar la lista final actualizada.

presentes=["Juan","Pedro","Jose","Laura","Julia","Florencia","Nahir","Nicolas"]

agregar_presente=input("Agregar presente:")
eliminar_ausente=input("Ausentes:")

presentes.append(agregar_presente)
presentes.remove(eliminar_ausente)

print(presentes)    