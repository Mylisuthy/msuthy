temperatura = float(input("¿Cuál es la temperatura actual en grados Celsius? "))
llueve = input("¿Está lloviendo? (sí o no): ").strip().lower()

if temperatura < 10:
    categoria_temp = "frio"
elif 10 <= temperatura < 20:
    categoria_temp = "templado"
elif 20 <= temperatura < 30:
    categoria_temp = "calido"
else:
    categoria_temp = "calor_extremo"

match categoria_temp:
    case "frio":
        print("Usa abrigo grueso")
    case "templado":
        print("lleva una chaqueta ligera")
    case "calido":
        print("Puedes usar ropa ligera")
    case "calor_extremo":
        print("Usa ropa muy ligera y mantente hidratado")

match llueve:
    case "sí":
        print("lleva paraguas o impermeable")
    case "no":
        pass