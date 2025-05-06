from exercises_Python_estructuras_condicionales.exercise1_2 import asistente_productividad


limitecupos = 10
asistregistros = 0
while asistregistros < limitecupos:
    print("---registra asistentes---")
    nombre = input ("ingresa el nombre del asistente: ")
    edad = int(input("ingresa la edad del asistente: "))
    if edad < 18:
        print(f"{nombre} es mayor de edad, puede asistir. ")
        asistregistros += 1
    else:
        print(f"{nombre} es menor de edad, no puede asistir. ")
        asistregistros += 0

    
