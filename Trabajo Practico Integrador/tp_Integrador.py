#aplicación en Python que permite gestionar información sobre países,
#aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas,
#ordenamientos y estadísticas. El sistema es capaz de leer datos desde un archivo CSV,
#realizar consultas y generar indicadores clave a partir del dataset. 
# ===================== IMPORTACIÓN DE MÓDULOS Y CONFIGURACIÓN ====================
import csv # Módulo para leer y escribir archivos CSV (valores separados por coma)
import os  # Módulo para interactuar con el sistema operativo (verificar existencia de archivos, etc.


ARCHIVO = "paises.csv" # Nombre del archivo donde se almacenan los datos de los países

# ========== VALIDACIONES DE CAMPOS ==========

# Verifica que el nombre no esté vacío ni sea solo números
def validar_nombre_pais(nombre):
    nombre = nombre.strip()
    return nombre != "" and not nombre.isdigit()

# Verifica que la población sea un número entero positivo dentro del rango permitido
def validar_poblacion(poblacion):
    poblacion = poblacion.strip()
    return poblacion.isdigit() and 1 <= int(poblacion) <= 2_000_000_000

# Verifica que la superficie sea un número entero positivo dentro del rango permitido
def validar_superficie(superficie):
    superficie = superficie.strip()
    return superficie.isdigit() and 1 <= int(superficie) <= 20_000_000

# Verifica que el continente no esté vacío ni sea un número
def validar_continente(continente):
    continente = continente.strip()
    return continente != "" and not continente.isdigit()

# Verifica si el país ya existe en la lista (comparación insensible a mayúsculas)
def existe_pais(paises, nombre):
    nombre = nombre.strip().lower()
    for pais in paises:
        if pais["nombre"].strip().lower() == nombre:
            return True
    return False

# Busca países por coincidencia exacta o parcial en el nombre
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

# Normaliza un texto eliminando espacios, convirtiendo a minúsculas
# y reemplazando vocales con tilde por su versión sin tilde.
# Se utiliza para comparar nombres o continentes sin errores por mayúsculas o acentos

def normalizar_texto(texto):
    texto = texto.strip().lower()
    texto = texto.replace("á", "a")
    texto = texto.replace("é", "e")
    texto = texto.replace("í", "i")
    texto = texto.replace("ó", "o")
    texto = texto.replace("ú", "u")
    return texto


# ========== FUNCIONES DE ORDENAMIENTO ==========
# Devuelve el nombre del país sin espacios al inicio o final.
# Se utiliza como clave para ordenar alfabéticamente por nombre

def obtener_nombre(pais):
    return pais.get("nombre", "").strip()


# Devuelve la población del país como entero.
# Se utiliza como clave para ordenar por cantidad de población.
def obtener_poblacion(pais):
    return int(pais.get("poblacion", 0))


# Devuelve la superficie del país como entero.
# Se utiliza como clave para ordenar por tamaño territorial.

def obtener_superficie(pais):
    return int(pais.get("superficie", 0))



# ========== CARGA Y GUARDADO DE DATOS ==========

def cargar_datos():
    paises = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)

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
                    validar_poblacion(poblacion) and
                    validar_superficie(superficie)
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

# ==========CASO 1:  AGREGAR PAÍS ==========

# Función que permite agregar un país al listado.
# Valida todos los campos obligatorios: nombre, población, superficie y continente.
# Evita duplicados y permite cancelar en cualquier paso.
def agregar_pais(paises):
    print("\n--- Agregar un nuevo país ---")

    # Validación del nombre del país
    while True:
        nombre = input("\nIngrese el nombre del país (o 'salir' para cancelar): ").strip()
        if nombre.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if not validar_nombre_pais(nombre):
            print("Error: el nombre no puede estar vacío ni contener números o símbolos.")
            continue
        if any(normalizar_texto(p["nombre"]) == normalizar_texto(nombre) for p in paises):
            print("Error: ese país ya está registrado.")
            continue
        break

    # Validación de población
    while True:
        poblacion = input("Ingrese la población (o 'salir' para cancelar): ").strip()
        if poblacion.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_poblacion(poblacion):
            poblacion = int(poblacion)
            break
        print("Error: población inválida. Debe ser un número entre 1 y 2.000.000.000.")

    # Validación de superficie
    while True:
        superficie = input("Ingrese la superficie en km² (o 'salir' para cancelar): ").strip()
        if superficie.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_superficie(superficie):
            superficie = int(superficie)
            break
        print("Error: superficie inválida. Debe ser un número entre 1 y 20.000.000.")

    # Validación de continente (obligatorio)
    while True:
        continente = input("Ingrese el continente (no puede estar vacío ni ser un número): ").strip()
        if validar_continente(continente):
            break
        print("Error: el continente no puede estar vacío ni ser un número.")

    # Agregar país al listado (solo una vez)
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    paises.append(nuevo_pais)
    print(f"País '{nombre}' agregado correctamente.")


# ========== CASO 2: ACTUALIZAR DATOS ==========
# Función que permite actualizar los datos de un país existente.
# Muestra los datos actuales, valida los nuevos y actualiza ambos campos solo si son válidos.

def actualizar_datos_pais(paises):
    print("\n--- Actualizar datos de un país ---")

    while True:
        # Ingreso del nombre
        while True:
            nombre = input("Ingrese el nombre del país a actualizar (o 'salir' para cancelar): ").strip()
            if nombre.lower() == "salir":
                print("Operación cancelada por el usuario.")
                return
            if not validar_nombre_pais(nombre):
                print("Error: el nombre no puede estar vacío ni contener números o símbolos.")
                continue
            break

        nombre_normalizado = normalizar_texto(nombre)

        # Búsqueda del país
        pais_encontrado = None
        for pais in paises:
            if normalizar_texto(pais["nombre"]) == nombre_normalizado:
                pais_encontrado = pais
                break

        if not pais_encontrado:
            print("No se encontró un país con ese nombre.")
            return

        while True:
            # Mostrar datos actuales
            print(f"\nDatos actuales de '{pais_encontrado['nombre']}':")
            print(f"- Población: {pais_encontrado['poblacion']}")
            print(f"- Superficie: {pais_encontrado['superficie']} km²")

            # Validar nueva población
            while True:
                nueva_poblacion = input("Ingrese la nueva población (o 'salir' para cancelar): ").strip()
                if nueva_poblacion.lower() == "salir":
                    print("Actualización cancelada.")
                    return
                if validar_poblacion(nueva_poblacion):
                    nueva_poblacion = int(nueva_poblacion)
                    break
                print("Error: población inválida. Debe ser un número entre 1 y 2.000.000.000.")

            # Validar nueva superficie
            while True:
                nueva_superficie = input("Ingrese la nueva superficie (o 'salir' para cancelar): ").strip()
                if nueva_superficie.lower() == "salir":
                    print("Actualización cancelada.")
                    return
                if validar_superficie(nueva_superficie):
                    nueva_superficie = int(nueva_superficie)
                    break
                print("Error: superficie inválida. Debe ser un número entre 1 y 20.000.000.")

            # Actualizar ambos datos juntos
            pais_encontrado["poblacion"] = nueva_poblacion
            pais_encontrado["superficie"] = nueva_superficie
            print("Datos actualizados correctamente.")

            # Confirmación final
            print(f"\nDatos actualizados de '{pais_encontrado['nombre']}':")
            print(f"- Nueva población: {pais_encontrado['poblacion']}")
            print(f"- Nueva superficie: {pais_encontrado['superficie']} km²")

            

#----------------------CASO 3: BUSCAR PAISES POR NOMBRE----------------------
# Función que permite buscar países por nombre o parte del nombre.
# Ignora mayúsculas y tildes, y muestra coincidencias si las hay.


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

    termino_normalizado = normalizar_texto(termino)

    # Busca coincidencias en la lista de países
    resultados = []
    for pais in paises:
        nombre_normalizado = normalizar_texto(pais["nombre"])
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





#----------------------CASO 4: FILTRAR PAISES POR CONTINENTE----------------------------------
# Función que filtra los países según el continente ingresado.
# Ignora tildes y mayúsculas para evitar errores de coincidencia.

def filtrar_paises_por_continente(paises):
    print("\n--- Filtrar países por continente ---")

    # Solicita el nombre del continente y permite cancelar con 'salir'
    continente = input("Ingrese el nombre del continente (o 'salir' para cancelar): ").strip()
    if continente.lower() == "salir":
        print("Operación cancelada por el usuario.")
        return

    # Validar que no sea un número
    if continente.isdigit():
        print("Error: el continente no puede ser un número.")
        return

    # Normaliza el texto ingresado para comparar de forma consistente
    continente_normalizado = normalizar_texto(continente)

    # Filtra los países que pertenecen al continente ingresado
    encontrados = []
    for pais in paises:
        if normalizar_texto(pais["continente"]) == continente_normalizado:
            encontrados.append(pais)

    # Muestra los resultados encontrados
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} país(es) en {continente.capitalize()}:")
        for p in encontrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km²")
    else:
        print("No se encontraron países en ese continente.")






# ===================== CASO 5: FILTRAR POR RANGO DE POBLACIÓN =====================
# Función que filtra los países cuya población esté dentro de un rango dado.
# Valida ambos extremos y muestra los resultados encontrados.


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

    # Filtra países dentro del rango
    encontrados = [p for p in paises if minimo <= p["poblacion"] <= maximo]

    # Muestra resultados
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} país(es) con población entre {minimo} y {maximo}:")
        for p in encontrados:
            print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")
    else:
        print("No se encontraron países en ese rango de población.")

# ===================== CASO 6: FILTRAR POR RANGO DE SUPERFICIE =====================
# Función que filtra los países cuya superficie esté dentro de un rango dado.
# Valida ambos extremos y muestra los resultados encontrados.


def filtrar_paises_por_rango_superficie(paises):
    print("\n--- Filtrar países por rango de superficie ---")

    # Solicita y valida la superficie mínima
    while True:
        minimo = input("Superficie mínima (o 'salir' para cancelar): ").strip()
        if minimo.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_superficie(minimo):
            minimo = int(minimo)
            break
        print("Error: la superficie mínima debe ser un número entero positivo entre 1 y 20.000.000.")

    # Solicita y valida la superficie máxima
    while True:
        maximo = input("Superficie máxima (o 'salir' para cancelar): ").strip()
        if maximo.lower() == "salir":
            print("Operación cancelada por el usuario.")
            return
        if validar_superficie(maximo):
            maximo = int(maximo)
            break
        print("Error: la superficie máxima debe ser un número entero positivo entre 1 y 20.000.000.")

    if minimo > maximo:
        print("Error: el mínimo no puede ser mayor que el máximo.")
        return

    # Filtra países dentro del rango
    encontrados = [p for p in paises if minimo <= p["superficie"] <= maximo]

    # Muestra resultados
    if encontrados:
        print(f"\nSe encontraron {len(encontrados)} país(es) en ese rango:")
        for p in encontrados:
            print(f"- {p['nombre']} | Superficie: {p['superficie']} km²")
    else:
        print("No se encontraron países en ese rango de superficie.")



# ===================== CASO 7, 8, 9: ORDENAR PAÍSES =====================
# Función que ordena los países por nombre, población o superficie.
# El orden puede ser ascendente o descendente según el campo.


def ordenar_paises(paises, campo):
    campo = campo.strip().lower()
    campos_validos = ["nombre", "poblacion", "superficie"]

    if campo not in campos_validos:
        print("Error: campo de ordenamiento inválido.")
        return

    print(f"\n--- Ordenar países por {campo} ---")

    # Determina el tipo de ordenamiento
    if campo == "superficie":
        while True:
            print("1. Ascendente")
            print("2. Descendente")
            orden = input("Seleccione el orden (o 'salir' para cancelar): ").strip()
            if orden.lower() == "salir":
                print("Operación cancelada por el usuario.")
                return
            if orden in ["1", "2"]:
                reverso = orden == "2"
                break
            print("Error: opción inválida. Ingrese '1', '2' o 'salir'.")
    elif campo == "nombre":
        reverso = False  # Siempre ascendente
    elif campo == "poblacion":
        reverso = True   # Siempre descendente

    # Aplica el ordenamiento
    if campo == "nombre":
        ordenados = sorted(paises, key=lambda p: normalizar_texto(p["nombre"]), reverse=reverso)
    elif campo == "poblacion":
        ordenados = sorted(paises, key=lambda p: p["poblacion"], reverse=reverso)
    elif campo == "superficie":
        ordenados = sorted(paises, key=lambda p: p["superficie"], reverse=reverso)

    print(f"\nListado ordenado por {campo} ({'descendente' if reverso else 'ascendente'}):")
    for p in ordenados:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")



# ===================== CASO 10: MOSTRAR ESTADÍSTICAS =====================
# Función que muestra estadísticas generales sobre los países cargados.
# Incluye máximos, promedios y cantidad por continente.


def mostrar_estadisticas(paises):
    print("\n--- Estadísticas de países ---")

    if not paises:
        print("No hay datos disponibles.")
        return

    mayor = menor = paises[0]
    suma_poblacion = 0
    suma_superficie = 0
    continentes = {}

    for pais in paises:
        if pais["poblacion"] > mayor["poblacion"]:
            mayor = pais
        if pais["poblacion"] < menor["poblacion"]:
            menor = pais

        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]

        cont = normalizar_texto(pais["continente"])
        continentes[cont] = continentes.get(cont, 0) + 1

    promedio_poblacion = suma_poblacion / len(paises)
    promedio_superficie = suma_superficie / len(paises)

    print(f"País con mayor población: {mayor['nombre']} ({mayor['poblacion']:,})")
    print(f"País con menor población: {menor['nombre']} ({menor['poblacion']:,})")
    print(f"Promedio de población: {int(promedio_poblacion):,}")
    print(f"Promedio de superficie: {int(promedio_superficie):,} km²")
    print("Cantidad de países por continente:")
    for cont in sorted(continentes):
        print(f"- {cont.capitalize()}: {continentes[cont]}")

# ===================== CASO 11: MOSTRAR TODOS LOS PAÍSES =====================
# Muestra todos los países cargados con sus datos completos.

def mostrar_todos_los_paises(paises):
    print("\n--- Listado completo de países ---")
    if not paises:
        print("No hay países cargados.")
        return

    for p in paises:
        print(f"- {p['nombre']} | Población: {p['poblacion']} | Superficie: {p['superficie']} km² | Continente: {p['continente']}")


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
    print("11.Mostar todos los paises cargados")
    print("0. Salir")

def ejecutar_programa():
    paises = cargar_datos()
    print(f"\nSe cargaron {len(paises)} país(es) desde el archivo.")
    while True:
        print("\n" + "=" * 40)
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                agregar_pais(paises)
                guardar_datos(paises)
            case "2":
                actualizar_datos_pais(paises)
                guardar_datos(paises)
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
            case "11":
                mostrar_todos_los_paises(paises)
            case "0":
                guardar_datos(paises)
                print("Datos guardados. ¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")

# Ejecutar el programa
ejecutar_programa()

