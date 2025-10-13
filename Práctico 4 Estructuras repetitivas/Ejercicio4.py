#programa que permita al usuario ingresar nros enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando ingre=
    

total_acumulado = 0

print("Introduce números enteros para sumarlos. Ingresa '0' para finalizar.")

# Usamos un bucle 'while True' para que el programa se ejecute indefinidamente
while True:
    try:
        # Solicitamos al usuario que ingrese un número
        numero_ingresado = int(input("Ingresa un número: "))
        
        # Si el número ingresado es 0, salimos del bucle
        if numero_ingresado == 0:
            break
        
        # Si no es 0, lo sumamos al total acumulado
        total_acumulado += numero_ingresado
    
    except ValueError:
        # Manejamos el caso en que el usuario no ingrese un número válido
        print("Entrada no válida. Por favor, ingresa un número entero.")

# Cuando el bucle termina, mostramos el resultado
print(f"El total acumulado es: {total_acumulado}")



