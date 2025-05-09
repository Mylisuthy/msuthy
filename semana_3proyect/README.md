**Desarrollado por:** Juan David (Pk)  
**Semana:** 3 – Entrenamiento en Python  
**Proyecto:** Gestión de inventario con funciones y colecciones  
**Lenguaje:** Python 3.x  

---

## 📌 Descripción del proyecto

Este programa es un sistema de **gestión de inventario** interactivo que permite administrar productos de una tienda. Está construido usando funciones, colecciones (`diccionarios`, `tuplas`, `listas`) y programación funcional con `lambda`.

El usuario puede:

- Añadir productos con nombre, precio y cantidad
- Consultar un producto por nombre
- Mostrar todos los productos del inventario
- Actualizar el precio de un producto
- Eliminar productos con confirmación
- Calcular el valor total del inventario (precio × cantidad) usando `lambda`

---

## 🧱 Estructura del programa

El programa está organizado en funciones específicas para cada operación:

| Función | Descripción |
|--------|-------------|
| `añadir_producto()` | Añade un producto nuevo al inventario |
| `consultar_producto()` | Busca un producto y muestra su precio y cantidad |
| `mostrar_inventario()` | Lista todos los productos guardados |
| `actualizar_precio()` | Cambia el precio de un producto existente |
| `eliminar_producto()` | Permite eliminar un producto con confirmación |
| `calcular_valor_total()` | Calcula el valor total del inventario usando `lambda` |
| `pedir_dato_numerico()` | Valida la entrada numérica del usuario |

Todos los datos se almacenan en un diccionario de la forma:
```python
inventario = {
  "manzana": (1.5, 10),
  "arroz": (2.0, 5.5)
}
```
🔑 La clave es el nombre del producto.  
📦 El valor es una tupla con `(precio, cantidad)`.

---

## 🧑‍💻 Cómo usarlo

1. Ejecuta el archivo Python (`.py`).
2. Usa el menú interactivo para navegar:
```
1. Añadir producto
2. Mostrar todos los productos
3. Consultar producto
4. Actualizar precio
5. Eliminar producto
6. Calcular valor total del inventario
0. Salir
```
3. Ingresa los datos solicitados (nombre, precio, cantidad).
4. Sigue las instrucciones que aparecen en pantalla.

---

## 🚨 Manejo de errores

El programa incluye validaciones para:

- ❌ Entradas no numéricas en precio y cantidad
- 🔁 Opción no válida en el menú
- 🔎 Búsquedas de productos inexistentes
- ⚠️ Intento de duplicar productos ya existentes
- 🔙 Cancelar operaciones presionando `ENTER`
- 🛑 Confirmaciones para eliminar productos

---

## 💡 Características adicionales

✅ Permite cantidades en **kilos (float)** o **unidades (int)**  
✅ Opción para **cancelar** operaciones como eliminación y búsqueda  
✅ Uso de **funciones lambda** para el cálculo total  
✅ Modularidad, limpieza y comentarios explicativos en el código  
✅ Listo para pasar un examen de calidad de software (QA)

---

## 📂 Archivos incluidos

```
inventario.py         # Código fuente principal
README.md             # Documentación explicativa (este archivo)
```

---

## ✍️ Autor

**Juan David Gonzalez Hincapie**  
Entrenamiento Python - Semana 3
en conclucion: learn, make a mistake, fix it, repeat. (at some point the error will go away just don't give up.)