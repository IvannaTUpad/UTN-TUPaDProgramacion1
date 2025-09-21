
# 1) Crear una lista con las notas de 10 estudiantes.
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja.

notas = [4, 4, 7, 7, 8, 9, 9, 10, 5, 5]
print(notas)

for n in notas:
    print(n)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)

nota_mas_alta = max(notas)
nota_mas_baja = min(notas)

print("La nota más alta es:", nota_mas_alta)
print("La nota más baja es:", nota_mas_baja)



# 2) Pedir al usuario que cargue 5 productos en una lista.
# • Mostrar la lista ordenada alfabéticamente.
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []
for i in range(5):
    producto = input(f"Cargue un producto: ").lower()
    productos.append(producto)

lista_ordenada = sorted(productos)
print("Lista ordenada:", lista_ordenada)

producto_eliminado = input("¿Qué producto desea eliminar?: ").lower()
if producto_eliminado in lista_ordenada:
    lista_ordenada.remove(producto_eliminado)
    print("Lista actualizada:", lista_ordenada)
else:
    print("Ese producto no está en la lista.")


# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

import random

numeros = []
for i in range(15):
    numero = random.randint(1, 100)
    numeros.append(numero)

print("Números generados:", numeros)

pares = []
impares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Cantidad de pares:", len(pares))
print("Números impares:", impares)
print("Cantidad de impares:", len(impares))


# 4) Dada una lista con valores repetidos:
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado.

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetir = []

for dato in datos:
    if dato not in datos_sin_repetir:
        datos_sin_repetir.append(dato)

print("Lista sin repetir:", datos_sin_repetir)


# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

estudiantes = ["Ana", "Luis", "María", "Carlos", "Sofía", "Pedro", "Lucía", "Juan"]
print("Estudiantes presentes:", estudiantes)

accion = input("¿Desea agregar o eliminar un estudiante? (agregar/eliminar): ").lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("Ese estudiante no está en la lista.")
else:
    print("Acción no reconocida.")

print("Lista actualizada:", estudiantes)


# 6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

lista_num = [1, 2, 3, 4, 5, 6, 7]
lista_rotada = [lista_num[-1]] + lista_num[:6]
print("Lista rotada:", lista_rotada)


# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

lista_anidada = [
    [20, 30],
    [15, 25],
    [10, 18],
    [18, 35],
    [10, 25],
    [11, 32],
    [12, 27]
]

minimas = [fila[0] for fila in lista_anidada]
maximas = [fila[1] for fila in lista_anidada]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)

print("Promedio mínimas:", promedio_min)
print("Promedio máximas:", promedio_max)

amplitud = [fila[1] - fila[0] for fila in lista_anidada]
dia_mayor_temp = amplitud.index(max(amplitud)) + 1
print("El día con mayor amplitud térmica es:", dia_mayor_temp)


# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

notas_estud = [
    [5, 6, 7],
    [7, 8, 8],
    [9, 6, 7],
    [10, 9, 9],
    [6, 8, 8]
]

# Promedio por estudiante
for i in range(5):
    suma = 0
    for j in range(3):
        suma += notas_estud[i][j]
    promedio = suma / 3
    print(f"Estudiante {i+1}: {promedio:.2f}")

# Promedio por materia
for j in range(3):
    suma = 0
    for i in range(5):
        suma += notas_estud[i][j]
    promedio = suma / 5
    print(f"Promedio materia {j+1}: {promedio:.2f}")


# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.



tablero = [["-" for _ in range(3)] for _ in range(3)]

# Mostrar tablero inicial
for i in range(3):
    for j in range(3):
        print(tablero[i][j], end=" ")
    print()

turno = 0
jugadores = ["X", "O"]

while turno < 9:
    jugador = jugadores[turno % 2]
    print(f"\nTurno del jugador {jugador}")

    # Mostrar posiciones libres
    print("Posiciones libres:")
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "-":
                print(f"({i}, {j})", end=" ")
    print()

    fila = int(input("Ingrese fila (0-2): "))
    columna = int(input("Ingrese columna (0-2): "))

    # Validar que la posición esté dentro del tablero
    if fila < 0 or fila > 2 or columna < 0 or columna > 2:
        print("Posición fuera del tablero. Intente de nuevo.")
        continue

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador

        # Mostrar tablero actualizado
        for i in range(3):
            for j in range(3):
                print(tablero[i][j], end=" ")
            print()

        turno += 1
    else:
        print("Casilla ocupada. Intente de nuevo.")




# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 20, 30, 40, 50, 60, 70],
    [15, 25, 35, 45, 55, 65, 75],
    [12, 22, 32, 42, 52, 62, 72],
    [18, 28, 38, 48, 58, 68, 78]
]

print("Total vendido por cada producto:")
for i in range(len(ventas)):
    total = sum(ventas[i])
    print(f"Producto {i+1}: {total}")

dia_mayor = 0
mayor_total = 0
for j in range(7):
    total_dia = sum(ventas[i][j] for i in range(4))
    if total_dia > mayor_total:
        mayor_total = total_dia
        dia_mayor = j
print(f"\nDía con mayores ventas totales: Día {dia_mayor+1} con {mayor_total} ventas")

producto_mayor = 0
mayor_ventas = 0
for i in range(4):
    total = sum(ventas[i])
    if total > mayor_ventas:
        mayor_ventas = total
        producto_mayor = i
print(f"Producto más vendido en la semana: Producto {producto_mayor+1} con {mayor_ventas} ventas")
