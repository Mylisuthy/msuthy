contact_list = []

def menu():
    print(f"""
{"-"*30}
    welcome to your list of contacts 
{"-"*30}
    what do you want to do today?
    1. add new contact.
    2. search contact.
    3. change a contact.
    4. delete a contact.
    5. show all contacts.
    0. exit...
""")
    while True:
        option = input("select option: ")
        if option in ["1", "2", "3", "4", "5", "0"]:            
            return option
        else:
            print("invalid option, enter a new one in range (0 al 5)")

def add_contact():
    while True:
        try:
            contact = input("type the name of the contact or output to return to the menu").strip().lower()
            if contact == "":
                print("the contact name must not be empty")
                continue
            elif contact == "exit":
                return
            else:
                print("name entered correctly")
            
            while True:
                marital_status = input("type the marital status of the contact to be added\n(single, married, separated, divorced or widowed.): ").strip().lower()
                if marital_status == "":
                    print("the contact merital status must not be empty")
                    continue
                elif marital_status == "single" or "married" or "separated" or "divorced" or "widowed":
                    break
                else:
                    print("Invalid option")

            while True:
                gender = input("enter the gender of your contact (female, male, apache elicopter): ").strip().lower()
                if gender == "":
                    print("the gender is empty")
                    continue
                elif gender == "female" or "male" or "apache elicopter":
                    break      
                else:
                    print("gender must be within the options (male, female, apache elicopter)")
            while True:
                number_extension = input("type the extension of the number (ej: +57): ")
                if number_extension == "":
                    print("the number extension cannot be empty")
                    continue
                elif number_extension.startswith("+") and number_extension[1:].isdigit():
                    break
                else:
                    print("Invalid extension. Must start with '+' and continue with numbers.")
            while True:
                number = int(input("enter your contact number (ej: 3004527640): "))
                if number == "":
                    print("the number of your contact cannot be empty")
                    continue
                else:
                    break
        except ValueError:
            print("you do not recognize what you want to do")
        pk = {
            'contact': contact,
            'marital_status': marital_status,
            'gender': gender,
            'number_extension': number_extension,
            'number': number
        }
        contact_list.append(pk)
        
while True:
    option = menu()
    match option:
        case "1": add_contact()
        case 2: search_contact()
        case 3: change_a_contact()
        case 4: delete_a_contact()
        case 0: 
            print("you left the menu")
