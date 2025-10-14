#Crear una función llamada calcular_promedio(a, b, c) que reciba 3 nros como parámetros y devuelva el promedio de ellos.
#solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a,b,c):
    promedio=(a+b+c)/3
    print (f"El promedio es: {promedio}")
    return (promedio)

a=int(input("Ingrese el primer número:"))
b=int(input("Ingrese el segundo número:"))
c=int(input("Ingrese el tercer número:"))

    
print(calcular_promedio(a,b,c))