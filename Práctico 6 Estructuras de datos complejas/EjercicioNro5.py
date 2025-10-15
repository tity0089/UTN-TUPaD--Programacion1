#Solicita al usuario una frase e imprime:
#• Las palabras únicas (usando un set).
#• Un diccionario con la cantidad de veces que aparece cada palabra.

frase=input("Ingrese una frase:")

palabras=frase.lower().split()
palabras_unicas=set(palabras)
frecuencia={}

for palabras in palabras:
    frecuencia[palabras]=frecuencia.get(palabras,0)+1

    print(f"Palabras únicas:", palabras_unicas)
    print(frecuencia)