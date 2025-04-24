# 1) invertir valores
a = float(input("Dame un numero "))
b = float(input("Dame el otro uwu "))
print(f"Sus numeros son {a}, y {b}")
a,b = b, a
print (f"Sus numeros invertidos son {a}, {b}")

# 2) invertir num 3 cifras
#se piden los datos al usuario
numeros = int(input("dame un numero de 3 cifras"))
#transforma la variable numeros en caracteres, la enlista y lee la lista hacia atras 
inver = int(str(numeros)[::-1])
#escribe el numero ya transformado y llama variable
print(f"el numero es" + str(inver))
#hace las operaciones y transforma las variables
centena = int(inver) //100
Decena = (int(inver) % 100) // 10
Unidades = int(inver) % 10
#lee, escribe y organiza los datos
print(f"estas son tus centenas:{centena}\nestas tus decenas: {Decena}\nestas tus unidades: {Unidades}")

# 3) calculo de timpo en segundos
#se pide el dato a usar
numero = int(input("dime un numero para el calculo"))
#variables y calculo de operaciones
hora = int(numero) // 3600
minutos = int(numero) %3600 // 60
segundos = int(numero) % 60
#escribe/inprime el resultado de las variables con un mensage pre definido
print (f"tienes {hora} hora's, {minutos} minutos y {segundos} segundos")

# 4) pedir fecha al usuario declarando variable
#peticion de datos
dd = int(input("dame el numero del mes en el que nacimiento " ))
mm = int(input("dame el dia en que naciste " ))
aaaa = int(input("dame el año en que naciste " ))
#transformar variable (.zfill = rellena el espacio basio con 0)
dd = str(dd).zfill(2)
mm = str(mm).zfill(2)
#escribir texto, mostrar datos
print(f" Naciste el {dd}/{mm}/{aaaa} \n La fecha al contrario {aaaa}-{mm}-{dd}")

# 5) converción de temperatura 
# Solicitar la temperatura en Fahrenheit
Temperatura = input("Dame tu temperatura en Fahrenheit: ")

# Verificar si la entrada es un número
if Temperatura.replace('.', '', 1).isdigit() or (Temperatura[0] == '-' and Temperatura[1:].replace('.', '', 1).isdigit()):
    Temperatura = float(Temperatura)  # Convertir a float si es un número válido
    temperatura_c = (Temperatura - 32) / 1.8
    print(f"Su temperatura en Fahrenheit: {Temperatura} \nSu temperatura en Celsius: {temperatura_c}")
else:
    print("La temperatura se mide con números, ¿no?")
    
 #6) Solicitar el costo de la comida al usuario
preciocomida = int(input("¿Cuánto costó la comida? "))

# Calcular las propinas
p10porciento = preciocomida * 0.10
p15porciento = preciocomida * 0.15
p20porciento = preciocomida * 0.20

# Calcular los totales a pagar
t10pagar = p10porciento + preciocomida
t15pagar = p15porciento + preciocomida
t20pagar = p20porciento + preciocomida
# Mostrar los resultados
print (f"precio {preciocomida}$-propina {p10porciento}$\ntotal a pagar {t10pagar}$".upper())
print (f"precio {preciocomida}$-propina {p15porciento}$\ntotal a pagar {t15pagar}$".upper())
print (f"precio {preciocomida}$-propina {p20porciento}$\ntotal a pagar {t20pagar}$".upper())

# 7) Extraer digitos de un numero de 4 cifras

#peticion de digitos al usuario
Digito = int(input("dame un digito de 4 sifras: "))
#se cambia el formato a texto para facilitar su lectura
cadena = str(Digito)
#se añaden las "," (queria que la "," se implementara cada 2 digitos)
resultado = ','.join([cadena[i:i+2] for i in range(0, len(cadena), 2)])
#se imprime el mensaje
print(f"estos son tus numeros separados por coma: {resultado}")

# 8) formato de precio con 2 decimales

#se define la variable que se usara
primerP = float("dame tu primer digito: ")
segundoP = float("dame el segundo numero: ")
#suma de variables
resultado = primerP + segundoP
#mostrar el resultado
print (f"este es tu precio ${resultado} :3")

# 9) 
