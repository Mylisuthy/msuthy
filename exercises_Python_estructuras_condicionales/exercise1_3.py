usuario_esperado = "admin"
contrasena_esperada = "admin123"
codigo_verificacion = "12345"
usuario = input("Ingresa tu usuario: ")
contrasena = input("Ingresa tu contraseña: ")
if usuaruio == usuario_esperado and contrasena == contrasena_esperada:
    print("Inicio de sesión exitoso.")
    codigo = input("Ingresa el código de verificación que te emos enviado(simulado): ")
    if codigo == codigo_verificacion:
        print("Código de verificación correcto. Acceso concedido.")
    else:
        print("Código de verificación incorrecto. Acceso denegado.")
else:
    print("Usuario o contraseña incorrectos. Acceso denegado.")