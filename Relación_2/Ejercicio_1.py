#Escribir un programa que pregunte el nombre del usuario en la consola y un número
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
#como el número introducido.
nombre_usuario = input ("Introduce tu nombre de usuario: ")
numero_int = input ("Introduce un número entero: ") 

print ( (nombre_usuario + "\n" ) * int(numero_int) ) 

#salto de linea es \n. Hay que ponerlo como texto