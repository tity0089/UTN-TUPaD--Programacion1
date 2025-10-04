#Ejercicio1- Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("Hola mundo!")


#Ejercicio2-Saludo personalizado
nombre=input("Ingrese su nombre:")
print(f"Hola {nombre}!")


#Ejercicio3-Saludo con nombre completo, edad y residencia
nombre=input("Ingrese su nombre completo por favor:")
edad=int(input("Ingrese su edad:"))
residencia=input("Ingrese su lugar de residencia:")
print(f"Soy {nombre}, tengo {edad} años y vivo en {residencia}.")


#Ejercicio4- pida el radio de un círculo e imprima su área y perímetro.
nro=float(input("Ingrese el radio del círculo:"))
pi=3.14159265
area=(pi*nro)**2
perimetro=(2*pi)*nro
print(f"El área del círculo es {area} y el perímetro es {perimetro}")


#Ejercicio5-pida una cant de segundos e imprima a cuántas horas equivale

segundos=int(input("Ingrese los segundos:"))
hora=segundos/3600
print (f"{hora} hora/s.")



#6-pida al usuario un nro e imprima la tabla de multiplicar de dicho número


num=int(input("Ingrese un número (del 1 al 9):"))
one=num*1
two=num*2
three=num*3
four=num*4
five=num*5
six=num*6
sev=num*7
eig=num*8
nine=num*9

print(f"{num}x1={one}")
print(f"{num}x2={two}")
print(f"{num}x3={three}")
print(f"{num}x4={four}")
print(f"{num}x5={five}")
print(f"{num}x6={six}")
print(f"{num}x7={sev}")

print(f"{num}x8={eig}")
print(f"{num}x9={nine}")











#Ejercicio7- pida dos nros enteros distintos del 0 y muestre el resultado de sumarlos, dividirlos, multiplicarlos y restarlos
 nro1=int(input("Ingrese un número entero por favor:"))
nro2=int(input("Ingrese el segundo número entero:"))
suma=nro1+nro2
resta=nro1-nro2
div=nro1/nro2
mult=nro1*nro2
print(f"Suma:{suma}.")
print(f"Resta:{resta}.")
print(f"División:{div}.")
print(f"Multiplicación:{mult}.")


#Ejercicio8-


#pida altura y peso, calcule imc
altura=float(input("Ingrese su altura:"))
peso=float(input("Ingrese su peso:"))
imc=peso/altura**2
print(f"Su IMC es:{imc}")


#Ejercicio9-


#convertir de celsius a Fahrenheit 
celsius=float(input("Ingrese la temperatura:"))
Fahrenheit=celsius*9/5+32
print(f"La temperatura es {Fahrenheit} Fahrenheit")



#Ejercicio10-


#pide 3 nros y muestre el promedio de dichos nros
nro1=int(input("Ingrese el primer número:"))
nro2=int(input("Ingrese el segundo número:"))
nro3=int(input("Ingrese el tercer número:"))
promedio=(nro1+nro2+nro3)/3

print(f"El promedio es:{promedio}")