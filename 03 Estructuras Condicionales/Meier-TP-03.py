#1) Escribir un programa que solicite la edad del usuario. 
# Si el usuario es mayor de 18 años, deberá mostrar 
# un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese a continuacion su edad: "))

if edad >= 18:
    print("Es mayor de edad")


#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6,
#  deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá 
# mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese la nota de su examen: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par
# , imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla 
# "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar 
# si un número es par o impar.

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("El número ingresado es par: ")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál 
# de las siguientes categorías pertenece: 
# ● Niño/a: menor de 12 años. 
# ● Adolescente: mayor o igual que 12 años y menor que 18 años. 
# ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
# ● Adulto/a: mayor o igual que 30 años.

edad = int(input("A continuación ingrese su edad: "))
if edad < 12:
    print("Niño/a: menor de 12 años.")
elif edad >= 12 and edad < 18:
    print("Adolescente: mayor o igual que 12 años y menor que 18 años.")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven: mayor o igual que 18 años y menor que 30 años.")
elif edad >= 30:
    print("Adulto/a: mayor o igual que 30 años.")


#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 
# caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de 
# longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una 
# contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, 
# ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
# de la función len() en Python para evaluar la cantidad de elementos que tiene 
# un iterable tal como una lista o un string.

contraseña = input("A continuación ingrese una contraseña de entre 8 y 14 caracteres:")

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)escribir un programa que tome la lista numeros_aleatorios, calcule 
# su moda, su mediana y su media y las compare para determinar si hay 
# sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

#Importo moda,mediana y media. Importo random y declaro una variable 
# con 50 numeros que se generan aleatoriamente
from statistics import mode, median, mean 
import random 
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

#Declaro las variables que guardaran los numeros de cada funcion
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

#Imprimo por pantalla la media, la mediana y la moda.
print("Media:",media)
print("Mediana:",mediana)
print("Moda:",moda)

#Comparo los numeros productos de la funcion media, mediana y moda.
if moda<mediana<media:
    print("Sesgo Positivo")
elif media<mediana<moda:
    print("Sesgo Negativo")
elif media == mediana == moda:
    print("No hay Sesgo")
else:
    print("No corresponde a un patrón de Sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante 
# por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

palabra = input("Por favor, ingrese una frase o palabra: ")

ultima_letra = (palabra[len(palabra)-1])
ultima_letra = ultima_letra.upper()

if ultima_letra == "A" or ultima_letra == "E" or ultima_letra == "I" or ultima_letra == "O" or ultima_letra == "U":
    palabra = palabra + '!'
    print(palabra.upper())
else:
    print(palabra)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada 
# por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones
# upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Por favor, ingrese su nombre")
print("Ingrese un numero a continuacion: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
numero = input()

if numero == "1":
    print(nombre.upper())
elif numero == "2":
    print(nombre.lower())
elif numero == "3":
    print(nombre.title())


#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una 
# de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud = input("Por favor, ingrese la magnitud del terremoto: ")

magnitud = float(magnitud)

if magnitud > 0 and magnitud < 3:
    print("Muy leve(imperceptible).")

elif magnitud >= 3 and magnitud < 4:
    print("Leve(ligeramente perceptible.")

elif magnitud >= 4 and magnitud < 5:
    print("Moderado(sentido por personas, pero generalmente no causa daños).")

elif magnitud >= 5 and magnitud < 6:
    print("Fuerte(puede causar daños en estructuras débiles).")

elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte(puede causar daños significativos).")
    
elif magnitud >= 7:
    print("Extremo(puede causar graves daños a gran escala ).")


# 10) Utilizando la información aportada en la siguiente tabla sobre las estaciones 
# del año Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra 
# (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información 
# para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Ingrese en que hemisferio se encuentra: ")

mes = input("Ingrese en que mes del año está: ")

dia = int(input("Ingrese en que día se encuentra: "))

if hemisferio == "sur" :
    #verano
    if mes == "diciembre" and dia >=21 and dia <= 31:
        print("es verano")
    elif mes == "enero" and dia > 0 and dia <= 31:
        print ("es verano")
    elif mes == "febrero" and dia > 0 and dia <= 28:
        print ("es verano")
    elif mes == "marzo" and dia > 0 and dia <=20:
        print ("es verano")
    #otoño
    elif mes == "marzo" and dia >= 21 and dia <=31:
        print("es otoño")
    elif mes == "abril" and dia > 0 and dia <= 30:
        print("es otoño")
    elif mes == "mayo" and dia > 0 and dia <= 31:
        print("es otoño")
    elif mes == "junio" and dia >= 0 and dia <= 20:
        print("es otoño")
    #invierno
    elif mes == "junio" and dia >= 21 and dia <= 30:
        print("es invierno")
    elif mes == "julio" and dia > 0 and dia <= 31:
        print("es invierno")
    elif mes == "agosto" and dia > 0 and dia <= 31:
        print("es invierno")
    elif mes == "septiembre" and dia > 0 and dia <= 20:
        print("es invierno")
    #primavera
    elif mes == "septiembre" and dia >= 21 and dia <= 30:
        print("es primavera")
    elif mes == "octubre" and dia > 0 and dia <= 31:
        print("es primavera")
    elif mes == "noviembre" and dia > 0 and dia <= 30:
        print("es primavera")
    elif mes == "diciembre" and dia > 0 and dia <= 20:
        print("es primavera")
    else: 
        print("Datos incorrectos! Porfavor, pruebe nuevamente.")

elif hemisferio == "norte":
    #invierno
    if mes == "diciembre" and dia >=21 and dia <= 31:
        print("es invierno")
    elif mes == "enero" and dia > 0 and dia <= 31 :
        print ("es invierno")
    elif mes == "febrero" and dia > 0 and dia <= 28 :
        print ("es invierno")
    elif mes == "marzo" and dia > 0 and dia <=20:
        print ("es invierno")
    #primavera
    elif mes == "marzo" and dia >= 21 and dia <=31:
        print("es primavera")
    elif mes == "abril" and dia > 0 and dia <= 30:
        print("es primavera")
    elif mes == "mayo" and dia > 0 and dia <= 31:
        print("es primavera")
    elif mes == "junio" and dia >= 0 and dia <= 20:
        print("es primavera")
    #verano
    elif mes == "junio" and dia >= 21 and dia <= 30:
        print("es verano")
    elif mes == "julio" and dia > 0 and dia <= 31:
        print("es verano")
    elif mes == "agosto" and dia > 0 and dia <= 31:
        print("es verano")
    elif mes == "septiembre" and dia > 0 and dia <= 20:
        print("es verano")
    #otoño
    elif mes == "septiembre" and dia >= 21 and dia <= 30:
        print("es otoño")
    elif mes == "octubre" and dia > 0 and dia <= 31:
        print("es otoño")
    elif mes == "noviembre" and dia > 0 and dia <= 30:
        print("es otoño")
    elif mes == "diciembre" and dia > 0 and dia <= 20:
        print("es otoño")
    else: 
        print("Datos incorrectos! Porfavor, pruebe nuevamente.")

else:
    print("Datos incorrectos! Porfavor, pruebe nuevamente.")