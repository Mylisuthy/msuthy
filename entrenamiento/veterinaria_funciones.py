pacientes = []
def encontrar_paciente(nombre):
    nombre = nombre.strip().lower()
    for i, paciente in enumerate(pacientes):
        if paciente['nombre'].lower() == nombre:
            return i
    return None
def mostrar_info_paciente(paciente):
    print(f"Nombre: {paciente['nombre']}")
    print(f"Edad: {paciente['edad']}")
    print(f"Estado: {paciente['estado']}")
    print(f"Especie: {paciente['especie']}")
    print("-" * 30)

def menu():
    print(f"""
    {"-"*30}
    VETERINARIA
    {"-"*30}
    Menu:
    1. Agregar paciente
    2. Mostrar pacientes
    3. buscar estado de paciente
    4. buscar un paciente especifico
    5. eliminar un paciente
    6. modificar un paciente
    7. Salir
    {"-"*30}
    """)
    while True:
        opcion = input("Ingrese una opcion: ")
        if opcion in ["1", "2", "3", "4", "5", "6", "7"]:            
            return opcion
        else:
            print("Opcion invalida por favor ingresa un numero del menu (1 al 7)")

def agregar_paciente():
    print(f"""
    {"-"*30}
    Agregar paciente
    {"-"*30}
    """)

    # Validar nombre (no vacío)
    while True:
        nombre = input("Ingrese el nombre del paciente: ").strip().lower()
        if nombre:
            break
        else:
            print("El nombre no puede estar vacío.")

    # Validar edad (número entero positivo)
    while True:
        edad = input("Ingrese la edad del paciente: ").strip()
        if edad.isdigit():
            break
        else:
            print("La edad debe ser un número. Intenta de nuevo.")

    # Validar estado (si/no -> enfermo/sano)
    while True:
        respuesta = input("¿La mascota está enferma? (si/no): ").strip().lower()
        if respuesta == "si":
            estado = "enfermo"
            break
        elif respuesta == "no":
            estado = "sano"
            break
        else:
            print("Respuesta inválida. Escribe 'si' o 'no'.")

    # Validar especie (no vacía)
    while True:
        especie = input("Ingrese la especie del paciente: ").strip()
        if especie:
            break
        else:
            print("La especie no puede estar vacía.")

    # Guardar paciente
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "estado": estado,
        "especie": especie
    }
    pacientes.append(paciente)
    print("Paciente agregado exitosamente.")

def mostrar_pacientes():
    print(f"""
    {"-"*30}
    Pacientes en la clinica
    {"-"*30}
    """)
    
    if not pacientes:
        print("No hay pacientes")
    else:
        for paciente in pacientes:
            print(f"Nombre: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}")
            print(f"Estado: {paciente['estado']}")
            print(f"Especie: {paciente['especie']}")
            print("------------------------")

def buscar_estado():
    if not pacientes:
        print(f"""
        {"-"*30}
        No hay pacientes
        {"-"*30}
        """)
        return
    nombre = input("Ingrese el nombre del paciente: ").strip().lower() # convertir a minusculas para que no se distinga entre mayusculas y minusculas #
    encontrado = False
    print(f"""
    {"-"*30}
    Pacientes
    {"-"*30}
    """)
    if not nombre:
        print("debes ingresar un nombre para buscar")
        return
    for paciente in pacientes:
        if paciente['nombre'].lower() == nombre:
            estado = paciente['estado'] # guardar el estado del paciente en una variable para imprimirlo despue
            if estado == "enfermo":
                print(f"""
                {"-"*30}
                el paciente {paciente['nombre']} esta {paciente['estado']}
                el paciente necesita atencion
                {"-"*30}
                """)
            elif estado == "sano":
                print(f"""
                {"-"*30}
                el paciente {paciente['nombre']} esta {paciente['estado']}
                el paciente esta a la espera del alta
                {"-"*30}
                """)    
            encontrado = True
            break
    if not encontrado:
        print("Paciente no encontrado")
    print("-"*30)
            
def buscar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip().lower()
    busqueda = encontrar_paciente(nombre)
    print(f"""
    {"-"*30}
    Buscar paciente
    {"-"*30}
    """)
    if busqueda is not None:
        mostrar_info_paciente(pacientes[busqueda])
    else:
        print("Paciente no encontrado.")

def eliminar_paciente():
    nombre = input("Ingrese el nombre del paciente: ").strip().lower()
    busqueda = encontrar_paciente(nombre)
    print(f"""
    {"-"*30}
    Eliminar paciente
    {"-"*30}
    """)
    if busqueda is not None:
        confirmar = input("¿Está seguro de eliminar al paciente? (si/no): ").strip().lower()
        if confirmar == "si":
            pacientes.pop(busqueda)
            print("Paciente eliminado")
        else:
            print("Eliminación cancelada")
    else:
        print("Paciente no encontrado")
    print("-"*30)

def modificar_paciente():
    nombre = input("Ingrese el nombre del paciente que desea modificar: ").strip().lower()
    indice = encontrar_paciente(nombre)

    print(f"""
    {"-"*30}
    Modificar paciente
    {"-"*30}
    """)

    if indice is not None:
        paciente = pacientes[indice]
        print(f"Información actual del paciente: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}, Estado: {paciente['estado']}, Especie: {paciente['especie']}")

        # Copia de los datos para confirmar antes de guardar
        nuevo_paciente = paciente.copy()

        # Nombre
        nuevo_nombre = input("Ingrese el nuevo nombre (dejar vacío para mantener): ").strip().lower()
        if nuevo_nombre:
            nuevo_paciente['nombre'] = nuevo_nombre

        # Edad
        while True:
            nueva_edad = input("Ingrese la nueva edad (dejar vacío para mantener): ").strip()
            if not nueva_edad:
                break
            elif nueva_edad.isdigit():
                nuevo_paciente['edad'] = nueva_edad
                break
            else:
                print("La edad debe ser un número. Intenta de nuevo.")

        # Estado
        while True:
            respuesta = input("¿La mascota está enferma? (si/no, dejar vacío para mantener): ").strip().lower()
            if not respuesta:
                break
            elif respuesta == "si":
                nuevo_paciente['estado'] = "enfermo"
                break
            elif respuesta == "no":
                nuevo_paciente['estado'] = "sano"
                break
            else:
                print("Respuesta inválida. Escribe 'si', 'no' o deja vacío.")

        # Especie
        nueva_especie = input("Ingrese la nueva especie (dejar vacío para mantener): ").strip()
        if nueva_especie:
            nuevo_paciente['especie'] = nueva_especie

        # Mostrar resumen y confirmar
        print(f"""
        {"-"*30}
        Nueva información del paciente:
        Nombre: {nuevo_paciente['nombre']}
        Edad: {nuevo_paciente['edad']}
        Estado: {nuevo_paciente['estado']}
        Especie: {nuevo_paciente['especie']}
        {"-"*30}
        """)

        confirmar = input("¿Deseas guardar estos cambios? (si/no): ").strip().lower()
        if confirmar == "si":
            pacientes[indice] = nuevo_paciente
            print("Paciente modificado exitosamente.")
        else:
            print("Modificación cancelada.")
    else:
        print("Paciente no encontrado.")

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
            print("Saliendo del sistema... ¡Hasta luego!")
            break
