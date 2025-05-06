print("calculemos tu presupuesto de ingresos menduales")
while True:
    try:
        ingresos_mensuales = float(input("ingresa tus ingresos mensuales: "))
        if ingresos_mensuales < 0:
            print("ingresa un valor positivo")
        else:
            break
    except ValueError:
        print("ingresa un valor numerico valido")
while True:
    try:
        gastos_mensuales = float(input("ingresa tus gastos mensuales: "))
        if gastos_mensuales < 0:
            print("ingresa un valor positivo")
        else:
            break
    except ValueError:
        print("ingresa un valor numerico valido")
print("\n---resultado---")        
ahorro = ingresos_mensuales - gastos_mensuales
if ahorro > 0:
    print(f"felicidades, este mes tienes un presupuesto de ${ahorro:.2f} para ahorrar")
elif ahorro == 0:
     print("tienes un presupuesto justo, este mes no puedes ahorrar")
else:
    print(f"gastas mas de lo que ganas, este mes no puedes ahorrar. deberias de reducir {abs(ahorro):.2f} en tus gastos")