#Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
#y Parcial 2:
#• Mostrá los que aprobaron ambos parciales.
#• Mostrá los que aprobaron solo uno de los dos.
#• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1={"Laura",
    "Juan","Ana"}
parcial_2={"Pablo","Andres","Laura","Ana"}

ambos_aprobados=parcial_1 & parcial_2
print(f"Aprobados en ambos parciales:", ambos_aprobados)

solo_1=parcial_1 ^ parcial_2
print("Aprobados en un parcial:", solo_1)

total= parcial_1| parcial_2
print("Aprobaron al menos un parcial:", total)

   


    