# 1) Crea una función recursiva que calcule el factorial de un número.
# Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
# de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(n):
    if n == 0 or n == 1:
        return 1  
    else:
        return n * factorial(n - 1)  

print("\n--- Ejercicio 1: Factorial ---")
for i in range(1, 6):
    print(f"{i}! = {factorial(i)}")


# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada.
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\n--- Ejercicio 2: Fibonacci ---")
for i in range(7):
    print(f"F({i}) = {fibonacci(i)}")


# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente,
# utilizando la fórmula n^m = n * n^(m-1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

print("\n--- Ejercicio 3: Potencia ---")
print("2^4 =", potencia(2, 4))
print("5^3 =", potencia(5, 3))


# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal
# y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

print("\n--- Ejercicio 4: Decimal a Binario ---")
print("Binario de 10:", decimal_a_binario(10))
print("Binario de 25:", decimal_a_binario(25))


# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
# Requisitos: La solución debe ser recursiva. No se debe usar [::-1] ni la función reversed().

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

print("\n--- Ejercicio 5: Palíndromo ---")
print("¿'reconocer' es palíndromo?:", es_palindromo("reconocer"))
print("¿'mama' es palíndromo?:", es_palindromo("mama"))


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
# número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones: No se puede convertir el número a string. Usá operaciones matemáticas (%, //) y recursión.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

print("\n--- Ejercicio 6: Suma de Dígitos ---")
print("Suma de dígitos de 1234:", suma_digitos(1234))
print("Suma de dígitos de 305:", suma_digitos(305))


# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques,
# en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo
# y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print("\n--- Ejercicio 7: Contar Bloques ---")
print("Bloques para pirámide de 4 niveles:", contar_bloques(4))
print("Bloques para pirámide de 6 niveles:", contar_bloques(6))


# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    numero_str = str(numero)
    digito_str = str(digito)

    if len(numero_str) == 0:
        return 0
    else:
        coincidencia = 1 if numero_str[0] == digito_str else 0
        return coincidencia + contar_digito(numero_str[1:], digito)

print("\n--- Ejercicio 8: Contar Dígito ---")
print("Cantidad de veces que aparece el 2 en 12233421:", contar_digito(12233421, 2))
print("Cantidad de veces que aparece el 5 en 5555:", contar_digito(5555, 5))
print("Cantidad de veces que aparece el 7 en 123456:", contar_digito(123456, 7))



