numero = int(input("dame un numero "))

if numero % 5 == 0 and numero % 3 == 0:
    print ("fizzbuzz")
elif numero % 5 == 0:
    print ("buzz")
elif numero % 3 == 0:
    print ("fizz")
else :
    print (numero)
    
#entrada a unicornio ninja

edad = int(input("cual es tu edad? "))
dorado = bool(input("tienes el pase dorado "))

if edad <= 18:
    print("no puedespasar ")
elif dorado == "no" and edad >= 18 or edad <= 25:
        print("puedes pasar ")    
elif edad <= 18 and dorado == "si":
        print("puedes pasar")
else:
    edad < 25 and dorado == "no"
    print("no puedes pasar ")
