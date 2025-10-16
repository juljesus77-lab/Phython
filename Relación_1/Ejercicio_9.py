numero = input ("Ingrese por la cantidad a invertir: ")
interes = input ("Ingrese como numero el interés anual: ")
años = input ("Ingrese por el número de años que se va a invertir: ")

porcentaje_interes = float(interes) / 100 

capital = float(numero) * (1 + float(porcentaje_interes) / 100) ** int(años) # Cálculo del capital final

print ("El capital obtenido en la inversión es de : " + str(round(capital,2)))
