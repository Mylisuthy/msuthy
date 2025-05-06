hora = int(input("dime la hora en la que te encuentras (formato 24horas): "))
dia_de_semana = str(input("dime el dia de la semana en el que te encuentras (lunes a domingo): ")).lower()
if dia_de_semana in ["lunes", "martes", "miercoles", "jueves", "viernes"]:
    if 2 <= hora < 4:
        print("descansar por dios")
    elif 4 <= hora < 6:
        print("buenos dias, deberias de hacer ejercicio")
    elif 6 <= hora < 8:
        print("preparate para trabajar")
    elif 8 <= hora < 18:
        print("debes de trabajar aprovecha el dia al maximo")
    elif 18 <= hora < 20:
        print("deberias hacer ejersicio o descansar")
    elif 20 <= hora < 23:
        print("deberias dormir mañana necesitas energia para trabajar")
    else:
        print("buenas noches, deberias de descansar")    
elif dia_de_semana in ["sabado", "dormingo"]:
    if 8 <= hora < 12:
        print("algo de ejercicio es recomendado, luego dascansar la mente seria esencial para el dia")
    else:
        print("descansar la mente es algo esencial no lo crees?")
else:
    print("no es un dia de la semana valido")
#Versión en función con match-case:
def asistente_productividad():
    hora = int(input("Dime la hora en la que te encuentras (formato 24 horas): "))
    dia_de_semana = input("Dime el día de la semana en el que te encuentras (lunes a domingo): ").lower()

    match dia_de_semana:
        case "lunes" | "martes" | "miercoles" | "jueves" | "viernes":
            if 2 <= hora < 4:
                print("Descansa, por Dios.")
            elif 4 <= hora < 6:
                print("¡Buenos días! Deberías hacer ejercicio.")
            elif 6 <= hora < 8:
                print("Prepárate para trabajar.")
            elif 8 <= hora < 18:
                print("Debes trabajar, aprovecha el día al máximo.")
            elif 18 <= hora < 20:
                print("Podrías hacer ejercicio o descansar.")
            elif 20 <= hora < 23:
                print("Deberías dormir, mañana necesitas energía para trabajar.")
            else:
                print("Buenas noches, deberías descansar.")

        case "sabado" | "domingo":
            if 8 <= hora < 12:
                print("Algo de ejercicio es recomendable. Luego, descansar la mente es esencial.")
            else:
                print("Descansar la mente es algo esencial, ¿no lo crees?")

        case _:
            print("Día de la semana no reconocido.")

# Llamada a la función
asistente_productividad()
