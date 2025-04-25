# 💸 Sistema de Cálculo de Costo Total con Descuento

Este es un programa desarrollado en Python para calcular el costo total de varios productos aplicando descuentos personalizados.

---

## 🚀 Características

- Solicita datos del usuario (nombre del producto, precio, cantidad, descuento).
- Valida entradas numéricas y rangos válidos.
- Calcula el costo total aplicando el descuento.
- Muestra resultados con formato en dólares y dos decimales.
- Permite calcular múltiples productos en una sola ejecución.

---

## 📦 ¿Cómo usar el programa?

1. Ejecuta el script en un entorno que permita entrada de datos (como VS Code, IDLE, o consola).
2. Ingresa la cantidad de productos que deseas registrar.
3. Introduce los datos que el sistema solicita.
4. El programa mostrará el total por producto y el total final.

---

## ✅ Recomendaciones

- Asegúrate de ingresar **números válidos** (positivos) para el precio y la cantidad.
- El **descuento** debe estar entre **0 y 100**.
- Si cometes un error al ingresar datos, el sistema te pedirá que lo intentes de nuevo.

---

## 🐞 Posibles errores y cómo se corrigieron

| Error detectado | Cómo se comprobó | Solución aplicada |
|-----------------|------------------|-------------------|
| Ingresar texto en lugar de número | Se probó ingresando letras en lugar de números | Uso de `try-except` para capturar errores con `ValueError` |
| Ingreso de números negativos | Se ingresaron valores como -5 para probar | Condicionales `if` dentro de bucles `while` para validar valores positivos |
| Descuento fuera del rango | Se intentó con descuentos mayores a 100 o negativos | Validación con `if 0 <= descuento <= 100` |

---

## 📚 Tecnologías utilizadas

- Lenguaje: **Python**
- Entrada/Salida: Consola
- Funcionalidades usadas: `input()`, `float()`, `int()`, `if`, `else`, `elif`, `while`, `for`, `try-except`, `print()`, `isalpha()`, `replace()`, operadores lógicos y aritméticos.

---

## 🧑‍💻 Autor

Desarrollado con pasión por JuanDGonzalezH – coder de programación en RiWi 🚀

---

## concluciones

> ¡Sigue aprendiendo, sigue construyendo! Cada línea de código es un paso más cerca de dominar el arte de programar. 💻✨
