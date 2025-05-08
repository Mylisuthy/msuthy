estudiantes = {
    "juan": {
        "edad": 15,
        "calificación": 8.5
    },
    "maria": {
        "edad": 16,
        "calificación": 9.0
    },
    "carlos": {
        "edad": 14,
        "calificación": 7.5
        }
}

def agregar_estudiante():
    while True:
        nombre_estudiante = input("Ingresa el nombre del estudiante: ").strip().lower()
        if nombre_estudiante == "":
            print("El nombre no puede estar vacío.")
            continue
        break
    while True:
        try:
            edad_estudiante = int(input("Ingresa la edad del estudiante: "))
            if edad_estudiante < 5 or edad_estudiante > 20:
                print("La edad debe estar entre 5 y 20 años.")
                continue
            break
        except ValueError:
            print("La edad debe ser un número entero.")
    while True:
        try:
            calificacion = float(input("Ingresa la calificación del estudiante: "))
            if calificacion < 0 or calificacion > 10:
                print("La calificación debe estar entre 0 y 10.")
                continue
            break
        except ValueError:
            print("La calificación debe ser un número decimal.")
    estudiantes[nombre_estudiante] = {
        "edad": edad_estudiante,
        "calificación": calificacion
        }
    print(f"Usted ha agregado correctamente a {nombre_estudiante}")

def modificar_estudiante():
    nombre_modifcar = input("dime el nombre del estudiante que deseas modificar (0 para volver al menú): ").strip().lower()
    if nombre_modifcar == "0":
        return
        
    if nombre_modifcar in estudiantes:
        while True:
            modifica_algo = input("¿Qué deseas modificar?\n1: edad.\n2: calificación.\n0: volver al menú: ")
            if modifica_algo in ("0", "1", "2"):
                break
            print("Por favor introduce 1 para edad, 2 para calificación o 0 para volver al menú: ")

        if modifica_algo == "0":
            return

        while True:
            try:
                if modifica_algo == "1":
                    nueva_edad = int(input("Ingresa la nueva edad (0 para volver al menú): "))
                    if nueva_edad == 0:
                        return
                    if nueva_edad < 5 or nueva_edad > 20:
                        print("La edad debe estar entre 5 y 20 años.")
                        continue
                    estudiantes[nombre_modifcar]['edad'] = nueva_edad
                    print(f"La edad de {nombre_modifcar} ha sido modificada a {nueva_edad}")
                    break
                        
                else: # modifica_algo == "2"
                    nueva_calificacion = float(input("Ingresa la nueva calificación (0 para volver al menú): "))
                    if nueva_calificacion == 0:
                        return
                    if nueva_calificacion < 0 or nueva_calificacion > 10:
                        print("La calificación debe estar entre 0 y 10.")
                        continue  
                    estudiantes[nombre_modifcar]['calificación'] = nueva_calificacion
                    print(f"La calificación de {nombre_modifcar} ha sido modificada a {nueva_calificacion}")
                    break
            except ValueError:
                print("Por favor, ingresa un número válido")
    else:
        print(f"No se encontró el estudiante {nombre_modifcar}")           
                
def mostrar_informacion():
    for estudiante, inf in estudiantes.items():
        print("-"*30)
        print(f"nombre: {estudiante}, edad: {inf['edad']}, calificaciones: {inf['calificación']}")
        
def eliminar_estudiante():
    nombre_eliminar = input("Ingresa el nombre del estudiante a eliminar (0 para volver al menú): ").strip().lower()
    if nombre_eliminar == "0":
        return
        
    if nombre_eliminar in estudiantes:
        while True:
            confirmar = input(f"¿Estás seguro de eliminar a {nombre_eliminar}? (si/no): ").strip().lower()
            if confirmar in ["si", "no"]:
                break
            print("Por favor, responde 'si' o 'no'")
            
        if confirmar == "si":
            del estudiantes[nombre_eliminar]
            print(f"El estudiante {nombre_eliminar} ha sido eliminado correctamente")
        else:
            print("Operación cancelada")
    else:
        print(f"No se encontró el estudiante {nombre_eliminar}")

while True:
    print("""
         
        1) Agregar un nuevo estudiante
        2) Modificar la calificacion
        3) Mostrar información de todos los estudiantes
        4) Eliminar un estudiante por su nombre

    """)
    try:
        opcion = int(input("Elige una opción: "))
        match opcion:
            case 1:
                agregar_estudiante()
            case 2:
                modificar_estudiante()
            case 3:
                mostrar_informacion()
            case 4:
                eliminar_estudiante()
    except ValueError:
        print("Digita un numero correcto")
