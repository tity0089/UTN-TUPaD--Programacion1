#Escribí un programa que permita almacenar y consultar números telefónicos.
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#• Luego, pedí un nombre y mostrale el número asociado, si existe.


agenda={
    "Juan":"15456789",
    "Lucas":"1578941236",
    "Laura":"154785123",
    "Florencia":"1574129632",
    "Nicolas":"154582147"
}

contacto=input("Buscar contacto:")

if contacto in agenda:
    print(f"Número:{agenda[contacto]}")
else:
    print("No existe el contacto solicitado.")