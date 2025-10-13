#ngresar 100 números enteros y calcule la media de esos valores

# Programa para calcular la media de varios números

cantidad = 2  # Cambia este número para probar con menos datos

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    suma += numero

media = suma / cantidad

print("\n--- Resultado ---")
print("La media de los números ingresados es:", media)