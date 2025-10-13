#debe adivinar un nro aleatorio entre 0 y 9. Al final mostrar cuántos intentos fueron necesarios para acertar el nro
cant_intentos=0

import random
numSecreto=random.randint(0,9)


for cant_intentos in range(9):

    print("Incorrecto.")
intento=int(input("Adivine el núumero secreto:"))    


if intento<numSecreto:
    print("Incorrecto")
elif intento>numSecreto:
    print("Incorrecto")    
else:
    print("Correcto")
    
if intento:numSecreto

cant_intentos=str(cant_intentos+1)
print("Cantidad de intentos:,{cant_intentos}")