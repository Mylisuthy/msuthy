# hola este es mi comienzo en python

#creacion de calculadora con presentacion

#bienvenida
print("hola usuario")
print("danos algo de informacion para comenzar")
#primeras preguntas
nombre = input("¿Cómo te llamas? ")
edad = input("que edad tienes? ")

#primeras interacciones
print("hola :) " + str(nombre))
print("juguemos algo ")

#peticion de datos para comienzo de presentacion
num1 = int(input ("quiero que primero me des un numero ;)" ))
num2 = int(input ("ahora dame un numero entero :o" ))

#introduccion a la suma
print("te pedire mas numeros, no te desanimes")
print("pero mientras tanto\nesta es la suma\nde tus primeros\nnumeros <;)")
res1suma = int(num1+num2)
print(str(res1suma))

#introduccion a la multiplicacion con decimales
print("hey! ahora probemos otra cosa")
multnum1 = float(input ("dame otro numero por favor\npero que esta ves sea decimal"))
multnum2 = float(input ("dame otro...\nsin pensar!"))
print("mira esto\n esta el la multiplicacion de tus numeros")
res1mult = float(multnum1*multnum2)
print(str(res1mult))
#el doble y el triple
