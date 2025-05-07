estudiantes = {}


def agregar_estudiante():
    nombre_estudiante = str(input("Ingresa el nombre del estudiante: "))
    edad_estudiante = int(input("Ingresa la edad del estudiante: "))
    calificacion = float(input("Ingresa la calificación del estudiante: "))
    estudiantes[nombre_estudiante] = {"edad":edad_estudiante,"calificación":calificacion}
    print(f"Usted ha agregado correctamente a {nombre_estudiante}")

def modificar_estudiante():
    nombre_modifcar = str(input("Ingresa el nombre del estudiante a modificar: "))
    if nombre_modifcar in estudiantes:
        modifica_algo = str(input("¿Qué deseas modificar edad o calificacion: "))
        while True:
            try:
                if modifica_algo == "edad":
                    nueva_edad = int(input("dime la nueva edad: "))
                    estudiantes[nombre_modifcar][modifica_algo] = nueva_edad
                    break
                        
                elif modifica_algo == "calificación":
                    nueva_calificacion = int(input("Ingrese la nueva calificación: "))  
                    estudiantes[nombre_modifcar][modifica_algo] = nueva_calificacion
                    break
            except ValueError:
                print("no se reconoce lo que quieres hacer")
                
def mostrar_informacion():
    for estudiante, inf in estudiantes.items():
        print("-"*30)
        print(f"nombre: {estudiante}, edad: {inf["edad"]}, calificaciones: {inf["calificación"]}")
        
    

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
    except ValueError:
        print("Digita un numero correcto")
