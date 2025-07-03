#Actividad 1 - Función factorial recursivo

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

#Mostrar factoriales desde 1 hasta número ingresado
num = int(input("Ingrese un número: "))
for i in range(1, num+1):
    print(f"Factorial de {i}: {factorial(i)}")
    
#Actividad 2- Función Fibonacci recursivo

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)

#Mostrar serie completa
n = int(input("Ingrese posición final: "))
for i in range(n+1):
    print(f"Posición {i}: {fibonacci(i)}")

#Actividad 3 - Función potencia recursiva

def potencia(base, exp):
    if exp == 0:
        return 1
    else:
        return base * potencia(base, exp-1)

#Ejemplo de uso
print(potencia(2, 3))  # Salida: 8

#Actividad 4 - Conversión decimal a binario (recursivo)

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n//2) + str(n%2)

#Ejemplo
print(decimal_a_binario(10))  # Salida: "1010"

#Actividad 5 - Función palíndromo recursivo

def es_palindrome(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindrome(palabra[1:-1])

#Ejemplos
print(es_palindrome("reconocer"))  # True
print(es_palindrome("python"))     # False

#Actividad 6 - Suma de dígitos recursiva

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n%10 + suma_digitos(n//10)

#Ejemplos
print(suma_digitos(1234))  # 10
print(suma_digitos(305))   # 8

#Actividad 7 - Pirámide de bloques recursiva

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n-1)

# Ejemplos
print(contar_bloques(4))  # 10
print(contar_bloques(2))  # 3

#Actividad 8 - Contar dígitos recursivo

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo = numero % 10
    conteo = 1 if ultimo == digito else 0
    return conteo + contar_digito(numero//10, digito)

#Ejemplos
print(contar_digito(12233421, 2))  # 3
print(contar_digito(123456, 7))    # 0