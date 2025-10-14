#Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función

def celsius_a_fahrenheit(celsius):
    fahrenheit=(celsius*1.8)+32

    print(f"{fahrenheit} fahrenheit")
    return (fahrenheit)

celsius=float(input("Ingrese la temperatura:"))    

print(celsius_a_fahrenheit(celsius))