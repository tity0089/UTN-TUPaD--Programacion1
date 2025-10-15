#Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
#Permití consultar qué actividad hay en cierto día y hora

agenda={
    ("Lunes","10:00"): "Doctor",
    ("Martes","08:00"): "Dentista",
    ("Miercoles","09:00"):"Psicologa"
}

dia=input("Ingrese el día a consultar:").capitalize()
hora=input("Ingrese el horario(00:00):")

if (dia,hora) in agenda:
       print(f"El {dia} a las {hora} : {agenda [(dia,hora)]}")
else:
       print("Disponible.")