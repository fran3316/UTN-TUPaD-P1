#Actividad 1 - Función Hola Mundo
def holaMundo():
    print("Hola mundo!!!")

holaMundo()

#Actividad 2 - Función Saludar

def saludar(nombre):
    print(f"Hola {nombre}!!!")

saludar("francisco")

#Actividad 3 - Función Información Personal
nombre = input("Ingrese a continuación su nombre: ")
apellido = input("Ingrese a continuación su apellido: ")
edad = input("Ingrese a continuación su edad: ")
residencia = input("Ingrese a continuación su residencia: ")

def infoPersonal(nombre, apellido, edad, residencia):
    print(f"Hola me llamo {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

infoPersonal(nombre, apellido, edad, residencia)

#Actividad 4 - Función para calcular área y perímetro
import math
radio = int(input("Ingrese a continuación el radio del círculo: "))
pi = math.pi  #aca guardo el numero de pi
#calcular área

def calculoArea(radio):
    area = pi * (radio**2)
    print(f"El área del círculo es de {area}")

#calcular perímetro

def calculoPerimetro(radio):
    perimetro = 2 * pi * radio
    print(f"El perímetro del círculo es de {perimetro}")

calculoArea(radio)
calculoPerimetro(radio)

#Actividad 5 - Función segundos a horas

#convierte segundos a horas
segundos = input("Ingrese la cantidad de segundos a convertir a horas: ")
def segundosAHoras(segundos):
    horas = int(segundos) / 3600
    print(f"{segundos} segundos son {horas} horas")

segundosAHoras(segundos)

#Actividad 6 - Tabla de Multiplicar
numero=int(input("Ingrese a continuación un número para mostrar su tabla: "))
def tablaMult(numero):
    print(f"La tabla de {numero} es: ")
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")
tablaMult(numero)

#Actividad 7 - Función Operaciones Básicas

def operaciones_basicas(a,b):
    suma = a+b
    resta = a-b
    division = a*b
    multiplicacion = a/b

    # Crea una tupla con los resultados y la devuelve
    resultados = (suma, resta, multiplicacion, division)
    return resultados


num1 = 10
num2 = 5
mis_resultados = operaciones_basicas(num1, num2)

print(f"Los resultados de las operaciones son: {mis_resultados}")
print(f"Tipo de variable 'mis_resultados': {type(mis_resultados)}")
print(f"Suma: {mis_resultados[0]}")
print(f"Resta: {mis_resultados[1]}")
print(f"Multiplicación: {mis_resultados[2]}")
print(f"División: {mis_resultados[3]}")

#Actividad 8 - Función calcular Imc

#ingreso los valores por teclado
peso = float(input("Ingrese a continuación su peso en kgs: "))
altura = float(input("ingrese a continuación su altura en mts: "))

#defino la función imc
def calcularImc(peso,altura):
    imc = peso / (altura**2)
    print(f"Su IMC es de: {imc}")

calcularImc(peso,altura)

#Actividad 9 - Funcion Celsius a Fahrenheit 
celsius = float(input("Ingrese la temperatura en Celsius para convertirla a Fahrenheit: "))

def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius*1.8) + 32
    print(f"{celsius}°C es igual a {fahrenheit}°F")

#llamo a la funcíon para que me haga el pasaje de C a F    
celsius_a_fahrenheit(celsius)

#Actividad 10 - Calcular Promedio dado 3 numeros
#ingresa 3 numeros por pantalla
num1 = float("ingrese un numero a continuación:")
num2 = float("ingrese otro numero a continuación:")
num3 = float("ingrese otro numero a continuación:")

def calcular_promedio(a,b,c):
    promedio = (a+b+c)/3
    print(f"el promedio de {a}, {b} y {c} es de {promedio}")

calcular_promedio(num1,num2,num3)