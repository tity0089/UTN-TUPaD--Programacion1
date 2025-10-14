#Generar una lista con 15 números enteros al azar entre 1 y 100•Crear una lista con los pares y otra con los impares•Mostrar cuántos números tiene cada lista
import random
nros_enteros=[]
impares=[]
pares=[]

for i in range (15):
    numero=random.randint(1,100)
    nros_enteros.append(numero)
    if numero%2==0:
        pares.append(numero)
    else:
        impares.append(numero)



print(f"La lista de números es:{nros_enteros}")
print(f"Números pares:{pares}")
print(f"Números impares:{impares}")

pares=(len(pares))
impares=(len(impares))
print(f"Cantidad de números pares:{pares}")
print(f"Cantidad de números impares:{impares}")