#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea

#Declaro e inicializo la variable contador que la voy a utilizar en la condicion del while.
contador = 0;

while (contador != 101):
    print(contador)
    contador += 1


# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
# dígitos que contiene.

#Declaro la variable ingresarNumero que va a almacenar el número ingresado por la persona.
ingresarNumero = input("Ingrese un numero Entero:")
#Declaro la variable digitos que va a contar la cantidad de dígitos del numero ingresado.
digitos = 0
#Segun las iteraciones que realice mi for voy a tener menos o mas dígitos.
for i in ingresarNumero:
    digitos += 1
#imprimo la cantidad de dígitos que tengo.
print(digitos)


# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.

#Declaro las variables que van a contener los  dos valores del rango comprendido
desde = int(input("Ingrese un número:"))
hasta = int(input("Ingrese un número:"))
# Declaro el bucle for que va a imprimir los números comprendidos entre los dos valores 
# anteriormente ingresados.
for i in range(desde+1, hasta, 1):
    print(i)


#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.


#La variable suma va a almacenar los números que vayan ingresando posteriormente.

suma = 0;
salir = False #Variable centinela
# Voy a utilizar un while que va a pedir repetidas veces que ingreses un número 
# que va a ser sumado a la variable acumuladora, hasta que el usuario ingrese un 0
# para salir del programa

while not salir:
    ingresarNumero = float(input("Porfavor, ingresar un número entero o un 0 para salir: "))
    if(ingresarNumero % 1 == 0 ):
         suma += ingresarNumero
         if(ingresarNumero == 0):
            salir = True
    else:
        print("Vuelva a intentar con un numero entero.")

# Imprimo por pantalla la suma de los números ingresados.

print(f"La suma de todos los números ingresados es {suma}")


# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
# Guardo dentro de esta variable numRandom, un numero random entre el 0 y el 9.
numRandom = random.randint(1, 8)
intentos = 0 #Variable contadora
adivinado = True #variable centinela, controla la ejecucion del bucle.
#Utilizo un bloque while porque no tengo determinada la cantidad de veces a iterar
while (adivinado):
    numero = int(input("Ingrese un número entre el 0 y el 9 e intente acertar esta adivinanza: "))
    # Por cada numero ingresar voy a sumar un intento a mi variable contadora
    intentos += 1
    # Si el numero ingresado es igual al numero random  hago lo siguiente.
    if numero == numRandom:
        # imprimo por pantalla el numero y la cantidad de intentos y luego salgo del blucle con break.
        print(f"adivinaste, el numero secreto es: {numero}")
        print(f"la cantidad de intentos es de {intentos}")
        adivinado = False



# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.

for i in range(98,0,-2):
    print(i) #imprimo uno por uno los numeros primos comprendidos entre el 0 y el 100


# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

# la variable suma va almacenar la suma de los numeros comprendidos entre 0 y el numero ingresado
suma = 0

#Solicito que se ingrese por teclado un numero entero positivo
numEntero = int(input("Ingrese a continuacion un numero entero positivo: "))

for i in range(1,numEntero):
    suma += i


print(f"la suma de todos los numeros comprendidos entre 0 y {numEntero} es: {suma}")



#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

#definimos e inicializamos las variables contadoras
negativos = 0
positivos = 0
par = 0
impar = 0

#el for se ejecuta 100 veces
for i in range(0, 100):
    numeroIngresado = int(input("Porfavor, ingrese a continuación un número entero:"))
    if numeroIngresado > 0:
        positivos += 1 # Si el numero es positivo, es decir > 0, sumo 1 a la variable.
        if numeroIngresado % 2 == 0:
            par +=1 # Si el numero es par sumo 1 a la variable.
        elif numeroIngresado % 2 == 1:
            impar += 1 # Si el numero es impar sumo 1 a la variable.        if numeroIngresado % 2 == 0:
            par +=1 # Si el numero es par sumo 1 a la variable.

    elif numeroIngresado < 0:
        negativos += 1 # Si el numero es negativo, sumo 1 a la variable.
        if numeroIngresado % 2 == 0:
            par +=1 # Si el numero es par sumo 1 a la variable.
        elif numeroIngresado % 2 == 1:
            impar += 1 # Si el numero es impar sumo 1 a la variable.
    
#imprimo la cantidad de numeros negativos, positivos, pares e impares.
print(f"la cantidad de numeros negativos es de: {negativos}")    
print(f"la cantidad de numeros positivos es de: {positivos}")
print(f"la cantidad de numeros pares es de: {par}")
print(f"la cantidad de numeros impares es de: {impar}")



#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

cantNumeros = 0 # En esta variable voy a contar la cantidad de numeros ingresados para utilizarla luego al dividir la suma.
suma = 0 #Esta variable la voy a utilizar como acumulador para sumar los numeros ingresados por teclado.
media = 0 # Aca voy a almacenar el valor de la media

for i in range(0, 100): #El for da 100 vueltas por lo que se ingresan por teclado 100 numeros
    numeroIngresado = int(input("Porfavor, ingrese a continuación un número entero:"))
    suma += numeroIngresado
    cantNumeros += 1

media = suma / cantNumeros # es el calculo de la media

print(f"El valor de la media es {media}")# imprime por pantalla el resultado de la media



#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

digitosInvertidos = ""
digitos = input("Por favor, a continuacion ingrese un numero:")

for i in reversed(digitos):
    digitosInvertidos+= i   

print(digitosInvertidos)
