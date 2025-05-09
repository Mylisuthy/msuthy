# inventario: diccionario global
# clave = nombre del producto, valor = tupla (precio, cantidad, tipo)
# tipo puede ser "kg" o "u" (kilos o unidades)
inventory = {}

def request_numeric_data(message, is_integer=False):
    """ Solicita al usuario un dato numérico válido. Puede ser float o int. """
    while True:
        entry = input(message)
        try:
            return int(entry) if is_integer else float(entry)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_item(name, price, quantity, unit_type):
    """ Agrega un producto al inventario, si no existe aún. """
    if name in inventory:
        print("The item already exists in the inventory.")
    else:
        inventory[name] = (price, quantity, unit_type)
        print(f"Item '{name}' added successfully.")

def show_all_items():
    """ Muestra todos los productos del inventario con sus datos. """
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for name, (price, quantity, unit_type) in inventory.items():
            unidad = "kg" if unit_type == "kg" else "units"
            print(f" {name} | Price: ${price:.2f} | Quantity: {quantity} {unidad}")

def consulter_item(name):
    """ Consulta un ítem específico por nombre. """
    product = inventory.get(name)
    if product:
        precio, cantidad, tipo = product
        print(f"""
{'-'*60}
        Product: {name} | Price: ${precio:.2f} | Quantity: {cantidad} {'kg' if tipo == 'kg' else 'units'}
{'-'*60}
        """)
    else:
        print(f"Item '{name}' not found in inventory.")

def update_price(name, new_price):
    """ Actualiza el precio de un producto existente. """
    if name in inventory:
        _, quantity, unit_type = inventory[name]
        inventory[name] = (new_price, quantity, unit_type)
        print(f"Price updated for '{name}'. New price: ${new_price:.2f}")
    else:
        print("Product not found in inventory.")

def remove_item(name):
    """ Elimina un producto con confirmación del usuario. """
    if name in inventory:
        confirmation = input(f"Are you sure you want to remove '{name}'? (y/n): ").strip().lower()
        if confirmation == "y":
            del inventory[name]
            print(f"Item '{name}' removed successfully.")
        else:
            print("Operation canceled.")
    else:
        print(f"Item '{name}' not found in inventory.")

def calculate_total_value():
    """ Calcula el valor total del inventario. """
    total = sum(price * quantity for price, quantity, _ in inventory.values())
    print(f"Total value of inventory: ${total:.2f}")

def menu():
    """ Imprime el menú de opciones. """
    print(f"""
{'-'*60}
                Inventory Management System
{'-'*60}
                1. Add item
                2. Show all items
                3. Consult item
                4. Update price
                5. Remove item
                6. Calculate total value
                0. Exit
{'-'*60}
    """)

def main():
    while True:
        menu()
        try:
            option = int(input("Enter an option (0-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue

        if option == 1:
            print("Add item".center(60, "-"))
            name = input("Enter item name (or press Enter to cancel): ").strip().lower()
            if not name:
                print("Operation canceled.")
                continue

            price = request_numeric_data("Enter item price: ")
            while True:
                unit_type = input("Quantity in kilograms (K) or units (U)? [K/U]: ").strip().lower()
                if unit_type == "k":
                    quantity = request_numeric_data("Enter quantity in kilograms: ")
                    unit = "kg"
                    break
                elif unit_type == "u":
                    quantity = request_numeric_data("Enter quantity in units: ", is_integer=True)
                    unit = "u"
                    break
                else:
                    print("Invalid unit type. Please enter 'K' for kilograms or 'U' for units.")

            add_item(name, price, quantity, unit)

        elif option == 2:
            print("Show all items".center(60, "-"))
            show_all_items()

        elif option == 3:
            print("Consult item".center(60, "-"))
            name = input("Enter the name of the item: ").strip().lower()
            if not name:
                print("Name cannot be empty.")
                continue
            consulter_item(name)

        elif option == 4:
            print("Update price".center(60, "-"))
            name = input("Enter the name of the item to update (enter to exit): ").strip().lower()
            if not name:
                print("Name cannot be empty.")
                continue
            new_price = request_numeric_data("Enter the new price: ")
            update_price(name, new_price)

        elif option == 5:
            print("Remove item".center(60, "-"))
            name = input("Enter the name of the item: ").strip().lower()
            if not name:
                print("Name cannot be empty.")
                continue
            remove_item(name)

        elif option == 6:
            print("Calculate total value".center(60, "-"))
            calculate_total_value()

        elif option == 0:
            print("Exiting the program...")
            break

        else:
            print("Invalid option. Please enter a number from 0 to 6.")

if __name__ == "__main__":
    main()
