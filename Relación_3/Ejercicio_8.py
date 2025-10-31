puntuacion = float( input ("Introduzca la puntuación que ha recibido: ") ) 
nivel = 2400
operacion = puntuacion * nivel 

if (puntuacion == 0.0 ):
    print ("Inaceptable" + "-------" + str(operacion) + "€" )
elif (puntuacion == 0.4 ):
    print ("Aceptable" + "-------" + str(operacion) + "€")
elif (puntuacion >= 0.6):
        print ("Meritorio" + "-------" + str(operacion) + "€" ) 



