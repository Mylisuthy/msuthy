def obtener_dato_producto():
    # Pedir nombre del producto
    nombre_producto = input("Ingrese el nombre del producto: ")
    return nombre_producto

def obtener_precio_unitario():
    # Pedir precio unitario y validar que sea positivo
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario <= 0:
                print("El precio debe ser un número positivo. Intente nuevamente.")
            else:
                return precio_unitario
        except ValueError:
            print("Debe ingresar un número válido para el precio. Intente nuevamente.")

def obtener_cantidad():
    # Pedir cantidad y validar que sea un número entero positivo
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número entero positivo. Intente nuevamente.")
            else:
                return cantidad
        except ValueError:
            print("Debe ingresar un número entero válido para la cantidad. Intente nuevamente.")

def obtener_descuento():
    # Pedir descuento y validar que esté entre 0 y 100
    while True:
        try:
            descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido para el descuento. Intente nuevamente.")

def calcular_costo_total(precio_unitario, cantidad, descuento):
    # Calcular costo sin descuento
    costo_sin_descuento = precio_unitario * cantidad
    
    # Aplicar descuento si es necesario
    if descuento > 0:
        costo_con_descuento = costo_sin_descuento * (1 - descuento / 100)
    else:
        costo_con_descuento = costo_sin_descuento
    
    return costo_con_descuento

def mostrar_resultados(nombre_producto, costo_total):
    # Mostrar el costo total con 2 decimales
    print(f"\nEl costo total de la compra del producto '{nombre_producto}' es: ${costo_total:.2f}")

def main():
    # Obtener datos del usuario
    nombre_producto = obtener_dato_producto()
    precio_unitario = obtener_precio_unitario()
    cantidad = obtener_cantidad()
    descuento = obtener_descuento()
    
    # Calcular el costo total
    costo_total = calcular_costo_total(precio_unitario, cantidad, descuento)
    
    # Mostrar el resultado
    mostrar_resultados(nombre_producto, costo_total)

# Ejecutar el programa
if __name__ == "__main__":
    main()