pacientes = []
def menu():
    print("------------------------")
    print("VETERINARIA")
    print("------------------------")
    print("1. Agregar paciente")
    print("2. Mostrar pacientes")
    print("3. buscar estado de paciente")
    print("4. buscar un paciente especifico")
    print("5. eliminar un paciente")
    print("6. modificar un paciente")
    print("7. Salir")
    print("------------------------")
    opcion = input("Ingrese una opcion: ")
    return opcion.strip() # eliminar espacios en blanco #

def agregar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").lower().strip()
    edad = input("Ingrese la edad del paciente: ").strip()
    estado = input("Ingrese el estado del paciente (enfermo,sano): ").lower().strip()
    raza = input("Ingrese la raza del paciente: ").strip()
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "estado": estado,
        "raza": raza
    }
    pacientes.append(paciente)
    print("Paciente agregado")

def mostrar_pacientes():
    print("------------------------")
    print("Pacientes en la clinica")
    print("------------------------")
    if not pacientes:
        print("No hay pacientes")
    else:
        for paciente in pacientes:
            print(f"Nombre: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}")
            print(f"Estado: {paciente['estado']}")
            print(f"Raza: {paciente['raza']}")
            print("------------------------")

def buscar_estado():
    nombre = input("Ingrese el nombre del paciente: ").strip().lower() # convertir a minusculas para que no se distinga entre mayusculas y minusculas #
    encontrado = False
    print("------------------------")
    print("Pacientes")
    print("------------------------")
    for paciente in pacientes:
        if paciente['nombre'].lower() == nombre:
            print(f"el paciente {paciente['nombre']} esta {paciente['estado']}")
            encontrado = True
            break
    if not encontrado:
        print("Paciente no encontrado")
    print("------------------------")
            
def buscar_paciente():
    nombre_buscado = input("Ingrese el nombre del paciente: ").strip().lower()
    encontrado = False

    print("------------------------")
    print("Pacientes")
    print("------------------------")

    for paciente in pacientes:
        if paciente['nombre'].lower() == nombre_buscado:
            print(f"Nombre: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}")
            print(f"Estado: {paciente['estado']}")
            print(f"Raza: {paciente['raza']}")
            print("------------------------")
            encontrado = True
            break

    if not encontrado:
        print("Paciente no encontrado")
    print("------------------------")

def eliminar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip().lower()
    eliminado = False
    print("------------------------")
    print("Pacientes")
    print("------------------------")
    for i, paciente in enumerate(pacientes):
        if paciente['nombre'].lower() == nombre:
            confirmar = input("¿Esta seguro de eliminar al paciente? (si/no): ").strip().lower()
            if confirmar == "si":                
                pacientes.pop(i)
                print("Paciente eliminado")
            else:
                print("eliminacion cancelada")
            eliminado = True
            break

    if not eliminado:
        print("Paciente no encontrado")
    print("------------------------")

def modificar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip().lower()
    encontrado = False

    print("------------------------")
    print("Pacientes")
    print("------------------------")

    for paciente in pacientes:
        if paciente["nombre"].lower() == nombre:
            print(f"informacion actual del paciente: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}, Estado: {paciente['estado']}, Raza: {paciente['raza']}")

            Nnombre_paciente = input("Ingrese el nuevo nombre del paciente: ").strip().lower()
            Nedad_paciente = input("Ingrese la nueva edad del paciente: ").strip()
            Nestado_paciente = input("Ingrese el nuevo estado del paciente: ").strip().lower()
            Nraza_paciente = input("Ingrese la nueva raza del paciente: ").strip()

            if Nnombre_paciente:
                paciente['nombre'] = Nnombre_paciente
            if Nedad_paciente:
                paciente['edad'] = Nedad_paciente
            if Nestado_paciente:
                paciente['estado'] = Nestado_paciente
            if Nraza_paciente:
                paciente['raza'] = Nraza_paciente

            print("Paciente modificado")
            encontrado = True
            break

    if not encontrado:
        print("Paciente no encontrado")
print("------------------------")
while True:
    opcion = menu()
    match opcion:
        case "1":
            agregar_paciente()
        case "2":
            mostrar_pacientes()
        case "3":
            buscar_estado()
        case "4":
            buscar_paciente()
        case "5":
            eliminar_paciente()
        case "6":
            modificar_paciente()
        case "7":
            print("Saliendo...")
            exit()
        case _:
            print("Opcion invalida")
