#solicite al usuario un nro entero y determine la cantidad de dígitos que contiene.
entrada_usuario = input("Introduce un número entero: ")

numero_str = entrada_usuario.strip()


if numero_str.isdigit():

    cantidad_digitos = len(numero_str)
    print(f"El número {numero_str} tiene {cantidad_digitos} dígitos.")
else:
    print("Entrada no válida. Por favor, introduce un número entero válido.")