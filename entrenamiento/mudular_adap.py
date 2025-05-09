# Diccionario global del inventario
# Clave = nombre del producto, valor = tupla (precio, cantidad, tipo)
# El tipo puede ser "kg" (kilogramos) o "u" (unidades)
inventario = {}

# Función que solicita un número al usuario y valida su formato
def solicitar_dato_numerico(mensaje, es_entero=False, permitir_negativo=True, valor_minimo=None, valor_maximo=None):
    while True:
        entrada = input(mensaje)
        try:
            valor = int(entrada) if es_entero else float(entrada)
            if not permitir_negativo and valor < 0:
                print("No se permiten valores negativos. Por favor, ingrese un número válido.")
                continue
            if valor_minimo is not None and valor < valor_minimo:
                print(f"El valor debe ser al menos {valor_minimo}.")
                continue
            if valor_maximo is not None and valor > valor_maximo:
                print(f"El valor no puede exceder {valor_maximo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número correcto.")

# Agrega un producto al inventario si no existe
def agregar_producto(nombre, precio, cantidad, tipo):
    if nombre in inventario:
        print("El producto ya existe en el inventario.")
    else:
        inventario[nombre] = (precio, cantidad, tipo)
        print(f"Producto '{nombre}' agregado exitosamente.")

# Muestra todos los productos disponibles en el inventario
def mostrar_todos_los_productos():
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for nombre, (precio, cantidad, tipo) in inventario.items():
            unidad = "kg" if tipo == "kg" else "unidades"
            print(f" {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad} {unidad}")

# Muestra la información de un producto específico
def consultar_producto(nombre):
    producto = inventario.get(nombre)
    if producto:
        precio, cantidad, tipo = producto
        print(f\"\"\"
{'-'*60}
        Producto: {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad} {'kg' if tipo == 'kg' else 'unidades'}
{'-'*60}
\"\"\")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

# Actualiza el precio de un producto existente
def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        _, cantidad, tipo = inventario[nombre]
        inventario[nombre] = (nuevo_precio, cantidad, tipo)
        print(f"Precio actualizado para '{nombre}'. Nuevo precio: ${nuevo_precio:.2f}")
    else:
        print("Producto no encontrado en el inventario.")

# Elimina un producto del inventario con confirmación
def eliminar_producto(nombre):
    if nombre in inventario:
        confirmacion = input(f"¿Está seguro de que desea eliminar '{nombre}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            del inventario[nombre]
            print(f"Producto '{nombre}' eliminado exitosamente.")
        else:
            print("Operación cancelada.")
    else:
        print(f"Producto '{nombre}' no encontrado en el inventario.")

# Calcula el valor total del inventario (precio * cantidad)
def calcular_valor_total():
    total = sum(precio * cantidad for precio, cantidad, _ in inventario.values())
    print(f"Valor total del inventario: ${total:.2f}")

# Crea la base de datos SQLite y la tabla si no existe
def crear_base_de_datos():
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute(\"\"\"
CREATE TABLE IF NOT EXISTS inventario (
    nombre TEXT PRIMARY KEY,
    precio REAL,
    cantidad REAL,
    tipo TEXT
)
\"\"\")
    conn.commit()
    conn.close()

# Guarda o actualiza un producto en la base de datos
def agregar_producto_a_db(nombre, precio, cantidad, tipo):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute(\"\"\"
INSERT OR REPLACE INTO inventario (nombre, precio, cantidad, tipo)
VALUES (?, ?, ?, ?)
\"\"\", (nombre, precio, cantidad, tipo))
    conn.commit()
    conn.close()

# Muestra los productos directamente desde la base de datos
def mostrar_inventario_de_db():
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute('SELECT * FROM inventario')
    productos = c.fetchall()
    for producto in productos:
        nombre, precio, cantidad, tipo = producto
        unidad = "kg" if tipo == "kg" else "unidades"
        print(f" {nombre} | Precio: ${precio:.2f} | Cantidad: {cantidad} {unidad}")
    conn.close()

# Menú principal que presenta las opciones al usuario
def menu():
    print(f\"\"\"
{'-'*60}
                Sistema de Gestión de Inventario
{'-'*60}
                1. Agregar producto
                2. Mostrar todos los productos
                3. Consultar producto
                4. Actualizar precio
                5. Eliminar producto
                6. Calcular valor total
                7. Mostrar inventario desde la base de datos
                8. Salir
{'-'*60}
\"\"\")

# Función principal que ejecuta el ciclo del menú
def principal():
    crear_base_de_datos()
    while True:
        menu()
        try:
            opcion = int(input("Ingresa una opción (1-8): "))
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entre 1 y 8.")
            continue

        if opcion == 1:
            nombre = input("Ingresa el nombre del producto: ").strip().lower()
            precio = solicitar_dato_numerico("Ingresa el precio del producto: ")
            while True:
                tipo_unidad = input("¿Cantidad en kilogramos (K) o unidades (U)? [K/U]: ").strip().lower()
                if tipo_unidad == "k":
                    cantidad = solicitar_dato_numerico("Ingresa la cantidad en kilogramos: ")
                    unidad = "kg"
                    break
                elif tipo_unidad == "u":
                    cantidad = solicitar_dato_numerico("Ingresa la cantidad en unidades: ", es_entero=True)
                    unidad = "u"
                    break
                else:
                    print("Tipo de unidad no válido. Por favor, ingresa 'K' o 'U'.")

            agregar_producto(nombre, precio, cantidad, unidad)
            agregar_producto_a_db(nombre, precio, cantidad, unidad)

        elif opcion == 2:
            mostrar_todos_los_productos()

        elif opcion == 3:
            nombre = input("Ingresa el nombre del producto: ").strip().lower()
            consultar_producto(nombre)

        elif opcion == 4:
            nombre = input("Ingresa el nombre del producto: ").strip().lower()
            nuevo_precio = solicitar_dato_numerico("Ingresa el nuevo precio: ")
            actualizar_precio(nombre, nuevo_precio)
            if nombre in inventario:
                agregar_producto_a_db(nombre, nuevo_precio, inventario[nombre][1], inventario[nombre][2])

        elif opcion == 5:
            nombre = input("Ingresa el nombre del producto: ").strip().lower()
            eliminar_producto(nombre)
            conn = sqlite3.connect('inventario.db')
            c = conn.cursor()
            c.execute('DELETE FROM inventario WHERE nombre = ?', (nombre,))
            conn.commit()
            conn.close()

        elif opcion == 6:
            calcular_valor_total()

        elif opcion == 7:
            mostrar_inventario_de_db()

        elif opcion == 8:
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, ingresa un número del 1 al 8.")

if __name__ == "__main__":
    principal()

# ------------------------------------------------------------------
# EXPLICACIÓN FINAL DE FUNCIONES Y BLOQUES PRINCIPALES:
# ------------------------------------------------------------------
# solicitar_dato_numerico: Solicita y valida entrada numérica (int o float), con límites opcionales.
# agregar_producto: Agrega un nuevo producto al diccionario del inventario.
# mostrar_todos_los_productos: Lista todo el contenido del inventario.
# consultar_producto: Muestra la información de un solo producto.
# actualizar_precio: Cambia el precio de un producto manteniendo sus demás datos.
# eliminar_producto: Elimina un producto del inventario tras confirmación.
# calcular_valor_total: Suma el valor total de todos los productos (precio * cantidad).
# crear_base_de_datos: Inicializa la base de datos SQLite.
# agregar_producto_a_db: Inserta o actualiza un producto en la base de datos.
# mostrar_inventario_de_db: Recupera todos los productos desde la base de datos y los muestra.
# menu: Imprime las opciones del sistema.
# principal: Ejecuta el flujo del programa controlando las opciones del usuario.
