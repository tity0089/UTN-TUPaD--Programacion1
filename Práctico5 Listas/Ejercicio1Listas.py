#1) Crear una lista con las notas de 10 estudiantes•Mostrar la lista completa•Calcular y mostrar el promedio•Indicar la nota más alta y la más baja#

notas=[1,2,3,4,5,6,7,8,9,10]


total=sum(notas)
cant_alumnos=len(notas)
promedio=total/cant_alumnos

alta=max(notas)
baja=min(notas)

print(f"Notas:", notas)
print(f"El promedio es:{promedio}")
print(f"La nota más alta es:{alta}")
print(f"La nota más baja es: {baja}")