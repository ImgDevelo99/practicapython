# dia = 0
# semana = ["lunes","martes","miercoles","jueves","viernes", "sabado","domingo"] 

# while dia < 7:
#     print("Hoy es: ", semana[dia])
#     dia += 1
#----------------------------------------------------------------------------------------
# contador = 1
# while contador <=5:
#     print(contador)
#     contador += 1 # contador = contador +1

# contador = 1
# while (contador <= 5):
#     contador = contador + 1
#     print("iteracion numero ",contador)    
#------------------------------------------------------------
# contador = 0
# while contador < 15:
#     contador += 1
#     print("Iteracion ", contador)
#     if contador == 5:
#         break
#     print("fin")
#---------------------------------------------------------------------------------------------------------
# Escribe un programa en Python que use un bucle while para sumar números ingresados por el usuario hasta
#  que se ingrese un número negativo. Luego, muestra la suma total.
# suma = 0
# while True:
#     numero = int(input("ingrese un numero positivo (si quiere salir ingrese uno negativo ):"))
#     if numero < 0:
#         break
#     suma += numero 
#     print("la suma total es: ",suma) 
# print("la suma total es: ",suma) 

#--------------------------------------------------------------------------------------------------
# Escribe un programa en Python que utilice un bucle while para encontrar y
#  mostrar el primer número divisible por 7 en el rango del 1 al 100.
# numero = 4
# while numero <= 100 :
#     if numero % 7 == 0:
#         print("El nuemro divisible por 7 en el rango es: ",numero)
#         break
#     numero += 1
#-----------------------------------------------------------------------------------------------------
# '''
# Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe
# cuántos tienen notas mayores o iguales a 7 y cuántos menores.
# '''

# notas_mayores = 0
# notas_menores = 0
# i = 1
# while i <= 10:
#     nota = float(input(f"ingrese la nota {i}:"))
#     if nota >= 7 :
#         notas_mayores += 1 #nota_mayor = nota_mayor -7 
#     else:
#         notas_menores += 1

#     i += 1

# print("l cantidad de notas del estudiantes mayores a 7 son: ",notas_mayores)     

# print("l cantidad de notas del estudiantes menores a 7 son: ",notas_menores) 
# #-------------------------------------------------------------------------------------
# #  crear un programa donde cuente de forma desendentes 10 segundos para que explote una bomba
# print("!BOMMMMMMMMMMMMMMMMMMMMMMMMMM!!!!!!!!")        
# segundos = 10
# while segundos > 0:
#     print("la bomba explotara en: ",segundos, "segundos")
#     segundos -= 1

# print("!BOMMMMMMMMMMMMMMMMMMMMMMMMMM!!!!!!!!")
#-----------------------------------------------------------------------------------------------------------
# Árbol de navidad en Python. Imprime un árbol de navidad formado con * haciendo uso del while
# y de la multiplicación deun entero por una cadena, cuyo resultado en Python es replicar la cadena.
z = 7
x = 1
while z > 0 :
    print(" "* z + "*"  * x + "" * z)
    x +=2
    z -=1