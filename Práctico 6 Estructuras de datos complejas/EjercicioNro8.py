# Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# 1. Consultar el stock de un producto ingresado.
# 2. Agregar unidades al stock si el producto ya existe.
# 3. Agregar un nuevo producto si no existe.

productos = {
    "Alfajor": 20,
    "Azúcar": 25,
    "Yerba": 18,
    "Arroz": 10
}

producto = input("Ingrese el producto buscado: ").capitalize()

if producto in productos:
    print(f"El stock de {producto} es {productos[producto]} unidades.")
    agregar = input("¿Desea agregar más unidades? (s/n): ").lower()
    if agregar == "s":
        cantidad = int(input("Ingrese cuántas unidades desea agregar: "))
        productos[producto] += cantidad
        print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    print(f"{producto} no existe en el inventario.")
    nuevo = input("¿Desea agregarlo? (s/n): ").lower()
    if nuevo == "s":
        cantidad = int(input("Ingrese el stock inicial: "))
        productos[producto] = cantidad
        print(f"{producto} agregado con {cantidad} unidades.")

print("\nInventario actualizado:")
for nombre, stock in productos.items():
    print(f"{nombre}: {stock}")