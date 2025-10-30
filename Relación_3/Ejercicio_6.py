# Grupo A: mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N
# Grupo B: Resto

N = input ("Introduzca su nombre (sin tildes): ")   #poniéndo tildes no funciona
S = input ("Introduzca su género en formato 'M o F:' ")

primera_letra = N[0]
primera_letra_mayus = primera_letra.upper()  #convierte la primera letra a mayúscula para que no de fallos

if ("A" <= primera_letra_mayus <= "L" and S == "F"):
    print ("Perteneces al Grupo A")
elif ("O" <= primera_letra_mayus <= "Z" and S == "M"):
    print ("Perteneces al Grupo A")
else: 
    print ("Perteneces al Grupo B")

    #lo podría revisar, pero parece que está bien

