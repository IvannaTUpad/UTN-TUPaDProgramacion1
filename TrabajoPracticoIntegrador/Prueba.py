# ========== VALIDACIONES ==========


import pycountry
import unicodedata

# Lista de continentes válidos
CONTINENTES_VALIDOS = ["América", "Europa", "Asia", "África", "Oceanía", "Antártida"]

# Quitar tildes de un texto
def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Normalizar y validar continente, devolviendo el nombre oficial si es válido
def normalizar_continente(entrada):
    entrada_normalizada = quitar_tildes(entrada.strip()).lower()
    continentes_normalizados = [quitar_tildes(c).lower() for c in CONTINENTES_VALIDOS]
    if entrada_normalizada in continentes_normalizados:
        indice = continentes_normalizados.index(entrada_normalizada)
        return CONTINENTES_VALIDOS[indice]
    return None

# Validar que el continente ingresado sea uno válido
def validar_nombre_continente(continente):
    return normalizar_continente(continente) is not None

# Validar que el nombre del país no esté vacío
def validar_nombre_pais(nombre):
    nombre = nombre.strip()
    return nombre != ""

# Validar que el país exista según pycountry
def validar_pais_existente(nombre):
    nombre = nombre.strip().lower()
    for pais in pycountry.countries:
        if pais.name.lower() == nombre:
            return True
    return False

# Validar población: entero positivo dentro de un rango razonable
def validar_poblacion(poblacion):
    poblacion = poblacion.strip()
    return poblacion.isdigit() and 1 <= int(poblacion) <= 2_000_000_000

# Validar superficie: entero positivo dentro de un rango razonable
def validar_superficie(superficie):
    superficie = superficie.strip()
    return superficie.isdigit() and 1 <= int(superficie) <= 20_000_000

# Verificar si un país ya existe en la lista
def existe_pais(paises, nombre):
    nombre = nombre.strip().lower()
    for pais in paises:
        if pais["nombre"].strip().lower() == nombre:
            return True
    return False

# Buscar países por coincidencia exacta o parcial
def buscar_paises_por_nombre(paises, termino):
    termino = termino.strip().lower()
    exactos = []
    parciales = []
    for pais in paises:
        nombre = pais["nombre"].strip().lower()
        if nombre == termino:
            exactos.append(pais)
        elif termino in nombre:
            parciales.append(pais)
    return exactos + parciales



# ========== FUNCIONES DE ORDENAMIENTO ==========

def obtener_nombre(pais):
    return pais.get("nombre", "").strip()

def obtener_poblacion(pais):
    return int(pais.get("poblacion", 0))

def obtener_superficie(pais):
    return int(pais.get("superficie", 0))



# ========== CARGA Y GUARDADO DE DATOS ==========
import csv
import os
ARCHIVO = "paises.csv"

def cargar_datos():
    paises = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

            # Validar encabezado
            if lector.fieldnames != ["nombre", "poblacion", "superficie", "continente"]:
                print("Formato de CSV incorrecto. Se esperaban las columnas: nombre, poblacion, superficie, continente.")
                return []

            for fila in lector:
                nombre = fila["nombre"].strip()
                poblacion = fila["poblacion"].strip()
                superficie = fila["superficie"].strip()
                continente = fila["continente"].strip()

                if (
                    validar_nombre_pais(nombre) and
                    validar_pais_existente(nombre) and
                    validar_poblacion(poblacion) and
                    validar_superficie(superficie) and
                    validar_nombre_continente(continente)
                ):
                    paises.append({
                        "nombre": nombre,
                        "poblacion": int(poblacion),
                        "superficie": int(superficie),
                        "continente": continente
                    })
                else:
                    print(f"País omitido por datos inválidos: {fila}")
    return paises


def guardar_datos(paises):
    with open(ARCHIVO, "w", newline='', encoding='utf-8') as archivo:
        campos = ["nombre", "poblacion", "superficie", "continente"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        for pais in paises:
            escritor.writerow(pais)

#---------------------------CASO 1:AGREGAR PAISES------------------------------------------------

def agregar_pais(paises):
    print("\n--- Agregar país ---")

    # Solicita y valida el nombre del país
    while True:
        nombre = input("Nombre del país (o 'salir' para cancelar): ").strip()
        if nombre.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if not validar_nombre_pais(nombre):
            print("Error: el nombre no puede estar vacío.")
            continue
        if not validar_pais_existente(nombre):
            print("Error: el país no existe según el estándar internacional.")
            continue
        if existe_pais(paises, nombre):
            print("Error: el país ya está en el listado.")
            return
        break  # El nombre es válido y no está duplicado

    # Solicita y valida la población
    while True:
        poblacion = input("Población total (o 'salir' para cancelar): ").strip()
        if poblacion.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_poblacion(poblacion):
            break
        print("Error: la población debe ser un número entero positivo entre 1 y 2.000.000.000.")

    # Solicita y valida la superficie
    while True:
        superficie = input("Superficie en km² (o 'salir' para cancelar): ").strip()
        if superficie.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_superficie(superficie):
            break
        print("Error: la superficie debe ser un número entero positivo entre 1 y 20.000.000.")

    # Solicita y valida el continente
    while True:
        continente = input("Continente (o 'salir' para cancelar): ").strip()
        if continente.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_nombre_continente(continente):
            continente = normalizar_continente(continente)
            break
        print("Error: el continente debe ser uno de los siguientes: América, Europa, Asia, África, Oceanía, Antártida.")

    # Agrega el país a la lista
    paises.append({
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente.capitalize()
    })
    print(f"País '{nombre}' agregado correctamente.")




# ===================== CASO 2: ACTUALIZAR DATOS =====================
def actualizar_datos_pais(paises):
    print("\n--- Actualizar datos de un país ---")

    # Solicita el nombre del país y permite cancelar
    while True:
        nombre = input("Ingrese el nombre del país a actualizar (o 'salir' para cancelar): ").strip()
        if nombre.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_nombre_pais(nombre):
            break
        print("Error: el nombre no puede estar vacío.")

    # Normaliza el nombre para buscar
    nombre_normalizado = quitar_tildes(nombre.lower())

    # Busca el país en la lista
    pais_encontrado = None
    for pais in paises:
        if quitar_tildes(pais["nombre"].lower()) == nombre_normalizado:
            pais_encontrado = pais
            break

    if not pais_encontrado:
        print("No se encontró un país con ese nombre.")
        return

    # Muestra datos actuales
    print(f"\nDatos actuales de '{pais_encontrado['nombre']}':")
    print(f"- Población: {pais_encontrado['poblacion']}")
    print(f"- Superficie: {pais_encontrado['superficie']} km²")

    # Actualiza población
    nueva_poblacion = input("Ingrese la nueva población: ").strip()
    if validar_poblacion(nueva_poblacion):
        pais_encontrado["poblacion"] = int(nueva_poblacion)
        print("✅ Población actualizada correctamente.")
    else:
        print("Error: población inválida.")

    # Actualiza superficie
    nueva_superficie = input("Ingrese la nueva superficie: ").strip()
    if validar_superficie(nueva_superficie):
        pais_encontrado["superficie"] = int(nueva_superficie)
        print(" Superficie actualizada correctamente.")
    else:
        print("Error: superficie inválida.")





# ===================== CASO 3: BUSCAR PAÍS POR NOMBRE =====================
def buscar_pais_por_nombre(paises):
    print("\n--- Buscar país por nombre ---")

    # Solicita el término de búsqueda y permite cancelar
    while True:
        termino = input("Ingrese el nombre o parte del nombre del país (o 'salir' para cancelar): ").strip()
        if termino.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if not validar_nombre_pais(termino):
            print("Error: el término de búsqueda no puede estar vacío.")
            continue
        break  # El término es válido

    # Normaliza el término de búsqueda
    termino_normalizado = quitar_tildes(termino.lower())

    # Busca coincidencias en la lista de países
    resultados = []
    for pais in paises:
        nombre_normalizado = quitar_tildes(pais["nombre"].strip().lower())
        if nombre_normalizado == termino_normalizado:
            resultados.append(pais)
        elif termino_normalizado in nombre_normalizado:
            resultados.append(pais)

    # Muestra los resultados encontrados
    if len(resultados) == 0:
        print("No se encontraron países que coincidan con ese nombre.")
    else:
        print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
        for pais in resultados:
            print(f"- {pais['nombre']} | Población: {pais['poblacion']} | Superficie: {pais['superficie']} km² | Continente: {pais['continente']}")



# ===================== CASO 4: FILTRAR POR CONTINENTE =====================
def filtrar_paises_por_continente(paises):
    print("\n--- Filtrar países por continente ---")

    # Solicita el nombre del continente y permite cancelar
    while True:
        continente = input("Ingrese el nombre del continente (o 'salir' para cancelar): ").strip()
        if continente.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_nombre_continente(continente):
            continente = normalizar_continente(continente)
            break
        print("Error: el continente debe ser uno de los siguientes: América, Europa, Asia, África, Oceanía, Antártida.")

    # Filtra los países que pertenecen al continente ingresado
    encontrados = []
    for pais in paises:
        if pais["continente"].strip() == continente:
            encontrados.append(pais)

    # Muestra los resultados encontrados
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} país(es) en {continente}:")
        for p in encontrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
    else:
        print("No se encontraron países en ese continente.")



# ===================== CASO 5: FILTRAR POR RANGO DE POBLACIÓN =====================

def filtrar_paises_por_rango_poblacion(paises):
    print("\n--- Filtrar países por rango de población ---")

    # Solicita y valida la población mínima
    while True:
        minimo = input("Población mínima (o 'salir' para cancelar): ").strip()
        if minimo.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_poblacion(minimo):
            minimo = int(minimo)
            break
        print("Error: la población mínima debe ser un número entero positivo entre 1 y 2.000.000.000.")

    # Solicita y valida la población máxima
    while True:
        maximo = input("Población máxima (o 'salir' para cancelar): ").strip()
        if maximo.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_poblacion(maximo):
            maximo = int(maximo)
            break
        print("Error: la población máxima debe ser un número entero positivo entre 1 y 2.000.000.000.")

    # Verifica que el mínimo no sea mayor que el máximo
    if minimo > maximo:
        print("Error: el valor mínimo no puede ser mayor que el máximo.")
        return

    # Filtra los países dentro del rango especificado
    encontrados = []
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            encontrados.append(pais)

    # Muestra los resultados encontrados
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} país(es) en ese rango:")
        for p in encontrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']}")
    else:
        print("No se encontraron países en ese rango.")
   


# ===================== CASO 6: FILTRAR POR RANGO DE SUPERFICIE =====================
def filtrar_paises_por_rango_superficie(paises):
    print("\n--- Filtrar países por rango de superficie ---")
    minimo = input("Superficie mínima: ").strip()
    maximo = input("Superficie máxima: ").strip()

    if not validar_superficie(minimo) or not validar_superficie(maximo):
        print("Error: ambos valores deben ser números enteros positivos.")
        return

    minimo = int(minimo)
    maximo = int(maximo)

    if minimo > maximo:
        print("Error: el mínimo no puede ser mayor que el máximo.")
        return

    encontrados = []
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            encontrados.append(pais)

    if encontrados:
        for p in encontrados:
            print(f"- {p['nombre']} | Superficie: {p['superficie']} km²")
    else:
        print("No se encontraron países en ese rango.")

# ===================== CASO 7, 8, 9: ORDENAR PAÍSES =====================
def ordenar_paises(paises, campo):
    print(f"\n--- Ordenar países por {campo} ---")

    # Solicita el tipo de ordenamiento y permite cancelar
    while True:
        print("1. Ascendente")
        print("2. Descendente")
        orden = input("Seleccione el orden (o 'salir' para cancelar): ").strip()
        if orden.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if orden in ["1", "2"]:
            break
        print("Error: opción inválida. Ingrese '1', '2' o 'salir'.")

    # Determina si el orden es descendente
    reverso = orden == "2"

    # Aplica el ordenamiento según el campo elegido
    if campo == "nombre":
        paises.sort(key=obtener_nombre, reverse=reverso)
    elif campo == "poblacion":
        paises.sort(key=obtener_poblacion, reverse=reverso)
    elif campo == "superficie":
        paises.sort(key=obtener_superficie, reverse=reverso)
    else:
        print("Error: campo de ordenamiento inválido.")
        return

    # Muestra los países ordenados
    print(f"\nListado ordenado por {campo} ({'descendente' if reverso else 'ascendente'}):")
    for p in paises:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")


# ===================== CASO 10: MOSTRAR ESTADÍSTICAS =====================
def mostrar_estadisticas(paises):
    print("\n--- Estadísticas de países ---")

    # Verifica si hay datos disponibles
    if len(paises) == 0:
        print("No hay datos disponibles.")
        return

    # Inicializa variables para cálculo
    mayor = paises[0]  # País con mayor población (inicialmente el primero)
    menor = paises[0]  # País con menor población (inicialmente el primero)
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}  # Diccionario para contar países por continente

    # Recorre la lista de países para calcular estadísticas
    for pais in paises:
        # Actualiza país con mayor población
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        # Actualiza país con menor población
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        # Acumula población y superficie
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        # Cuenta países por continente
        cont = pais["continente"]
        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    # Calcula promedios
    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    # Muestra resultados
    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']})")
    print(f"Promedio de población: {int(promedio_poblacion)}")
    print(f"Promedio de superficie: {int(promedio_superficie)} km²")
    print("Cantidad de países por continente:")
    for cont in continentes:
        print(f"- {cont}: {continentes[cont]}")





# ===================== MENÚ PRINCIPAL =====================
def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar país")
    print("2. Actualizar datos de un país")
    print("3. Buscar país por nombre")
    print("4. Filtrar países por continente")
    print("5. Filtrar países por rango de población")
    print("6. Filtrar países por rango de superficie")
    print("7. Ordenar países por nombre")
    print("8. Ordenar países por población")
    print("9. Ordenar países por superficie")
    print("10. Mostrar estadísticas")
    print("0. Salir")

def ejecutar_programa():
    paises = cargar_datos()
    print(f"\nSe cargaron {len(paises)} país(es) desde el archivo.")
    while True:
        print("\n" + "=" * 40)  # Línea divisoria visual
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_pais(paises)
            case "2":
                actualizar_datos_pais(paises)
            case "3":
                buscar_pais_por_nombre(paises)
            case "4":
                filtrar_paises_por_continente(paises)
            case "5":
                filtrar_paises_por_rango_poblacion(paises)
            case "6":
                filtrar_paises_por_rango_superficie(paises)
            case "7":
                ordenar_paises(paises, "nombre")
            case "8":
                ordenar_paises(paises, "poblacion")
            case "9":
                ordenar_paises(paises, "superficie")
            case "10":
                mostrar_estadisticas(paises)
            case "0":
                guardar_datos(paises)
                print("Datos guardados. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

ejecutar_programa()



