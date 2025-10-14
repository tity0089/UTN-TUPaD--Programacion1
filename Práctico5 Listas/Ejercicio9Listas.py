#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.#
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".#
#• Mostrar el tablero después de cada jugada.#

tablero = [["-", "-", "-"],
           ["-", "-", "-"],
           ["-", "-", "-"]]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

mostrar_tablero()

# máximo 9 turnos
for turno in range(9):
    jugador = "X" if turno % 2 == 0 else "O"
    print(f"Turno del jugador {jugador}")

    # loop para pedir posición hasta que sea válida
    while True:
        try:
            fila = int(input("Ingrese número de fila (0, 1 o 2): "))
            columna = int(input("Ingrese número de columna (0, 1 o 2): "))
        except ValueError:
            print("Por favor ingrese números enteros.")
            continue  # esto está dentro del while => válido

        
        if not (0 <= fila <= 2 and 0 <= columna <= 2):
            print("Número fuera de rango. Intente de nuevo.")
            continue

        
        if tablero[fila][columna] != "-":
            print("Casillero ocupado. Elija otro.")
            continue

        
        tablero[fila][columna] = jugador
        break 

    mostrar_tablero()


