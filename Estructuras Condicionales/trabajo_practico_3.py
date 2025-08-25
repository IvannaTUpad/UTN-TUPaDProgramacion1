#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad= int(input ("Ingrese su edad: "))

if edad > 18:
     print("Es mayor de edad") 

#2)Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”

nota= int(input ("Ingrese su nota: "))
if nota >=6 :
     print ("Aprobado")
else :
     print ("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par"

numero= int(input ("Ingrese un numero par: "))
if numero % 2 == 0 :
        print ("Ha ingresado un numero par ")
else:
      print ("Por favor, ingrese un numero par ")

#4)Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad= int(input ("Ingrese su edad: "))
if edad < 12 :
        print("Usted pertenece a la categoria Niño/a")
elif edad >= 12 and edad < 18 :
     print ("Usted pertenece a la categoria Adolescente")
elif edad >=18 and edad < 30 :
     print ("Usted pertenece a la categoria Adulto/a joven")
else :
     print ("Usted pertenece a la categoria Adulto/a")

#5)Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres"

contraseña= input ("Ingrese una contraseña de entre 8 y 14 caracteres: ")
if len(contraseña) >= 8 and len(contraseña) <= 14 :
     print ("Ha ingresado una contraseña correcta")
else:
     print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)Teniendo en cuenta lo antes mencionado(en el temario) escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mean, median, mode
import random
numeros_aleatorios =[random.randint(1,100) for i in range (50)]
print (numeros_aleatorios)
moda = mode (numeros_aleatorios)
mediana = median (numeros_aleatorios)
media= mean (numeros_aleatorios)

if media > mediana and mediana > moda :
     print ("Hay sesgo positivo o a la derecha")
elif media < mediana and mediana < moda :
      print ("Hay sesgo negativo o a la izquierda")
elif media == mediana == moda :
     print ("No hay sesgo")
else :
     print ("No se cumple ninguna condicion")

#7)Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.

frase = input ("Ingrese una frase o palabra: ")
if frase[-1].lower() in "aeiou":
     print (f"{frase}!")
else:
     print (frase)


#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro

nombre =input ("Ingrese su nombre: ")
print ("Opcion 1: Nombre en mayusculas")
print ("Opcion 2: Nombre en minusculas")
print ("Opcion 3: Nombre con la primera letra en mayuscula")
opcion = int(input ("Ingrese la opcion que desea (1, 2 o 3): "))
if opcion == 1:
     print (nombre.upper())
elif opcion == 2:
     print (nombre.lower())
elif opcion == 3:
     print (nombre.title())
else:
     print ("Opcion no valida")

#9-Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).


magnitud = float(input("Ingrese la magnitud de un terremoto en escala del 1 al 7: "))
if magnitud < 3:
     print ("Muy leve")
elif magnitud >= 3 and magnitud < 4:
     print ("Leve")
elif magnitud >= 4 and magnitud < 5:
     print ("Moderado")
elif magnitud >= 5 and magnitud < 6:
     print ("Fuerte")
elif magnitud >= 6 and magnitud < 7:
     print ("Muy fuerte")
else:
     print ("Extremo")
     


#10-Utilizando la información aportada en la siguiente tabla(en el temario) sobre las estaciones del año,escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Ingrese el hemisferio en el que se encuentra(norte/sur): ").strip().lower()
mes = int(input("Ingrese el mes en el que se encuentra (1-12): "))
dia = int(input("Ingrese el día (1-31): "))


if hemisferio == "sur":
        if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
            estacion = "Verano"
        elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
            estacion = "Invierno"
        elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion = "Primavera"
        else:
            estacion = "Fecha no válida"
else:  # hemisferio norte
        if (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 22):
            estacion = "Verano"
        elif (mes == 9 and dia >= 23) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
            estacion = "Otoño"
        elif (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 19):
            estacion = "Invierno"
        elif (mes == 3 and dia >= 20) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
            estacion = "Primavera"
        else:
            estacion = "Fecha no válida"

        print(f"Usted se encuentra en {estacion}.")   

