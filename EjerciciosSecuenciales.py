# palabra1 = "hola"
# palabra2 = "mundo"
# palabra3 = "python"

# frase = palabra1 + " " + palabra2 + " " + palabra3
# print("la frase completa es: ", frase) 
#---------------------------------------------------------------------- 


# # pograma donde se convierta los grados C a grados F

# celsius = float(input("Ingrese la temperatura en grados Celsius"))

# #C *9/5 + 32
# fahrenheit = celsius * 9/5 + 32
# print("la temperatura en grados fahrenheit es: ",fahrenheit)
#--------------------------------------------------------------------------

# ancho = float(input("ingrese el ancho del rectangulo: "))
# altura = float(input("ingrese la altura del rectangulo: 10"))

# area = ancho * altura
# print("el area del rectangulo es: ", area)
#----------------------------------------------------------------------------
# import math
# # resultado = math.sqrt(168)
# # print("la raiz cuadrada es: ",resultado)

# x1 = float(input("ingrese la coordenada X del primer punto"))
# y1 = float(input("ingrese la coordenada Y del primer punto"))

# x2 = float(input("ingrese la coordenada X del segundo punto"))
# y2 = float(input("ingrese la coordenada Y del segundo punto"))

# distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2) 

# print("la distancia entre los dos puntos es: ",distancia)
#-------------------------------------------------------------------------------

# Crea un programa que calcule el monto total después de aplicar interés compuesto. 
# El usuario debe ingresar el capital inicial, la tasa de interés anual y el número de años.
# La fórmula del interés compuesto es:
# M =P(1 + r/100)t

# M es el monto final,
# 
# P es el capital inicial,

# r es la tasa de interés anual,
# 
# t es el número de años.
# capitalI = float(input("Ingrese el capital inicial: "))
# tasaI = float(input("Ingrese la tasa de interes anual (%): "))
# anios = float(input("Iingrese el numero de años: "))

# montoFinal = capitalI * (1 + tasaI/100) **anios
# print("el monto total despues de: ",anios, "años es: ",montoFinal)

#-----------------------------------------------------------------------
# texto = input("ingrese el mensaje")

# mayuscula = texto.upper()#en miniscula
# minuscula = texto.lower()# en miniscula
# titulo = texto.title()#inicial en mayuscula

# print("el testo en mayuscula es: ", mayuscula)
# print("el testo en minuscula: ", minuscula)
# print("el testo en titulo es: ", titulo)
#----------------------------------------------------------------------

# Crea un programa en Python que muestre la fecha y hora actual en un format
# o legible utilizando el módulo datetime.
# import datetime
# fechaHoraActual = datetime.datetime.now()

# print(fechaHoraActual)
# #formato fecha y hora
# fechaFormato = fechaHoraActual.strftime("%d/%m/%Y %H:%M:%S")

# print("la fecha y la hora actual: ", fechaFormato)
#-----------------------------------------------------------------------------

#Escribe un programa en Python que genere un número aleatorio entre 1 y 100 utilizando el módulo random.

# import random
# numeroAleatorio = random.randint(1, 100)

# print("el numero aleatorio generado es: ",numeroAleatorio)
#------------------------------------------------------------------------------------------------
