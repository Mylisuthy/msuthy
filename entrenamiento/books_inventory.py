inventory = [
    {"name": "book 1", "price": 10.0, "quantity": 100},
    {"name": "book 2", "price": 15.0, "quantity": 50},
    {"name": "book 3", "price": 20.0, "quantity": 30},
    {"name": "book 4", "price": 25.0, "quantity": 10},
    {"name": "book 5", "price": 30.0, "quantity": 5}
]
def request_numeric(menssage, its_integer = False):
    """Prompts the user for valid numeric input. This can be a float or an int."""
    while True:
        entry = input(menssage)
        if entr
        return int(entry) if its_integer else float(entry)


def add_book(name, price, quantity):
    """Add a product to your inventory if it doesn't already exist. """
    if name in inventory:
        print("The book already exists in the inventory.")
    else:
        inventoryData = {"name": name, "price": price,"quantity": quantity}
        inventory.append(inventoryData)
        print(f"a book named '{name}' added successfully.")

def show_all_books():
    """Displays all products in the inventory with their data."""
    if not inventory:
        print("the inventory is empty.")
    else:
        print("inventory".center(60, "-"))
        for name, price, quantity in inventory:
            print(f"book name: {name} | price: ${price} | Quantity {quantity}")

def consulter_book(name):
    name = inventory(name)
    if name:
        price, quantity = name
        print(f"book name: {name} | price: ${price:.2f} | Quantity: {quantity}")
    else:
        print(f"book '{name}' not found in inventory.")

def update(name, new):
        if desition in inventory[price]:
            price, desition = inventory[name]
            inventory[name] = {new, price, desition}

        elif desition in inventory[quantity]:
            _, quantity, desition = inventory[quantity]
            inventory[name] = {new, quantity, desition}

def menu():
    """interactive menu :o"""
    print(f"""
{"-"*60}
                welcome to your book inventory
{"-"*60}
            1. Add new book
            2. Show all books
            3. Cunsult book in a inventory
            4. Update book in inventory
            5. Remove specifick book
            6. Calculate my price inventory
            0. Exit
{"-"*60}
""")
def main():
    while True:
        menu()
        
        option = input("enter an option prease (0-6): ")
        
        if option == "1":
            print("add item".center(60,"-"))
            name = input("please enter a book named or press ENTER to cancel: ").strip().lower()
            if not name:
                print("operation canceled.")
                continue
            price = request_numeric("Enter a book price: ")
            while True:
                if not price:
                    print("Price is a required field.")
                    continue
                else:
                    break
            quantity = request_numeric("Enter quantity in units: ")
            while True:
                if not quantity:
                    print("quantity is a required field.")
                    continue
                else:
                    break
            add_book(name, price, quantity)
        elif option == "2":
            print("show all books".center(60,"-"))
            show_all_books()
        elif option == "3":
            print("consult book".center(60, "-"))
            name = input("please enter the name of the book:")
            if not name:
                print("a book name cannot be empty.")
                continue
            consulter_book(name)
        elif option == "4":
            print("Update price or quantity".center(40, "-"))
            name = input("enter book name (or press ENTER to retry): ").strip().lower()
            if not name:
                print("operation canceled")
                continue
            else:
                while True:
                    desition = input("that you want to modify 1) price or 2) quantity? (or press ENTER to retry): ").strip().lower()
                    if not desition:
                        print("operation cancel")
                    elif desition == "1" or "price":
                        new = request_numeric("enter the new price: ", is_integer=True)
                        if not new:
                            print("new price cannot be empty")
                            continue
                        update(name, new)
                    elif desition == "2" or "quantity":
                        new = request_numeric("enter the new quantity: ")
                        if not new:
                            print("new quantity cannot be empty")
                            continue
                        update(name, new)
                    else:
                        print("option not recognized please retype it (1 or 2)")
                        continue

            

if __name__ == "__main__":
    main()
