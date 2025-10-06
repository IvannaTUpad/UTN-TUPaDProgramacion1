# 1. Crear una función llamada imprimir_hola_mundo que imprima por
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
# programa principal.

def imprimir_hola_mundo ():
    print("Hola mundo!")


imprimir_hola_mundo()





# 2. Crear una función llamada saludar_usuario(nombre) que reciba
# como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario

def saludar_usuario(nombre):
    return(f"Hola {nombre}!")


nombre=input("Ingrese su nombre: ")

saludo=saludar_usuario(nombre)
print(saludo)



# 3. Crear una función llamada informacion_personal(nombre, apellido,
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.


def informacion_personal(nombre,apellido,edad,residencia):
 print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=int(input("Ingrese su edad: "))
residencia=input("Ingrese su residencia: ")

informacion_personal(nombre, apellido,edad,residencia)




# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados

pi=3.1416
def calcular_area_circulo(radio):
   return (pi*radio*radio)


def calcular_perimetro_circulo(radio):
   return (2*pi*radio)


radio=float(input("Ingrese el radio del circulo para realizar los calculos: "))

area=calcular_area_circulo(radio)
perimetro=calcular_perimetro_circulo(radio)

print(f"El area del circulo es:{area}")
print(f"El perimetro del circulo es:{perimetro}")




# 5. Crear una función llamada segundos_a_horas(segundos) que reciba
# una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.


def segundos_a_horas(segundos):
   return (segundos/3600)

segundos=int(input("Ingrese una cantidad de segundos, por favor: "))


hora= segundos_a_horas(segundos)
print(f"{hora} de hora")





# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un
# número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


num = int(input("Ingrese un número para ver su tabla de multiplicar: "))


tabla_multiplicar(num)






# 7. Crear una función llamada operaciones_basicas(a, b) que reciba
# dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.


def operaciones_basicas(a,b):
   return (a+b, a-b, a*b, a/b)

a= int(input("Ingrese un numero por favor: "))
b=int(input("Ingrese un segundo numero: "))

resultado= operaciones_basicas(a,b)

print("Suma:", resultado[0])
print("Resta:", resultado[1])
print("Multiplicación:", resultado[2])
print("División:", resultado[3])

  
 


# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el
# peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales


def calcular_imc(peso,altura):
   return peso/(altura**2)


peso=int(input("Ingrese su peso: "))
altura=float(input("Ingrese su altura: "))

IMC= calcular_imc(peso,altura)

print(f"su IMC es {round(IMC,2)}")




# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
# una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
# resultado usando la función.

def celsius_a_fahrenheit(celsius):
   return (celsius*9/5)+32


temp=float(input("Ingrese una temperatura en c°: "))

print(f"La temperatura  {temp} en grados Celsius equivale a {celsius_a_fahrenheit(temp)} Fahrenheit")







# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba
# tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta
# función.

def calcular_promedio(a,b,c):
   return((a+b+c)/3)

a=int(input("Ingrese un numero: "))
b=int(input("Ingrese un numero: "))
c=int(input("Ingrese un numero: "))

promedio=calcular_promedio(a,b,c)

print(f"El promedio entre {a} , {b}, {c} es {promedio}")