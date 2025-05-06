datpelicula = str(input("que genero de pelicula te gusta?(accion, comedia, terror, etc): ")).lower()
edad_user = int(input("cuantos años tienes?: "))
if edad_user <= 13:
    if datpelicula in ["terror",  "accion"]:
        print(f"tu genero favorito es {datpelicula}, pero a tu edad no es recomendable ver peliculas de adultos")
        respuestaedad = input("te gustaria que te recomiendemos una pelicula acorde con tu edad o prefieres saltarte esa regla?:(saltarse o no saltarse) ")
        if respuestaedad == "saltarse":
            print("genial, te recomendamos la peliculas  asociadas a tu genero favorito")
        elif respuestaedad == "no saltarse":
            print("aqui tienes algunas peliculas que recomendamos acordes a tu edad:")
        else:
            print(f"tu genero favorito es {datpelicula}. es una buena eleccion para tu edad")
else:   
    print(f"tu genero favorito es {datpelicula}, te recomendamos que veas peliculas de ese genero")

# Versión en función: recomendar_pelicula()
def recomendar_pelicula():
    genero = input("¿Qué género de película te gusta? (acción, comedia, terror, etc.): ").lower()
    edad = int(input("¿Cuántos años tienes?: "))

    if edad <= 13:
        if genero in ["terror", "acción"]:
            print(f"Tu género favorito es '{genero}', pero a tu edad no es recomendable ver películas para adultos.")
            respuesta = input("¿Te gustaría que te recomendemos una película acorde con tu edad o prefieres saltarte esa regla? (saltarse / no saltarse): ").lower()

            if respuesta == "saltarse":
                print("Genial, te recomendamos películas asociadas a tu género favorito.")
            elif respuesta == "no saltarse":
                print("Aquí tienes algunas películas recomendadas acordes a tu edad.")
            else:
                print("Opción no válida. Intenta nuevamente.")
        else:
            print(f"¡Perfecto! Aquí tienes algunas películas de {genero} recomendadas para tu edad.")
    else:
        print(f"Tu género favorito es '{genero}', te recomendamos ver películas de ese género.")

# Llamada a la función
recomendar_pelicula()
