E = int ( input ("Introduzca su edad: ") ) 
I = float ( input ("Introduzca sus ingresos mensuales: "))

#¿el usuario tiene que tributar o no?
if (E > 16 and I >= 1000):
    print ("El usuario tiene que tributar")
else:
    print ("El usuario NO tiene que tributar")