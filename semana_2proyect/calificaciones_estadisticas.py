# Desafio de calificaciones y estadisticas:
# hecho por JuanDgonzalezH con amor y dedicacion
# este trabajo se realizo en la fecha: 1/05/2025

# Paso 1: Ingreso de una calificación individual con validación
while True:
    try:
        nota = int(input("Ingresa una calificación entre (0 a 100) por favor: "))
        if 0 <= nota <= 100:
            break
        else:
            print("El numero que ingreses debe estar entre 0 y 100.")
    except ValueError:
        print("Error: Debes ingresar un número entero válido.")

# Paso 2: Determinar estado de aprobación
if nota >= 60:
    print("nota aprobatoria.")
else:
    print("nota reprobatoria.")

# Paso 3: Ingreso de lista de calificaciones con validación
while True:
    entrada = input("\nIngresa una lista de calificaciones separadas por comas (0 a 100): ")
    partes = entrada.split(',')
    try:
        lista = [int(x.strip()) for x in partes]
        if all(0 <= x <= 100 for x in lista):
            break
        else:
            print("Todas las calificaciones deben estar entre 0 y 100.")
    except ValueError:
        print("Error: Asegúrate de ingresar solo números enteros separados por comas.")

# Cálculo del promedio usando for
suma = 0
for calificacion in lista:
    suma += calificacion
promedio = suma / len(lista)
print(f"El Promedio de las calificaciones es: {promedio:.2f}")

# Paso 4: Contar cuántas calificaciones son mayores que un valor dado
while True:
    try:
        valor = int(input("\ncual es el valor que quieres comparar (0 a 100): "))
        if 0 <= valor <= 100:
            break
        else:
            print("Por favor, ingresa un número entre 0 y 100.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

mayores = 0
indice = 0
while indice < len(lista):
    if lista[indice] > valor:
        mayores += 1
    indice += 1
print(f"Las Calificaciones mayores que {valor} son {mayores}")

# Paso 5: Verificar y contar cuántas veces aparece una calificación específica
while True:
    try:
        buscar = int(input("\ncual es la calificación que deseas buscar (0 a 100): "))
        if 0 <= buscar <= 100:
            break
        else:
            print("Por favor, ingresa un número entre 0 y 100.")
    except ValueError:
        print("Error: Debes ingresar un número válido.")

contador = 0
for nota in lista:
    if nota == buscar:
        contador += 1
        continue
print(f"La calificación {buscar} aparece {contador} veces en la lista.")

print("Gracias por usar el programa, espero fuese de tu agrado")