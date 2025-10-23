# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado
# productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad

print('Creando archivo inicial')

# Abrimos el archivo en modo escritura con 'with'
with open("productos.txt", "w") as archivo_productos:
    print("1. Escribiendo archivo")
    archivo_productos.write("Pan,150,20\n")
    archivo_productos.write("Leche,200,15\n")
    archivo_productos.write("Arroz,300,10\n")
import os
print("Archivo productos.txt creado con tres productos.")
print("¿Existe productos.txt?", os.path.exists("productos.txt"))
print("Ruta completa:", os.path.abspath("productos.txt"))

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
# línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
# formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

print("Leyendo archivo txt")

with open("productos.txt","r") as archivo:
    print("\n Lista de productos:")


    for linea in archivo:
        linea=linea.strip()
        partes=linea.split(",")
    

        if len(partes) == 3:
            nombre, precio, cantidad = partes
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
        else:
            print("Línea mal formada:", linea)



# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
# los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
# cantidad) y lo agregue al archivo sin borrar el contenido existente.

# 3. Agregar productos desde teclado

# 3. Agregar productos desde teclado 

while True:
    nuevo_producto = input("¿Desea agregar un nuevo producto? (s/n): ").lower()
    if nuevo_producto != "s":
        break

    nombre = input("Nombre del producto: ")
    precio = input("Precio: ")
    cantidad = input("Cantidad: ")

    if (
        nombre.strip() != "" and
        precio.strip() != "" and
        cantidad.strip() != "" and
        precio.replace(".", "", 1).isdigit() and
        cantidad.isdigit()
    ):
        linea = f"{nombre},{precio},{cantidad}\n"
        with open("productos.txt", "a") as archivo:
            archivo.write(linea)
        print(" Producto agregado al archivo.")
    else:
        print("Datos inválidos. No se agregó el producto.")



# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
# una lista llamada productos, donde cada elemento sea un diccionario con claves:
# nombre, precio, cantidad.

productos = []

with open("productos.txt", "r") as archivo:
    for linea in archivo:
        partes = linea.strip().split(",")
        if len(partes) == 3:
            nombre, precio, cantidad = partes
            if (
                nombre.strip() != "" and
                precio.replace(".", "", 1).isdigit() and
                cantidad.isdigit()
            ):
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
            else:
                print("Datos inválidos en línea:", linea.strip())
        else:
            print("Línea mal formada:", linea.strip())




# 5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
# producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
# no existe, mostrar un mensaje de error.
# 5. Buscar producto por nombre

consulta = input("Ingrese el producto a consultar: ").lower()
encontrado = False

for producto in productos:
    if producto["nombre"].lower() == consulta:
        print(f"\n Producto encontrado:")
        print(f"Nombre: {producto['nombre']}")
        print(f"Precio: ${producto['precio']:.2f}")
        print(f"Cantidad: {producto['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print(f"\n El producto '{consulta}' no se encuentra en la lista.")

    
# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
# productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
# productos actualizados desde la lista
with open("productos.txt", "w") as archivo:
    for producto in productos:
        linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
        archivo.write(linea)

print("\n Archivo productos.txt actualizado con todos los productos.")


print("\n Lista final guardada:")
for producto in productos:

    print(f"{producto['nombre']} - ${producto['precio']} - Cantidad: {producto['cantidad']}")
