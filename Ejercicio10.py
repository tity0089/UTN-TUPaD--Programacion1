#Escribe un programa que invierta el orden de los dígitos de un número ingresado. Ej.: si el usuario ingresa 547, el programa debe mostrar 745.

# Programa que invierte los dígitos de un número

numero = input("Ingrese un número entero: ")

invertido = numero[::-1]  # Invierte la cadena

print("El número invertido es:", invertido)