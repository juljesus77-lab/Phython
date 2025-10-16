#Los teléfonos de una empresa tienen el siguiente formato
#prefijo-número-extension donde el prefijo es el código del país +34, y la
#extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un
#programa que pregunte por un número de teléfono con este formato y muestre por
#pantalla el número de teléfono sin el prefijo y la extensión.

num_telefono = input ("Introduce un número de teléfono con el formato +34-913724710-56: ")
num_sin_prefijo_ni_extension = num_telefono [4:13]


print (num_sin_prefijo_ni_extension)

#le metes el numero con prefijo y extensión y te lo tiene que devolver
#sin prefijo ni extensión