compatible = 0
pregunta = input("hola señorita, que tal si te ago unas preguntas para saber que tan compatibles somos?")
if pregunta == "no":
     print("coma MMMMMM chao")
elif pregunta == "si":
     print("genial comencemos, pero quiero que me respondas si no o que prefieres porfaaaaaaaa ")
     pregunta1 = input("te gustan los video juegos?").lower()
     if pregunta1 == "si":
          compatible = compatible + 10
     elif pregunta1 == "no":
            compatible = compatible + 5
     

     pregunta2 = input("te gusta el anime?").lower()
     if pregunta2 == "si":
           print ("eso te da muchos puntos")
           pregunta2_1 = input("tambien lees manga?").lower()
           if pregunta2_1 == "si":
                 compatible = compatible + 20
           elif pregunta2_1 == "no":
                 compatible = compatible + 10
     
     pregunta3 = input("prefieres perros o gatos").lower()
     if pregunta3 == "perros":
           compatible = compatible +10
     elif pregunta3 == "gatos":
           compatible = compatible +10
          


