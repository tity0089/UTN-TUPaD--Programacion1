#Crear una matriz con las notas de 5 estudiantes en 3 materias•Mostrar el promedio de cada estudiante•Mostrar el promedio de cada materia


notas = [
    ["juan", 4, 8, 10],
    ["pedro", 10, 7, 6],
    ["ignacio", 7, 7, 10],
    ["lucas", 2, 8, 7],
    ["marcelo", 10, 7, 7]
]

# Promedio de cada estudiante
print("Promedio de cada estudiante:")
for estudiante in notas:
    nombre = estudiante[0]
    # sum() toma todos los valores de las notas y los suma
    # estudiante[1:] toma todos los elementos menos el nombre
    promedio_estudiante = sum(estudiante[1:]) / (len(estudiante) - 1)
    print(f"{nombre}: {promedio_estudiante:.2f}")

# Promedio de cada materia
print("\nPromedio de cada materia:")
cant_estudiantes = len(notas)
cant_materias = len(notas[0]) - 1  # restamos el nombre

for i in range(1, cant_materias + 1):
    suma_materia = 0
    for estudiante in notas:
        suma_materia += estudiante[i]
    promedio_materia = suma_materia / cant_estudiantes
    print(f"Materia {i}: {promedio_materia:.2f}")