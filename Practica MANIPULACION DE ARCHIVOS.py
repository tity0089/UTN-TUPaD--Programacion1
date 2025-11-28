productos=open ("productos.txt","w")
productos.write ("Producto: Lapicera, Precio: $120, Cantidad: 40 u \n")
productos.write ("Producto: Cuaderno, Precio: $450, Cantidad: 25 u \n")
productos.write("Producto: Regla, Precio: $150, Cantidad: 10 u \n")

productos.close()


#Leer y mostrar productos

with open("productos.txt","r") as archivo:
    print(archivo.read())


#Procesar con strip y split

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        print(linea.strip().split(","))

productos_lista=[]

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        partes= linea.strip().split(",")

        nombre = partes[0].split(":")[1].strip()
        precio = partes[1].split("$")[1].strip()
        cantidad = partes[2].split(":")[1].strip()


        producto_diccionario = {"Nombre": nombre,
                                "Precio": precio,
                                "Cantidad": cantidad }

        productos_lista.append(producto_diccionario)





#Agregar productos desde teclado sin borrar contenido existente

with open ("productos.txt","a") as archivo:
    nuevo=input("Ingrese nuevo producto:")
    precio=input("Ingrese el precio:")
    cantidad=input("Ingrese la cantidad:")

    archivo.write(f"Producto:{nuevo}, Precio: ${precio}, Cantidad: {cantidad} u\n") 

productos_lista = []

with open ("productos.txt","r") as archivo:
    for linea in archivo:
        partes= linea.strip().split(",")

        nombre = partes[0].split(":")[1].strip()
        precio = partes[1].split("$")[1].strip()
        cantidad = partes[2].split(":")[1].strip()

        producto_diccionario = {
            "Nombre": nombre,
            "Precio": precio,
            "Cantidad": cantidad        }

        productos_lista.append(producto_diccionario)


#Buscar producto

producto_buscado = input("Ingrese el producto buscado:")

encontrado = False

for p in productos_lista:
    if p ["Nombre"].lower()== producto_buscado.lower():
        print(f"Producto:{p ['Nombre']}")
        print(f"Precio: ${p ['Precio']}")
        print(f"Cantidad:{p ['Cantidad']}")
        encontrado = True
        break
    
if not encontrado:
    print("Producto no encontrado")        

