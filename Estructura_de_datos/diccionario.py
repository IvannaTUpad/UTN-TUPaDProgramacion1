
# 1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
 1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300


precios_frutas['Naranja']= 1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=2300

print(precios_frutas)

print('                                      ')

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800

print(precios_frutas)

print('                                                 ')
# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
# desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
# precios.


lista_frutas=list(precios_frutas.keys())
print(lista_frutas)
print('                                             ')
# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ").strip().title()
    numero = input(f"Ingresá el número de {nombre}: ").strip()
    
    # Validación básica: que no esté vacío y tenga al menos 7 dígitos
    if numero.replace("+", "").replace("-", "").replace(" ", "").isdigit() and len(numero) >= 7:
        contactos[nombre] = numero
    else:
        print("Número inválido. No se guardó el contacto.")

# Consultar contacto
nombre_buscar = input("Ingresá el nombre que querés buscar: ").strip().title()

if nombre_buscar in contactos:
    print(f"El número de {nombre_buscar} es {contactos[nombre_buscar]}")
else:
    print("Ese contacto no está guardado.")

print('                                  ')

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.
# Ejemplo:
frase= input('Escriba una frase: ').lower()

palabras_unicas=set(frase.split())
print(palabras_unicas)

from collections import Counter

conteo=Counter(frase.split())
print(conteo)
print('                                         ')

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
# Luego, mostrá el promedio de cada alumno.

# Crear diccionario para guardar alumnos y sus notas
alumnos = {}

# Cargar datos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    
    # Ingresar las 3 notas como tupla
    nota1 = float(input(f"Ingresá la primera nota de {nombre}: "))
    nota2 = float(input(f"Ingresá la segunda nota de {nombre}: "))
    nota3 = float(input(f"Ingresá la tercera nota de {nombre}: "))
    
    alumnos[nombre] = (nota1, nota2, nota3)



print(alumnos)

# Mostrar promedio de cada alumno
print(" Promedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: {promedio:.2f}")




print('                              ')

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
# y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)


parcial1={10,11,12,18}
parcial2={15,6,17,18}



print("Ambos parciales", parcial1 & parcial2)
print("Solo uno de los parciales", parcial1 - parcial2)
print("Al menos un parcial aprobado", parcial1| parcial2)

print('                                     ')
# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

stock_productos = {
    "Leche": 500,
    "Azucar": 300,
    "Sal": 1000,
    "Fideos": 300
}

producto = input("Ingresá el nombre del producto: ")

# Consultar stock
if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    
    # Preguntar si quiere agregar unidades
    opcion = input("¿Querés agregar unidades a este producto? (s/n): ").lower()
    if opcion == "s":
        unidades = int(input("¿Cuántas unidades querés agregar?: "))
        stock_productos[producto] += unidades
        print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
    else:
        print("No se modificó el stock.")
else:
    print(" El producto no está en el inventario.")
    
    # Preguntar si quiere agregarlo
    opcion = input("¿Querés agregar este producto al inventario? (s/n): ").lower()
    if opcion == "s":
        nuevo_stock = int(input("Ingresá el stock inicial: "))
        stock_productos[producto] = nuevo_stock
        print(f"Producto agregado: {producto} con stock de {nuevo_stock}")
    else:
        print(" No se agregó el producto.")

print('                               ')

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
agenda={('miercoles','10:00'):'reunion',('jueves','9:00'):'trabajo_grupal',('viernes','11:00'):'tramite'}

dia = input("Ingrese el día: ").lower()
hora = input("Ingrese la hora (formato HH:MM): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Evento agendado: {agenda[clave]}")
else:
    print("No hay eventos agendados en ese horario.")


print('                                     ')
# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Italia": "Roma",
    "Japón": "Tokio"
}

capitales = {capital: pais for pais, capital in paises.items()}

print(capitales)