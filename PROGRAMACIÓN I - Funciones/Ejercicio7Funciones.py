#Crear una función llamada operaciones_basicas(a, b) que reciba 2 num como parámetros y devuelva una tupla 
# con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
#Mostrar los resultados de forma clara.

def operaciones_basicas(a,b):

    suma= a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    print (f"Suma= {suma}, resta= {resta}, división= {division}, multiplicación= {multiplicacion}")
    return (suma,resta,multiplicacion,division)

nro1=int(input("Ingrese el primer número:"))
nro2=int(input("Ingrese el segundo número:"))

print(operaciones_basicas(nro1,nro2))