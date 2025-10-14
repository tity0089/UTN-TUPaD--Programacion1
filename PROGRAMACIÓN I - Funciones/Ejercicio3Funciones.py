#Crear una función llamada informacion_personal(nombre, apellido,edad, residencia)que reciba 4 parámetros e imprima: “Soy[nombre] [apellido],
#  tengo [edad] años y vivo en [residencia]”. 
# Pedir los datos al usuario y llamar a esta función con los valores ingresados
 
def informacion_personal(nombre,edad,residencia):
    return f"Soy {nombre},tengo {edad} años y vivo en {residencia}."

nombre=input("Ingresa tu nombre y apellido:")
edad=input("Ingresa tu edad:")
residencia=input("Lugar de residencia:")

print(informacion_personal(nombre,edad,residencia))