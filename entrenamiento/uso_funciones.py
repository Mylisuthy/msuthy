# que es una funcon? #
# una funcion es una linea de codigo avierta pre definida que se puede utilizar luego de su creacion #

# como se usa despues de su creacion? #
# para usar la funcion luego de su creacion es necesario implementar un llamado a la funcion #
# ejemp #

def saludar(): # esta linea actua como la funcion a usar #
    print("hola, como estas") # este es el proceso que se llebara acabo dentro de la funcion #
saludar() # este es el llamado a la funcion en especifico #
print("------------------------")
# que son los parametros y los argumentos #
# parametros: son variebles que defines entre los parentecis de la funcion, actuando como entradas que la funcion puede utilizar. #
# ejemp #

def saludar(nombre): # en este caso el "nombre" es el parametro #
    print(f"hola, {nombre}")

# argumento: son los valores reales que le das a la funcion cuando la llamas. #
# ejemp #

saludar("jhoana") # en este caso el valor que se le da es "jhoana" y es el valor que la funcion utilizara #
print("------------------------")
# asi se ve una funcion con multiples parametros. #
# ejemp #

def sumar(a, b): # la funcion con los parametros definidos #
    resultado = a + b # la operacion que la funcion llebara a cabo #
    return resultado # se usa return para que la funcion arroje los resultados deseados de la operacion #
print(sumar(3, 5)) # se imprime la suma llamando a la funcion con los valores pre definidos #
# el resultado debe ser 8 #
print("------------------------")

# que timpos de argumentos existen? #
# 1) argumentos posicionales (el orden importa) #
# ejemp #
def resta(a, b): # la funcion
    return a - b # la operacion que debe dar la funcion #
print(resta(10, 6)) # 
# el resultado debe ser 4 #
print("------------------------")


# 2) argumento con nombre (keyword arguments) #
print(resta(b = 6, a = 12))
# el resultado debe ser 6 #
print("------------------------")

# 3) parametros con valor por defecto #
def saludar2(nombre = "invitado"):
    print(f"hola, {nombre}")
saludar2() # da el resultado con el valor pre definido #
print("------------------------")
saludar2("maria") # da el resultado con un valor añadido #
print("------------------------")

# return vs print #
# print() # muestra un resultado en pantalla. #
# return # devuelve un valor para usarse despues. #
# ejemp #
def doble(x):
    return x * 2
resultado = doble(4)
print(resultado)
print("------------------------")
# debe de dar 8 como resultado #
# con print #
# def doble2(x):
#    print x * 2
# resultado = doble2(4)
# print(resultado) # da error porque no se definio la operacion y solo se pidio inprimir # 

# variebles globales #
# se definen fuera de cualquier funcion #
n = 10 # variable global #
# esta se encontrara visible en todo el programa #
def mostrar():
    print(n) # axede a la variable global #
mostrar() # el llamado a la funcion que mostrara la variable global #
print("------------------------")

# variables locales #
# se definen dentro de la funcion. solo existen y dan valor dentro de la funcion #
def saludo3():
    mensaje = "hola" # esta es la variable local #
    print(mensaje)
    print("------------------------")
saludo3() # el llamado a la funcion (hola) #
# el print(mensaje) no debe estar fuera ya que no lo reconoceria y dara error, por lo que la variable solo se usa dentro de la funcion #

# que sucede si deseo usar una variable local dentro de una funcion y luego modificarla #
# se debe usar la palabra clave Global para poder proceder a modificarla #
# ejemp #
contador = 0
def aumentar():
    global contador # llamado a la variable global #
    contador += 1 # interaccion con la variable global
aumentar() # llamado a la funcion #
print(contador) # mostrar la variable modificada #
print("------------------------")

# si solo quieres usar el valor se pasa como argumento #
# ejemp #
contador2 = 10 
def aumentar(numero):
    numero += 10
    return numero
aumentar(contador2)
print(contador2)
