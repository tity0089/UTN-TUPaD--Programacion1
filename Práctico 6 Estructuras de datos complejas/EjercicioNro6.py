#Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
#Luego, mostrá el promedio de cada alumno.

notas={
    "Laura":(8,9,7),
    "Juan":(4,8,6),
    "Ana":(10,9,8)
}

print("Promedio:")

for alumno,notas in notas.items():
    promedio=sum(notas)/len(notas)
    print(f"El promedio de {alumno} es:{promedio}")