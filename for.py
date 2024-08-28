#sintaxis bucle for
#for variable in secuencia:
    #bloque de codigo

# for i in range(2,10,2):
#     print(i)
#------------------------------------------
# frutas = ["manzana","pera","sandia","banano","piña","fresa","uva"]
# for i in frutas:
#     if i == "pera":
#         print(f"la fruta es {i}")
#         break
#-----------------------------------------------------
# numeros = [2,4,6,8,10]
# suma = 0
# for i in numeros:
#     suma += i

# print(f"la suma total de los elementos de la lista es: {suma} ")    
#---------------------------------------------------------------------------
# numeros = [ 3,5,8,10,11,14,16,21,25,30]
# for i in numeros:
#     if i % 2 == 0:
#         print(f"{i} es par")
#--------------------------------------------------------------------------
# Escribe un programa en Python que recorra una cadena
# de texto y cuente cuántas vocales (a, e, i, o, u) hay en la cadena.
# cadena = "bienvenido a python, estoy aprendiendo a programar" 
# vocales = "aeiou"
# contador = 0

# for letra in cadena:
#     if letra in vocales:
#         contador += 1

# print(f"el numero de vocales de la cadena son: {contador}")        

#-----------------------------------------------------------------
# Crea un programa en Python que solicite al usuario un número entero
# y luego genere la tabla de multiplicar de ese número del 1 al 10.
# numero = int(input("ingrese un numero"))
# for i  in range(1,11):
#     print(f"{numero} X {i} = {numero * i }")

#--------------------for anidado   ----------------------------------------------
# for i in range(1,11):
#     for j in range(1,11):
#         print(f"{i} X {j} = {i * j}")
#     print("-" * 20 )
# print("exit")    
#------------------------------------------------------------------------------------------

# Escribe un programa en Python que dibuje un triángulo de asteriscos,
# donde el número de filas es determinado por el usuario
# fila = int(input("ingrese el numero de filas"))

# for i in range(1, fila, +1):
#     for j in range(i):
#         print("*", end= "")
#     print() ## nueva linea   


