#Escribir un programa que pregunte el nombre completo del usuario en la consola y
#después muestre por pantalla el nombre completo del usuario tres veces, una con
#todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
#primera letra del nombre y de los apellidos en mayúscula. El usuario puede
#introducir su nombre combinando mayúsculas y minúsculas como quiera

nombre_completo = input("Introduce tu nombre completo: ")
letra_minúscula = nombre_completo.lower()
letra_mayúscula = nombre_completo.upper()
letra_primera_mayúscula = nombre_completo.title() #primera letra en mayúscula

print ( letra_minúscula + "\n" + letra_mayúscula + "\n" + letra_primera_mayúscula + "\n")





