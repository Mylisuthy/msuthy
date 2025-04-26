# Sistema de Cálculo de Costo Total con Descuento

# Paso 1: Mostrar mensaje de bienvenida
print("bienvenido al Sistema de Cálculo de Costo Total con Descuento")

# Paso 2: Creamos una variable para acumular el total general
totalg = 0

# Paso 3: Preguntar cuántos productos se van a calcular
while True:
    try:
        cantidadProd = int(input("¿cuantos productos vas a comprar?: "))
        if cantidadProd > 0:
            break #se usa para salir del bucle si el caracter es valido
        else:
            print("seguro que tienes 0 productos?")
    except ValueError:
        print:("tal vez no entendi bien el numero, me lo repites po fa: ")        

# Paso 4: Repetir el proceso por cada producto
for i in range(cantidadProd):
    print(f"\ndime el producto #{i + 1}") # Mostrar el número del producto

    # Solicitar nombre del producto (que solo contenga letras y espacios)
    while True:
        nombre = input("dame el nombre del producto: ")
        if nombre.replace(" ", "").isalpha(): # Elimina espacios y verifica que sean solo letras
            break
        else:
            print("yo pienso que un nombre solo debe llevar letras, tu que opinas?: ")

    # Validar precio
    while True:
        try:
            precio = float(input("que precio tiene el producto? ($):")) # Convertimos a decimal (float)
            if precio > 0:
                break
            else:
                print("creo que dijiste mal el precio, repitemelo po favo")
        except ValueError:
            print("po favooo, ingresa un numero") # Si el dato no es numérico, mostramos error

    # Validar cantidad
    while True:
        try:
            cantidad = int(input("cantidad: ")) # Convertimos a número entero
            if cantidad > 0:
                break
            else:
                print("la cantidad cuando compras indica los productos que quieres llevarte si no te llevaras ninguno que quieres que te cobre?")
        except ValueError:
            print("por favor, dime en realidad cuantos productos quieres comprar: ")        

    # Validar descuento
    while True:
        try:
            descuento = int(input("dime el porsentage del descuento: "))
            if 0 <= descuento <= 100:
                break
            else:
                print("el descuento debe ser un numero 0 y 100...\nsi me dices que es mas que 100 o menos que 0 si se llamaria descuento?.")
        except ValueError:
            print("dime de nuevo el descuento porfa.")        

    # Calcular el costo sin descuento
    subtotal = precio * cantidad

    # Calcular el monto de descuento
    condescuento = subtotal * (descuento / 100)

    # Calcular el total con descuento
    total = subtotal - condescuento

    # Sumar al total general
    totalg += total

    # Mostrar el resultado de este producto
    print (f"entonces te vas a llevar '{cantidad}' '{nombre}' que en total te costara: ${total:.2f}")

# Mostrar el total de toda la compra
print(f"el total a pagar es: ${totalg:.2f}")

