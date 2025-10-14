#Crear una matriz (lista anidada)de 7x2 con las temperaturas mínimas y máximas de una semana•Calcular el promedio de las mínimas y máximas
# •Mostrar en qué día se registró la mayor amplitud térmica.#
matriz= [
    ["lunes",5,18],
    ["martes",7,19],
    ["miercoles",6,20],
    ["jueves",9,21],
    ["viernes",10,21],
    ["sabado",12,23],
    ["domingo",13,24]
    ]

minimo=0
maximo=0

for dia in matriz:
    minimo+=dia[1]
    maximo+=dia[2]

promedio_min=minimo/len(matriz)
promedio_max=maximo/len(matriz)

print(matriz)
print(f"Promedio de temperatura mínima:{promedio_min}")
print(f"Promedio de temperatura máxima:{promedio_max} ")

mayor_amplitud=0
dia_mayor=""

for dia in matriz:
    amplitud=dia[2]-dia[1]
    if amplitud>mayor_amplitud:
        mayor_amplitud=amplitud
        dia_mayor=dia[0]
print(f"El día con mayor amplitud térmica fue {dia_mayor}")        