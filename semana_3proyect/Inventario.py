#
Program: Inventory Management System
Author: juanch0 (Coder of Riwi Medellín clan linus) 
Description:
This program allows to manage the inventory of a store interactively from the VS Code terminal.
Functionalities:
- Add products to the inventory with name, price, quantity and unit type (kg or units).
- View all stored products
- Search for a specific product and view its details
- Update the price of an existing product
- Remove products from inventory with user confirmation
- Calculate total inventory value using lambda functions.

Structures used:
- Main dictionary `inventory` where the key is the product name and the value is a tuple (price, quantity, unit_type).

- Constant interaction through a menu displayed in the terminal.
#
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

# Function to normalize product names
def normalize_name(name):
    """ Converts the name to lowercase and removes leading/trailing spaces. """
    return name.strip().lower()

# Function to check if a string represents a valid float
def is_float(value):
    """ Checks if the string can be converted to a float. """
    if value.count(".") == 1:
        left, right = value.split(".")
        return left.replace("-", "").isdigit() and right.isdigit()
    return value.isdigit() or (value.startswith("-") and value[1:].isdigit())

# Function to request numeric input with validation
def request_numeric_data(message, is_integer=False, allow_negative=True, min_value=None):
    """ Requests numeric input with explicit validation. """
    while True:
        entry = input(message).strip()
        
        if not entry:
            print("Input cannot be empty. Try again.")
            continue

        if is_integer:
            if not (entry.lstrip("-").isdigit() and (allow_negative or not entry.startswith("-"))):
                print("Invalid input. Please enter a valid integer.")
                continue
            value = int(entry)
        else:
            if not is_float(entry):
                print("Invalid input. Please enter a valid decimal number.")
                continue
            value = float(entry)

        if not allow_negative and value < 0:
            print("Negative values are not allowed. Try again.")
            continue

        if min_value is not None and value < min_value:
            print(f"The value must be at least {min_value}. Try again.")
            continue

        return value

# Function to add products
def add_item(name, price, quantity, unit_type):
    """ Adds a product to the inventory if it doesn't already exist. """
    name = normalize_name(name)
    if name in inventory:
        print("The product already exists in the inventory.")
    else:
        inventory[name] = (price, quantity, unit_type)
        print(f"Product '{name}' added successfully.")

# Function to display all products
def show_all_items():
    """ Displays all products in the inventory with details. """
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for name, (price, quantity, unit_type) in inventory.items():
            print(f" {name} | Price: ${price:.2f} | Quantity: {quantity} {unit_type}")

# Function to consult a specific product
def consulter_item(name):
    """ Searches for a product by its name. """
    name = normalize_name(name)
    product = inventory.get(name)
    if product:
        price, quantity, unit_type = product
        print(f"""
{'-'*60}
        Product: {name} | Price: ${price:.2f} | Quantity: {quantity} {unit_type}
{'-'*60}
        """)
    else:
        print(f"Product '{name}' not found in the inventory.")

# Function to update the price of a product
def update_price(name, new_price):
    """ Updates the price of an existing product. """
    name = normalize_name(name)
    if name in inventory:
        _, quantity, unit_type = inventory[name]
        inventory[name] = (new_price, quantity, unit_type)
        print(f"Price updated for '{name}'. New price: ${new_price:.2f}")
    else:
        print("Product not found in the inventory.")

# Function to remove a product
def remove_item(name):
    """ Removes a product from the inventory with confirmation. """
    name = normalize_name(name)
    if name in inventory:
        confirmation = input(f"Are you sure you want to delete '{name}'? (y/n): ").strip().lower()
        if confirmation == "y":
            del inventory[name]
            print(f"Product '{name}' removed successfully.")
        else:
            print("Operation canceled.")
    else:
        print(f"Product '{name}' not found in the inventory.")

# Function to calculate the total inventory value
def calculate_total_value():
    """ Calculates and displays the total value of the inventory. """
    total = sum(price * quantity for price, quantity, _ in inventory.values())
    print(f"Total inventory value: ${total:.2f}")

# Main program loop
while True:
    print(f"""
{'-'*60}
                Inventory Management System
{'-'*60}
                1. Add product
                2. Show all products
                3. Consult product
                4. Update price
                5. Remove product
                6. Calculate total value
                0. Exit
{'-'*60}
    """)

    option = input("Enter an option (0-6): ").strip()

    if not option.isdigit() or int(option) < 0 or int(option) > 6:
        print("Invalid option. Please enter a number between 0 and 6.")
        continue

    option = int(option)

    if option == 1:
        print("Add Product".center(60, "-"))
        name = input("Enter the product name (or press Enter to cancel): ").strip()
        if not name or name.isspace():
            print("Operation canceled.")
            continue
        price = request_numeric_data("Enter the product price: ", allow_negative=False, min_value=0.01)
        while True:
            unit_type = input("Quantity in kilograms (K) or units (U)? [K/U]: ").strip().lower()
            if unit_type == "k":
                quantity = request_numeric_data("Enter the quantity in kilograms: ", allow_negative=False, min_value=0.01)
                unit = "kg"
                break
            elif unit_type == "u":
                quantity = request_numeric_data("Enter the quantity in units: ", is_integer=True, allow_negative=False, min_value=1)
                unit = "units"
                break
            else:
                print("Invalid unit type. Type 'K' for kilograms or 'U' for units.")
        add_item(name, price, quantity, unit)

    elif option == 2:
        print("Show All Products".center(60, "-"))
        show_all_items()

    elif option == 3:
        print("Consult Product".center(60, "-"))
        name = input("Enter the product name: ").strip()
        if not name or name.isspace():
            print("The name cannot be empty.")
            continue
        consulter_item(name)

    elif option == 4:
        print("Update Price".center(60, "-"))
        name = input("Enter the product name (or press Enter to cancel): ").strip()
        if not name or name.isspace():
            print("Operation canceled.")
            continue
        name = normalize_name(name)
        if name not in inventory:
            print("Product not found in the inventory.")
            continue
        new_price = request_numeric_data("Enter the new price: ", allow_negative=False, min_value=0.01)
        update_price(name, new_price)

    elif option == 5:
        print("Remove Product".center(60, "-"))
        name = input("Enter the product name: ").strip()
        if not name or name.isspace():
            print("The name cannot be empty.")
            continue
        remove_item(name)

    elif option == 6:
        print("Calculate Total Value".center(60, "-"))
        calculate_total_value()

    elif option == 0:
        print("Exiting the program...")
        break
