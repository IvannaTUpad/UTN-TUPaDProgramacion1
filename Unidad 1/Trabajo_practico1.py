#1-Crear un programa que imprima por pantalla el mensaje. "Hola mundo!"
print("Hola Mundo!")

#2-Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado
nombre= input("Ingrese su nombre:")
print(f"Hola {nombre}!")

#3-Crear un programa que pida al usuario nombre,apellido,edad y lugar de residencia e imprima
nombre= input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
lugar_de_residencia=input("Ingrese su lugar de residencia actual:")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_de_residencia}")

#4-Crear un programa que pida al usuario el radio de un circulo e imprima por pantalla su area y su perimetro
radio=input(("Ingrese el radio de un circulo:"))
radio = float(radio)
pi=3.14159
area= pi * radio ** 2
perimetro= 2*pi*radio
print(f"el area del circulo es {area} y su perimetro  {perimetro}")

#5-Crear un programa que pida al usuario una cantidad de segundos e imprima por pantallas a cuantas horas equivale.
cantidad_segundos= input("Ingrese una cantidad de segundos:")
cantidad_segundos=int(cantidad_segundos)
horas=cantidad_segundos/3600
print(f" equivale a {horas} de hora")

#6-Crear un programa que pida al usuario un numero e imprima por pantalla la tabla de multiplicar de dicho numero
numero=int(input("Ingrese un numero entero:"))
if numero>0 and i>0:
    for i in range (1,11):
        resultado= numero * i
        print(f"{numero} x i =  {resultado}")

      
#7-Crear un programa que pida al usuario dos numeros distintos de cero y muestre por pantalla el resultado de sumarlos, restarlos, dividirlos y multiplicarlos
num1= int(input("Ingrese un numero distinto de cero: "))
num2= int(input("Ingrese un segundo numero distinto de cero: "))
suma= num1 + num2
resta= num1 - num2
multiplicacion= num1*num2
division= num1/num2
if num1 !=0 and num2 !=0:
    print(suma, resta, multiplicacion, division )
else:
    print("Ambos numeros deben ser distintos de cero")

#8-Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su indice de masa corporal
altura=float(input("Ingrese su altura:")) 
peso = int(input("Ingrese su peso:")) 
IMC= peso/(altura) ** 2 
IMC= int(IMC)
print(f"Su indice de masa corporal es el siguiente: {IMC}")

#9-Crear un programa que pida al usuario una temperatura en grados celsius e imprima por pantalla su equivalente en fahrenheit
Celsius= float(input("Ingrese una temperatura en grados Celsius:"))
Fahrenheit= 9/5 * Celsius + 32
print(f"equivalente en fahrenheit {Fahrenheit}")

#10- Crear un programa que pida al usuario 3 numeros e imprima el promedio
num_1= int(input("Ingrese un primer numero:"))
num_2= int(input("Ingrese un segundo numero:"))
num_3= int(input("Ingrese un tercer numero:"))
promedio = (num_1+num_2+num_3)/3
print(f"el promedio de dichos numeros es: {promedio}")

#TODO EL TRABAJO REALIZADO