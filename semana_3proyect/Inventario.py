# inventory: global dictionary
# key = product name, value = tuple (price, quantity, type)
# type can be "kg" or "u" (kilograms or units)
inventory = {}

def request_numeric_data(message, is_integer=False, allow_negative=True, min_value=None):
    """ Requests a valid numeric input from the user. Can be either float or int. """
    while True:
        entry = input(message)
        try:
            value = int(entry) if is_integer else float(entry)
            # Check for negative values if not allowed
            if not allow_negative and value < 0:
                print("Negative values are not allowed. Please enter a valid number.")
                continue
            # Check if the value is above the minimum threshold
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}. Please enter a valid number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def add_item(name, price, quantity, unit_type):
    """ Adds an item to the inventory, if it doesn't exist yet. """
    if name in inventory:
        print("The item already exists in the inventory.")
    else:
        inventory[name] = (price, quantity, unit_type)
        print(f"Item '{name}' added successfully.")

def show_all_items():
    """ Displays all items in the inventory with their details. """
    if not inventory:
        print("The inventory is empty.")
    else:
        print("Inventory:")
        for name, (price, quantity, unit_type) in inventory.items():
            unit = "kg" if unit_type == "kg" else "units"
            print(f" {name} | Price: ${price:.2f} | Quantity: {quantity} {unit}")

def consulter_item(name):
    """ Consults a specific item by its name. """
    product = inventory.get(name)
    if product:
        price, quantity, unit_type = product
        print(f"""
{'-'*60}
        Product: {name} | Price: ${price:.2f} | Quantity: {quantity} {'kg' if unit_type == 'kg' else 'units'}
{'-'*60}
        """)
    else:
        print(f"Item '{name}' not found in inventory.")

def update_price(name, new_price):
    """ Updates the price of an existing product. """
    if name in inventory:
        _, quantity, unit_type = inventory[name]
        inventory[name] = (new_price, quantity, unit_type)
        print(f"Price updated for '{name}'. New price: ${new_price:.2f}")
    else:
        print("Product not found in inventory.")

def remove_item(name):
    """ Removes an item with user confirmation. """
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
    """ Calculates the total value of the inventory. """
    total = sum(price * quantity for price, quantity, _ in inventory.values())
    print(f"Total value of inventory: ${total:.2f}")

def menu():
    """ Prints the menu of options. """
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

# Handle adding items to the inventory
def handle_add_item():
    print("Add item".center(60, "-"))
    name = input("Enter item name (or press Enter to cancel): ").strip().lower()
    if not name:
        print("Operation canceled.")
        return

    # Request for valid price input (no negative values, minimum price = 0.01)
    price = request_numeric_data("Enter item price: ", allow_negative=False, min_value=0.01)

    # Request for valid unit and quantity (kg or units)
    while True:
        unit_type = input("Quantity in kilograms (K) or units (U)? [K/U]: ").strip().lower()
        if unit_type == "k":
            quantity = request_numeric_data("Enter quantity in kilograms: ", allow_negative=False, min_value=0.01)
            unit = "kg"
            break
        elif unit_type == "u":
            quantity = request_numeric_data("Enter quantity in units: ", is_integer=True, allow_negative=False, min_value=1)
            unit = "u"
            break
        else:
            print("Invalid unit type. Please enter 'K' for kilograms or 'U' for units.")

    # Add the item to the inventory
    add_item(name, price, quantity, unit)

# Handle showing all items in the inventory
def handle_show_items():
    print("Show all items".center(60, "-"))
    show_all_items()

# Handle consulting an item in the inventory
def handle_consult_item():
    print("Consult item".center(60, "-"))
    name = input("Enter the name of the item: ").strip().lower()
    if not name:
        print("Name cannot be empty.")
        return
    consulter_item(name)

# Handle updating the price of an item
def handle_update_price():
    print("Update price".center(60, "-"))
    name = input("Enter the name of the item to update (or press Enter to cancel): ").strip().lower()
    if not name:
        print("Operation canceled.")
        return
    if name not in inventory:
        print("Item not found in inventory.")
        return
    new_price = request_numeric_data("Enter the new price: ", allow_negative=False, min_value=0.01)
    update_price(name, new_price)

# Handle removing an item from the inventory
def handle_remove_item():
    print("Remove item".center(60, "-"))
    name = input("Enter the name of the item: ").strip().lower()
    if not name:
        print("Name cannot be empty.")
        return
    remove_item(name)

# Handle calculating the total value of the inventory
def handle_total_value():
    print("Calculate total value".center(60, "-"))
    calculate_total_value()

# Main function that handles the entire menu logic
def main():
    while True:
        menu()
        try:
            option = int(input("Enter an option (0-6): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 6.")
            continue

        # Execute the corresponding function based on user choice
        if option == 1:
            handle_add_item()
        elif option == 2:
            handle_show_items()
        elif option == 3:
            handle_consult_item()
        elif option == 4:
            handle_update_price()
        elif option == 5:
            handle_remove_item()
        elif option == 6:
            handle_total_value()
        elif option == 0:
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please enter a number from 0 to 6.")

# Entry point of the program
if __name__ == "__main__":
    main()
