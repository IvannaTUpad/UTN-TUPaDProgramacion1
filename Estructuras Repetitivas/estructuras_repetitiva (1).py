#1) crea un programa que imprima por pantalla todos los numeros enteros desde 0 hasta 100 (incluyendolos) en orden creciente, mostrando un numero por linea.


for i in range (101):
   print(i)    




#2)Desarrolla un programa que solicite al usuario un numero entero y determine la cantidad de digitos que contiene.

numero=abs(int(input("Ingrese un numero entero: ")))
numero= str(numero)
contador=0
for numero in range(len (numero)):
 contador+=1
print(f"la cantidad de digitos del numero ingresado es {contador}")
contador+=1




#3) Escribe un programa que sume todos los numeros enteros comprendidos entre dos valores dados por el usuario, excluyendo esos 2 valores.

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese un segundo valor: "))

if num1 > num2:
    num1, num2 = num2, num1

sumatoria = 0
for numero in range(num1 + 1, num2):
    sumatoria += numero

print(f"La sumatoria de los numeros enteros entre {num1} y {num2} es : {sumatoria}")



#4)Elabora un programa que permita al usuario ingresar numeros enteros y los sume en secuencia.El programa debe detenerse y mostrar el total acumulado cuando el usuario ingresa un 0.
suma=0

while True:
  numero=int((input("Ingrese un numero por favor: ")))
  if numero==0:
    break
  suma+=numero
print(f"El total acumulado es:{suma} ")


#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero = random.randint(0, 9)

intentos_limites=3

while intentos_limites>0:
    Intento_usuario = abs(int(input("Ingrese un número del 0 al 9: ")))
    if numero == Intento_usuario:
        print("¡Adivinaste!")
        break

    else:
        print("Intentelo otra vez")
        intentos_limites-=1

if intentos_limites==0:
   print(f"Se acabaron los intentos, gracias por participar, el numero era: {numero} ")




#6) Desarrolla un programa que imprima en pantalla todos los numeros pares comprendidos entre 0 y 100, en forma decreciente.

for i in range(98,1,-2):
     print(i)



#7)Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

numero = abs(int(input("Ingrese un número entero positivo: ")))

suma = 0
contador = 0

while contador <= numero:
    suma += contador
    contador += 1

print(f"La suma de todos los números entre 0 y {numero} es {suma}.")

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#  programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#  negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#  menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares=0
Impares=0
negativos=0
positivos=0
contador=0

while contador<100:
  numero=int(input("Ingrese hasta 100 numeros: "))
  if numero %2 ==0:
   pares+=1

  else :
   Impares+=1


  if numero<0:
   negativos+=1

  elif numero>0:
   positivos+=1

  contador+=1

print(f"la cantidad de numeros pares: {pares}")
print(f"la cantidad de numeros Impares: {Impares}")
print(f"la cantidad de numeros Negativos: {negativos}")
print(f"la cantidad de numeros Positivos: {positivos}")







#9) Elabora un programa que permita al usuario ingresar 100 numeros enteros y luego calcule la media de esos valores.

suma=0
contador=0 
print("Puede ingresar hasta 100 numeros")

while contador< 100: 
     numero=int(input("Ingrese los numeros enteros para calcular la media: "))
     suma+=numero
     contador+=1
media= suma/contador
print(f"La media de los numeros ingresados es {media}")


#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero=abs(int(input("Ingrese un numero: ")))
numero=str(numero)
numero_invertido=""
for i in range(len(numero)-1,-1,-1):
  numero_invertido+=numero[i]

print(f"El numero invertido es:{numero_invertido} ")





