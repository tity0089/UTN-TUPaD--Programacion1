#calcule la suma de todos los números comprendidos entre 0 y un nro entero positivo indicado por el usuario
valor1=int(input("Ingresa un número:"))

suma=sum(range(0,valor1+1))
print(f"La suma es:", suma)
