num1 = float (input ("Introduzca un primer número ") )
num2 = float (input ("Introduzca un segundo número "))

if (num2 == 0):
    print ("Error")
else:
    operacion =  float (num1 / num2)    #la operación dentro de la instrucción de donde se va a ejecutar
    print ("El resultado de la división es: "  + str(operacion) )

