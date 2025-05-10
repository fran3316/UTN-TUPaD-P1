# 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. 
# Utilizar la función range.

lista = list(range(4,101,4)) #crea la lista
print(lista) #la imprime

# 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) 
# y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar 
# cómo funciona el indexing con números negativos!


animales = ["Vaca","Chancho", "Caballo", "Gato", "Perro"] #creo la lista
print(animales[-5]) # imprime vaca

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la 
# lista resultante por pantalla. Pista: para crear una lista vacía debes 
# colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

frutas = [] # crea una lista vacia 

#agrego tres elementos a la lista  con la funcion .append
frutas.append("Pera")
frutas.append("Manzana")
frutas.append("Naranja")

print(frutas) # imprimo la lista

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras 
# “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"] #Creo una lista con 4 elementos

#modifico dos de sus elementos
animales[-3] = "loro"
animales[-1] = "oso"

print(animales) #imprimo la lista#

# 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras 
# “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona 
# el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]

animales = ["perro", "gato", "conejo", "pez"] #Creo una lista con 4 elementos

#modifico dos de sus elementos
animales[-3] = "loro"
animales[-1] = "oso"

print(animales) #imprimo la lista

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
numeros = [8, 15, 3, 22, 7] # crea una lista con 5 elementos 
numeros.remove(max(numeros)) # Elimina de mi lista el mayor de los numeros con la funcion remove 
                             # y la funcion max que devuelve el mayor de los numeros de la lista numeros
                             #, en este caso el 22

#6) Crear una lista con números del 10 al 30 (incluído), 
# haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

lista_numeros = list(range(10,31,5)) # creo la lista 
print(lista_numeros[0:2]) # muestro por pantalla los dos primeros

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos”   
# por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

autos = ["sedan", "polo", "suran", "gol"] #creo una lista con 4 elementos

#modifico 2 de sus elementos 
autos[1]= "siena"
autos[2]= "corolla"

#imprime por pantalla la lista
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 
# usando append directamente. Imprimir la lista resultante por pantalla.

#creo una lista vacia
dobles = []

#agrega a la lista el doble de 5,10 y 15
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

#imprime la lista
print(dobles)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# c) Eliminar "pan" de la lista del primer cliente.
# d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

# 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

#creo dos listas vacias una que sera la lista principal y 
# la otra, que la utilizare como sublista que se llama lista_vacia
lista_anidada = []
lista_vacia = []

#agrego elementos a mi lista principal y sublista
lista_anidada.append(15) 
lista_anidada.append(True)
lista_anidada.append(lista_vacia)
lista_anidada[2].append(25.5)
lista_anidada[2].append(57.9) 
lista_anidada[2].append(30.6)
lista_anidada.append(False) 

#imprimo mi lista principal
print(lista_anidada)