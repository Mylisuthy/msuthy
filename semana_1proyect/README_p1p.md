# Sistema de Cálculo de Costo Total con Descuento

Este proyecto implementa un programa que calcula el costo total de una compra en una tienda, teniendo en cuenta el precio unitario del producto, la cantidad de productos adquiridos y un posible descuento. El programa interactúa con el usuario para obtener los datos, valida las entradas y muestra el resultado final.

## Descripción

El programa realiza las siguientes tareas:

1. Solicita al usuario el **nombre del producto**, el **precio unitario**, la **cantidad de productos** y el **porcentaje de descuento** (si aplica).
2. Valida que el **precio** y la **cantidad** sean números positivos, y que el **descuento** esté dentro del rango permitido (0-100%).
3. Calcula el costo total de la compra, aplicando el descuento si es necesario.
4. Muestra el costo total con el símbolo `$` y con dos decimales.

## Paso a Paso del Programa

### Paso 1: Obtener el nombre del producto

La función `obtener_dato_producto()` pide al usuario que ingrese el nombre del producto. Este dato es simplemente capturado como texto.

```python
def obtener_dato_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    return nombre_producto
```

### Paso 2: Obtener el precio unitario (con validación)

La función `obtener_precio_unitario()` solicita el precio del producto, valida que sea un número positivo y maneja cualquier error de tipo de dato (si el usuario ingresa algo que no es un número).

```python
def obtener_precio_unitario():
    while True:
        try:
            precio_unitario = float(input("Ingrese el precio unitario del producto: "))
            if precio_unitario <= 0:
                print("El precio debe ser un número positivo. Intente nuevamente.")
            else:
                return precio_unitario
        except ValueError:
            print("Debe ingresar un número válido para el precio. Intente nuevamente.")
```

### Paso 3: Obtener la cantidad de productos (con validación)

La función `obtener_cantidad()` pide la cantidad de productos y valida que sea un número entero positivo.

```python
def obtener_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de productos: "))
            if cantidad <= 0:
                print("La cantidad debe ser un número entero positivo. Intente nuevamente.")
            else:
                return cantidad
        except ValueError:
            print("Debe ingresar un número entero válido para la cantidad. Intente nuevamente.")
```

### Paso 4: Obtener el porcentaje de descuento (con validación)

La función `obtener_descuento()` solicita el porcentaje de descuento y valida que esté dentro del rango de 0 a 100%.

```python
def obtener_descuento():
    while True:
        try:
            descuento = float(input("Ingrese el porcentaje de descuento (0 a 100): "))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido para el descuento. Intente nuevamente.")
```

### Paso 5: Calcular el costo total

La función `calcular_costo_total()` calcula el costo total de la compra. Primero calcula el costo sin descuento, luego si aplica un descuento, lo ajusta al costo final.

```python
def calcular_costo_total(precio_unitario, cantidad, descuento):
    costo_sin_descuento = precio_unitario * cantidad
    
    if descuento > 0:
        costo_con_descuento = costo_sin_descuento * (1 - descuento / 100)
    else:
        costo_con_descuento = costo_sin_descuento
    
    return costo_con_descuento
```

### Paso 6: Agregar el símbolo `$` al costo total

La función `agregar_simbolo_dolar()` toma el costo total y le agrega el símbolo `$`, mostrando el valor con dos decimales.

```python
def agregar_simbolo_dolar(costo_total):
    return f"${costo_total:.2f}"
```

### Paso 7: Mostrar los resultados

La función `mostrar_resultados()` muestra el costo total con el símbolo `$`, junto con el nombre del producto.

```python
def mostrar_resultados(nombre_producto, costo_total):
    costo_con_simbolo = agregar_simbolo_dolar(costo_total)
    print(f"\nEl costo total de la compra del producto '{nombre_producto}' es: {costo_con_simbolo}")
```

### Código Completo

```python
def obtener_dato_producto():
    nombre_producto = input("Ingrese el nombre del producto: ")
    return nombre_producto

def obtener_precio_unitario():
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
    costo_sin_descuento = precio_unitario * cantidad
    
    if descuento > 0:
        costo_con_descuento = costo_sin_descuento * (1 - descuento / 100)
    else:
        costo_con_descuento = costo_sin_descuento
    
    return costo_con_descuento

def agregar_simbolo_dolar(costo_total):
    return f"${costo_total:.2f}"

def mostrar_resultados(nombre_producto, costo_total):
    costo_con_simbolo = agregar_simbolo_dolar(costo_total)
    print(f"\nEl costo total de la compra del producto '{nombre_producto}' es: {costo_con_simbolo}")
```

## Recomendaciones

1. **Validación**: Siempre asegúrate de que las entradas del usuario sean válidas. El uso de ciclos `while` y el manejo de excepciones (`try-except`) son excelentes formas de asegurarte de que el programa se ejecute sin problemas.
2. **Formato de salida**: Mostrar los resultados con formato (en este caso, dos decimales y el símbolo `$`) hace que la salida sea más profesional y fácil de entender.

## Ejecutando el Programa

El código puede ejecutarse directamente desde la terminal de tu computadora. Al ejecutar el archivo, el programa te pedirá que ingreses los datos y luego te mostrará el costo total de la compra.
