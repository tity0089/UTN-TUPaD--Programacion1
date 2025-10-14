#Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#Mostrar el total vendido por cada producto.
#Mostrar el día con mayores ventas totales.
#Indicar cuál fue el producto más vendido en la semana


# Creamos la matriz vacía (4 productos x 7 días)
ventas = []

# Cargar las ventas
for i in range(4):
    fila = []
    print(f"\nProducto {i+1}:")
    for j in range(7):
        venta = float(input(f"  Ingrese ventas del día {j+1}: "))
        fila.append(venta)
    ventas.append(fila)

# 1️⃣ Total vendido por cada producto
print("\n--- TOTAL VENDIDO POR CADA PRODUCTO ---")
totales_producto = []
for i in range(4):
    total = sum(ventas[i])
    totales_producto.append(total)
    print(f"Producto {i+1}: {total}")

# 2️⃣ Día con mayores ventas totales
print("\n--- DÍA CON MAYORES VENTAS ---")
totales_dia = []
for j in range(7):
    suma_dia = 0
    for i in range(4):
        suma_dia += ventas[i][j]
    totales_dia.append(suma_dia)
mayor_dia = max(totales_dia)
indice_dia = totales_dia.index(mayor_dia)
print(f"El día con mayores ventas fue el día {indice_dia+1} con un total de {mayor_dia}")

# 3️⃣ Producto más vendido en la semana
print("\n--- PRODUCTO MÁS VENDIDO ---")
mayor_producto = max(totales_producto)
indice_producto = totales_producto.index(mayor_producto)
print(f"El producto más vendido fue el Producto {indice_producto+1} con un total de {mayor_producto}")
