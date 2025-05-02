
# 1) ¿Qué es un array o lista en Python? #
#* Un array es un espacio vacío en el código (memoria) que se puede llenar para su uso #
#* Para declarar una lista vacía # 
# Ejemp #
lista = []
# Para una lista con valores iniciales solo se debe crear la lista y definir sus valores #
lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = ["1","2","3","4","5"]
lista3 = [10, 20, 30, 40, 50]

# 2) ¿Cómo se accede a los elementos en una lista? ##
#* Para acceder al primer elemento de una lista es necesario crear un ciclo y definir cuál es su rango #
# Ejemp #
for lista1 in range(1,2):
    print (f"El primer número es {lista1}")
    print("--------------------------------------------------------------------")

#* El índice negativo es una forma de recorrer la lista en reversa, es decir -1 sería el último carácter almacenado y -2 el penúltimo
# Ejemp #
n = len(lista2)
for i in range(n-1,-1,-1):
    print(lista2[i])
    print("--------------------------------------------------------------------")

#* Si se intenta acceder a un índice que no existe, el programa dará error y te dirá que el índice no existe
# Ejemplo primer y último elemento #
lst = [10, 20, 30, 40, 50]
primelement = lst[0]
ultelement = lst[len(lst) -1]
print(f"Este es tu primer elemento {primelement}")
print("--------------------------------------------------------------------")

print(f"Este es tu último elemento {ultelement}")
print("--------------------------------------------------------------------")

# 3) ¿Qué es y cómo se usa el "slicing" o rebanado de listas? ##
#* ¿Qué es?: Es una herramienta que permite porcionar secuencias de elementos, pueden ser listas, tuplas o cadenas de texto con poco código #
# Ejemp #
(lista[::1])

#* Dejar un espacio vacío en la secuencia se refiere al inicio o el final de una secuencia respectivamente #
# Por ejemplo, si tienes una cadena de caracteres cadena = '¡Oh, gloria inmarcesible! ¡Oh, júbilo inmortal!', #
# la expresión cadena[:30] extraerá los caracteres desde el inicio hasta la posición 30 (excluida), #
# mientras que cadena[30:] extraerá los caracteres desde la posición 30 hasta el final de la cadena #
(lista[:30])
(lista[30:])
# Ejemp #
lst2 = [10,20,30,40,50,60,70,80,90,100]
elem1 = lst2 [3:7]
elem2 = lst2 [1:4]
elem3 = lst2 [2:]
print(f"Estos son los elementos del 3 al 6 {elem1} ")
print("--------------------------------------------------------------------")

print(f"Estos son los primeros 3 {elem2} ")
print("--------------------------------------------------------------------")

print(f"Estos son desde el 2 hasta el final {elem3}")
print("--------------------------------------------------------------------")

# 4) Para cambiar los elementos de una lista en Python se puede seleccionar el elemento a modificar por su índice e indicar el valor del reemplazo ##
#* Si se intenta cambiar un elemento que no existe te dará un IndexError
lst3 = [10,20,30,40,50,60]
lst3 [2] = 99 
print(lst3)
print("--------------------------------------------------------------------")

# 5) Para agregar nuevos elementos a la lista se debe usar una función que cambiará el resultado dependiendo de lo que desees hacer ##
lst4 = [10,20,30,40,50,60,70,80,90,100]
#* Para añadir elementos al final se usa append() #
# Ejemp #
lst4.append(110)
#* Para una posición específica se usa insert() #
# Ejemp #
lst4.insert(2, 25)
#* Para combinar dos listas en una se usa el operador + 
# Ejemp #
lst5 = lst3 + lst4
print(lst4)
print("--------------------------------------------------------------------")
print(lst5)
print("--------------------------------------------------------------------")

# 6) Al igual que al agregarlos se usan funciones
#* remove(): Elimina el primer elemento que coincida con el valor proporcionado. #
# Ejemp #
removido = lst5.remove(40)
#* .pop(): Elimina un elemento en un índice específico y lo devuelve, o elimina el último elemento si no se pasa índice. #
# Ejemp #
eliminado = lst5.pop(1)
#* del: Elimina un elemento en un índice específico o elimina toda la lista. #
# Ejemp #  ///si quieres eliminar toda la lista no le debes poner índice///
del lst5[6]
#* clear(): Elimina todos los ítems de la lista dejándola vacía, pero no deja de existir #
# Ejemp #
lst6 = [10,20,30,40,50,60,70,80,90,]
lst6.clear()

print(lst5)
print("--------------------------------------------------------------------")
print(lst6)
print("--------------------------------------------------------------------")

# 7) Se usa un ciclo for para recorrer la lista y con False o True se identifica el carácter # 
#* in: Verifica si un elemento está en la lista, este devuelve True o False #
#* index(): Devuelve el índice de la primera aparición de un elemento, lanza un ValueError si no lo encuentra. #
#* for: Puedes recorrer la lista manualmente y realizar acciones cuando encuentras un elemento. #
#* Expresión de lista: Permite filtrar elementos que cumplen un criterio. #
# Ejemp #
busqueda = 30
encontrado = False
for elemento in lst3:
    if elemento == busqueda:
        encontrado = True
        break
if encontrado:
    print(f"El elemento {busqueda} sí se encuentra en la lista")
else:
    print(f"El elemento que buscas no se encuentra en la lista")
print("--------------------------------------------------------------------")

#* Para saber el índice se usa la función index() #
# Ejemp #
indice = lst5.index(30)
print(f"El índice de 30 se encuentra en la posición {indice}")
print("--------------------------------------------------------------------")

#* Para contar cuántas veces aparece un valor se usa count() #
# Ejemp #
cantidad = lst5.count(2)
print(f"Hay {cantidad} elementos en la lista")
print("--------------------------------------------------------------------")

# 8) Para ordenar elementos en una lista se usan funciones como: sort(), sorted(). #
# Para una lista ordenada de forma ascendente (menor a mayor) se puede usar sort() o sorted() #
# Siendo su diferencia principal cómo afecta a la lista #
# sort(): Ordena la lista en el lugar, lo que significa que cambia la lista original, no devuelve nada, solo modifica la lista #
# sorted(): Crea una lista ordenada y deja la lista original sin cambios #
# Para ordenar en orden descendente se usan las funciones ya mencionadas con el añadido de reverse = True #
# Ejemp # 
# Lista original
lista4 = [40, 10, 30, 20]

# 1. Ordenar en orden ascendente usando sort()
lista4.sort()  # Modifica la lista4 original
print(f"Ordenada en orden ascendente con sort(): {lista4}")
print("--------------------------------------------------------------------")

# 2. Ordenar en orden descendente usando sort()
lista4.sort(reverse=True)  # Modifica la lista4 original
print(f"Ordenada en orden descendente con sort(): {lista4}")
print("--------------------------------------------------------------------")

# 3. Ordenar en orden ascendente usando sorted()
# Esto no modifica la lista4 original, sino que crea una nueva lista4 ordenada.
lista4_original = [40, 10, 30, 20]
lista4_ascendente = sorted(lista4_original)  # Crea una nueva lista4 ordenada
print(f"Lista4 original sin modificar: {lista4_original}")
print("--------------------------------------------------------------------")
print(f"Ordenada en orden ascendente con sorted(): {lista4_ascendente}")
print("--------------------------------------------------------------------")

# 4. Ordenar en orden descendente usando sorted()
# También crea una nueva lista4 ordenada en orden descendente.
lista4_descendente = sorted(lista4_original, reverse=True)  # Crea una nueva lista4 ordenada
print(f"Ordenada en orden descendente con sorted(): {lista4_descendente}")
print("--------------------------------------------------------------------") 

# 9) ¿Cómo invertimos el orden de los elementos de una lista? #
#* Se puede invertir el orden de una lista de dos formas comunes: usando reverse() o usando slicing [::-1] #
#* reverse(): Invierte la lista original directamente, no devuelve una nueva lista #
# Ejemp #
lista5 = [10, 20, 30, 40]
lista5.reverse()
print(f"Lista invertida con reverse(): {lista5}")
print("--------------------------------------------------------------------")
#* slicing [::-1]: Crea una nueva lista invertida sin modificar la original #
# Ejemp #
lisoriginal = [10, 20, 30, 40]
lisinvertida = lisoriginal[::-1]
print(f"Lista original: {lisoriginal}")
print("--------------------------------------------------------------------")
print(f"Lista invertida con slicing: {lisinvertida}")
print("--------------------------------------------------------------------")

# 10) ¿Cómo hacemos una copia de una lista? #
#* Existen varias formas de copiar una lista en Python sin modificar la original. Las más comunes son: slicing, list() y copy() #
#* slicing [:]: Crea una copia de toda la lista #
# Ejemp #
lista6 = [10, 20, 30]
copia1 = lista6[:]
print(f"Copia con slicing: {copia1}")
print("--------------------------------------------------------------------")
#* list(): Crea una nueva lista a partir de otra #
# Ejemp #
lista7 = [10, 20, 30]
copia2 = list(lista7)
print(f"Copia con list(): {copia2}")
print("--------------------------------------------------------------------")
#* copy(): Método propio de listas para hacer una copia #
# Ejemp #
lista8 = [10, 20, 30]
copia3 = lista8.copy()
print(f"Copia con copy(): {copia3}")
print("--------------------------------------------------------------------")

# 11) ¿Cómo comprobamos si una lista está vacía? #
#* Podemos verificar si una lista no contiene elementos usando una condición con if #
#* Una lista vacía se evalúa como False, por lo tanto, si no tiene elementos, la condición se cumple #
# Ejemp #
lisvacia = []
if not lisvacia:
    print("La lista está vacía")
else:
    print("La lista tiene elementos")
print("--------------------------------------------------------------------")

# 12) ¿Cómo pedir varios datos al usuario y almacenarlos en una lista? #
#* Para pedir varios datos al usuario se puede usar la función input() dentro de un ciclo #
#* Primero se pregunta cuántos elementos quiere ingresar #
#* Luego se usa un ciclo for para pedir cada dato y agregarlos a una lista con append() #
# Ejemp #
listusuario = []
# Preguntar cuántos elementos desea ingresar
cantidad = int(input("¿Cuántos elementos quieres ingresar?: "))
# Usar un ciclo for para ingresar los elementos uno por uno
for i in range(cantidad):
    elemento = input(f"Ingrese el elemento {i+1}: ")
    listusuario.append(elemento)
# Mostrar la lista completa
print(f"Los elementos que ingresaste son: {listusuario}")
print("--------------------------------------------------------------------")    

# Eso es todo #