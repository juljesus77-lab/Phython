num = input("Introduce la cantidad de dinero depositada en la cuenta de ahorros ")
interes = input("Introduce el interés anual (porcentaje) ")
años = input("Introduce el número de años que el dinero permanecerá en la cuenta ")

porcentaje_interés = (1 + (float(interes) / 100))
total = round(float(num),2) * round(str(porcentaje_interés),2)  ** int(años)



print ("El capital total después después de " + str(años) + "años es "  + str(total) ) 


#(REVISAR)
