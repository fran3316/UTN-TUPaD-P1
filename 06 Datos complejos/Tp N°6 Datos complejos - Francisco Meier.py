#Actividad 1 - Añadir frutas al diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

#Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Actividad 2 - Actualizar precios de frutas

#Actualizar precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Actividad 3 - Crear una lista solo con las frutas (sin precios)

lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

#Actividad 4 - Programa de agenda telefónica

#Crear diccionario para almacenar contactos
contactos = {}

#Cargar 5 contactos
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número telefónico: ")
    contactos[nombre] = telefono

#Consultar un contacto
consulta = input("\nIngrese el nombre a buscar: ")
if consulta in contactos:
    print(f"El número de {consulta} es: {contactos[consulta]}")
else:
    print("No se encontro al contacto!")

#Actividad 5 - Análisis de palabras en una frase

# Solicitar frase al usuario
frase = input("Ingrese una frase: ")

#Convertir a lista de palabras (separadas por espacios)
palabras = frase.split()

#Palabras únicas (usando set)
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

#Diccionario con recuento de cada palabra
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra, 0) + 1  # Si no existe, inicializa en 0
print("Recuento:", recuento)

#Actividad 6 - Promedio de notas de alumnos

#Diccionario para almacenar alumnos y notas
alumnos = {}

#Ingresar datos de 3 alumnos
for i in range(3):
    nombre = input(f"\nNombre del alumno {i+1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)  # Guardar como tupla

#Calcular y mostrar promedios
print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Actividad 7 - Operaciones con Sets 

#Sets de estudiantes que aprobaron cada parcial
parcial1 = {"Juan", "María", "Pedro", "Ana"}
parcial2 = {"Ana", "Luis", "María", "Carlos"}

#A)Estudiantes que aprobaron AMBOS parciales (intersección)
aprobados_ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", aprobados_ambos)  # Salida: {'María', 'Ana'}

#B)Estudiantes que aprobaron SOLO UNO (diferencia simétrica)
aprobados_solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno:", aprobados_solo_uno)  # Salida: {'Juan', 'Pedro', 'Luis', 'Carlos'}

#C)Total de estudiantes que aprobaron AL MENOS UN parcial (unión)
aprobados_al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos uno:", aprobados_al_menos_uno)  # Salida: {'Juan', 'María', 'Pedro', 'Ana', 'Luis', 'Carlos'}

#Actividad 8 - Gestión de Stock con Diccionarios

#Diccionario inicial de productos y stock
stock = {
    "Manzanas": 50,
    "Bananas": 30,
    "Peras": 20
}

def gestion_stock():
    producto = input("\nIngrese el nombre del producto: ").strip().title()
    
    #Consultar stock
    if producto in stock:
        print(f"Stock actual de {producto}: {stock[producto]} unidades")
        opcion = input("¿Desea agregar unidades? (s/n): ").lower()
        if opcion == 's':
            unidades = int(input("Cantidad a agregar: "))
            stock[producto] += unidades
            print(f"Stock actualizado: {stock[producto]} unidades")
    else:
        print("Producto no encontrado. ¿Desea agregarlo? (s/n): ")
        opcion = input().lower()
        if opcion == 's':
            unidades = int(input("Stock inicial: "))
            stock[producto] = unidades
            print(f"Producto '{producto}' añadido con {unidades} unidades.")

#Ejecutar la gestión
while True:
    print("\n--- Gestión de Stock ---")
    print("1. Consultar/Añadir stock")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        gestion_stock()
    elif opcion == '2':
        print("Stock final:", stock)
        break

#Actividad 9 - Agenda con Tuplas como Claves

#Crear la agenda inicial
agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Taller de programación"
}

def consultar_agenda():
    print("\n--- Consultar Agenda ---")
    dia = input("Ingrese el día (ej: lunes): ").strip().lower()
    hora = input("Ingrese la hora (ej: 15:00): ").strip()
    
    clave = (dia, hora)
    if clave in agenda:
        print(f"Evento: {agenda[clave]}")
    else:
        print("No hay eventos programados para ese día y hora.")

#Menú interactivo
while True:
    print("\n--- Agenda de Eventos ---")
    print("1. Consultar evento")
    print("2. Salir")
    opcion = input("Seleccione una opción (1/2): ")
    
    if opcion == '1':
        consultar_agenda()
    elif opcion == '2':
        print("nos vemos!")
        break

#Actividad 10 - Invertir un Diccionario (Claves ↔ Valores)

# Diccionario original: países → capitales
original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo"
}

#Invertir el diccionario: capitales → países
invertido = {capital: pais for pais, capital in original.items()}

print("Diccionario invertido:", invertido)
