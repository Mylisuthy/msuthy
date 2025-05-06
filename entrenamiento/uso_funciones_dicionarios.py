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

## diccionarios ##
#que es un diccionario? #
# es una coleccion de datos que se almacenan en pares de clave:valor #
# las claves son unicas e inmutables y se utilizan para acceder a los valores asociados (como strings o numeros) #
# ejemp #
# diccionario vacio #
mi_diccionario = {
    
}
# diccionario con datos #
personah = {
    "nombre": "jhoana",
    "edad": 25,
    "ciudad": "bogota"
}
# acceder a los valores #
print(personah["nombre"]) # jhoana #
print(personah["edad"]) # 25 #
print(personah["ciudad"]) # bogota #
print("------------------------")

# modificar valores #
personah["edad"] = 26
print(personah["edad"]) # 26 #
print("------------------------")

#eliminar un valor #
del personah["ciudad"]
personah.pop("edad") # elimina el edad #
personah.clear() # elimina todo el diccionario #
print(personah) # {} #
print("------------------------")

# recorrer un diccionario #
for clave, valor in personah.items():
    print(f"{clave}: {valor}")
print("------------------------")

# otras funciones utiles #
print(personah.keys()) # muestra las claves #
print(personah.values()) # muestra los valores #
print(personah.items()) # muestra los pares clave:valor #
print("------------------------")

# verificar si una clave existe #
if "nombre" in personah:
    print("existe la clave 'nombre'")
print("------------------------")
# ejemp completo #
usuario = {
    "nombre": "esteban",
    "Gmail": "estebis@example.com",
    "activo": True,
    "contrasena": "123456"
}
for clave, valor in usuario.items():
    print(f"{clave} => {valor}")
print("------------------------")

# listas de diccionarios #
# es una coleccion de diccionarios que se almacenan en una lista #
# ejemp #
usuarios1 = [
    {"nombre": "maria", "edad": 26},
    {"nombre": "carlos", "edad": 22},
    {"nombre": "juan", "edad": 20},
    {"nombre": "ana", "edad": 25},
    {"nombre": "jose", "edad": 28},
    {"nombre": "luis", "edad": 24}
]
# cada elemeneto de la lista es un diccionario independiente #
# como recorrer una lista de diccionarios #
for usuario in usuarios1:
    print(f"{usuario['nombre']} tiene {usuario['edad']} años") # puedes acceder a los valores de cada diccionario utilizando las claves #
print("------------------------")

# como modificar un diccionario dentro de una lista #
# ejemp #
usuarios1[0]["edad"] = 27 # modifica la edad de maria #
usuarios1[1]["nombre"] = "raul" # modifica el nombre de carlos #
print(usuarios1[0]["edad"]) # 27 #
print(usuarios1[1]["nombre"],usuarios1[1]["edad"]) # raul / 22 #
print("------------------------")

# como agregar un nuevo diccionario a una lista #
# ejemp #
usuarios1.append({"nombre": "pedro", "edad": 29}) # agrega un nuevo diccionario a la lista #
nuevo_usuario = {"nombre": "jose", "edad": 30}
usuarios1.append(nuevo_usuario) # agrega un nuevo diccionario a la lista #
for usuario in usuarios1:
    print(f"{usuario['nombre']} tiene {usuario['edad']} años") # puedes acceder a los valores de cada diccionario utilizando las claves #
print("------------------------")

# para agregar en una posicion especifica #
usuarios1.insert(2, {"nombre": "lisa", "edad": 23}) # agrega un nuevo diccionario en la posicion 2 #
for usuario in usuarios1:
    print(f"{usuario['nombre']} tiene {usuario['edad']} años") # puedes acceder a los valores de cada diccionario utilizando las claves #
print("------------------------")

#como eliminar un diccionario de una lista #
del usuarios1[0] # elimina el diccionario en la posicion 0 #
usuarios1.pop(1) # elimina el diccionario en la posicion 1 #
usuarios1.remove({"nombre": "juan", "edad": 20}) # elimina el diccionario con el nombre "juan" #

# buscar un diccionario en una lista #
# ejemp #
for usuario in usuarios1:
    if usuario["nombre"] == "ana":
        print("usuario encontrado", usuario)

# ejemp completo #
# se crea la lista de diccionarios #
productos = [ 
    {"nombre": "camisa", "precio": 90},
    {"nombre": "pantalon", "precio": 180},
    {"nombre": "zapatos", "precio": 340},
    {"nombre": "chaqueta", "precio": 220},
    {"nombre": "remera", "precio": 120},
    {"nombre": "gorra", "precio": 130},
    {"nombre": "bufanda", "precio": 60},
    {"nombre": "calcetines", "precio": 20},
    {"nombre": "medias", "precio": 15},
    {"nombre": "gafas", "precio": 2500},
    {"nombre": "reloj", "precio": 1000},  
]
# mostrar los productos #
for producto in productos:
    print(f"{producto['nombre']}: ${producto['precio']}")
print("------------------------")
# aumentar el precio de los productos en un 10% #
for producto in productos:
    producto["precio"] *= 1.1 # aumenta el precio en un 10% #
# mostrar los productos con el precio aumentado #
for producto in productos:
    print(f"{producto['nombre']}: ${producto['precio']:.2f}")
print("------------------------")    
