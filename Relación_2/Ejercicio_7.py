correo =  input ("Introduzca su correo electrónico: ")
dominio = correo.split ("@")[1] #divide por la @ y coge la segunda parte
nombre = correo.split ("@")[0] #divide por la @ y coge la primera parte


correo = nombre + "@" + dominio.replace(dominio,"ceu.es")

print (correo)