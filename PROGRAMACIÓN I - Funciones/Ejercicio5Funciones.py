#Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función

def segundos_a_horas(segundos):
    hora=float(segundos/3600)

    return f"{hora} hora/s"

segundos=int(input("Ingrese la cantidad de segundos:"))


print(segundos_a_horas(segundos))
