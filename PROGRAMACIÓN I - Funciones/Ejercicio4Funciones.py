#Crear dos funciones:calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. 
# calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def calcular_area_circulo(radio):
    pi=3.1416
    area=pi*(radio**2)
    return f"El área del círculo es {area}"

radio=float(input("Ingrese el radio del círculo:"))

def calcular_perimetro_circulo(radio):
    pi=3.1416
    perimetro=2*pi*radio
    return f"El perímetro del círculo es {perimetro}"

print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

