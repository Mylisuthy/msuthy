# 🧾 Inventory Management System

**Author:** juanch0 (Coder at Riwi Medellín, clan Linus)  
**Language:** Python 3  
**Interface:** Terminal (Recommended in Visual Studio Code)

---

## 📌 Description

This is a terminal-based interactive Inventory Management System designed to help users manage product stock in a store. It enables the addition, display, search, update, and deletion of products, as well as calculating the total value of all inventory items. It was built to reinforce concepts of functions, dictionaries, input validation, and lambda functions in Python.

---

## ⚙️ Features

- ✅ Add products with a name, price, quantity, and unit type (either kilograms or units).
- 📋 Show all products currently stored in the inventory.
- 🔍 Search for a specific product by name and view its details.
- 🔁 Update the price of any existing product.
- ❌ Remove products from the inventory with user confirmation.
- 💰 Calculate the **total inventory value** using a lambda-powered expression.

---

## 🧠 Data Structures Used

- **Main structure:** A `dictionary` named `inventory`, where:
  - The **key** is the product name (string).
  - The **value** is a tuple: `(price: float, quantity: float/int, unit_type: str)`.

- **Input validation:** Custom numeric input validation functions to ensure data integrity.

- **Lambda function:** Used to calculate total inventory value concisely.

---

## 🛒 Sample Inventory

```python
inventory = {
    "rice": (2.90, 25.0, "kg"),
    "eggs": (0.20, 60, "units"),
    "milk": (1.10, 18.0, "kg"),
    "bread": (1.25, 30, "units"),
    "sugar": (2.50, 10.0, "kg"),
    "apples": (1.80, 12.5, "kg"),
    "oranges": (2.00, 8.0, "kg"),
    "water bottles": (0.90, 24, "units"),
    "flour": (1.60, 15.0, "kg"),
    "cheese": (3.75, 5.0, "kg")
}
```

---

## 📂 Main Functions

- `normalize_name(name)`: Cleans and standardizes product names.
- `is_float(value)`: Checks if a value is a valid float.
- `request_numeric_data(...)`: Prompts and validates numeric input.
- `add_item(...)`: Adds a product to the inventory.
- `show_all_items()`: Displays all inventory items.
- `consulter_item(name)`: Displays the details of a specific item.
- `update_price(name, new_price)`: Updates the price of an item.
- `remove_item(name)`: Deletes an item with confirmation.
- `calculate_total_value()`: Computes total inventory value.

---

## 🖥️ How to Use

1. Run the script using Python in a terminal (recommended: Visual Studio Code).
2. Use the interactive menu to manage the inventory:
   ```
   1. Add product
   2. Show all products
   3. Consult product
   4. Update price
   5. Remove product
   6. Calculate total value
   0. Exit
   ```
3. Follow on-screen prompts for each action. Inputs are validated to avoid errors.

---

## 🏁 Final Notes

- This project is part of an educational exercise at **Riwi Medellín**.
- It's designed for learners with basic Python knowledge (Week 3 level).
- The code is modular, clear, and ready to be expanded (e.g., with persistence using JSON, logs, or a GUI).

---

## ✍️ Autor

**Juan David Gonzalez Hincapie**  
Entrenamiento Python - Semana 3
en conclucion: learn, make a mistake, fix it, repeat. (at some point the error will go away just don't give up.)
