#prog q permita ingresar 100 números enteros. Luego, el debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son neg y cuántos son positivos#

# Programa para contar pares, impares, positivos y negativos

cantidad = 100 # Puedes cambiarlo por un número menor para probar

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i + 1}: "))

    # Contar pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Contar positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\n--- Resultados ---")
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)