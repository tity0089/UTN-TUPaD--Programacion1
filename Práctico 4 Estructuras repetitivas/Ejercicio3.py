#programa que sume todos los nros enteros comprendidos entre2valores,excluyendo esos dos valores
valor1=int(input("Ingresa un número:"))
valor2=int(input("Ingresa el segundo número:"))

suma=sum(range(valor1+1,valor2+1))
print(f"La suma es:", suma)



