frutas = ["manzanas", "peras", "uvas","banano"]  
numeros = [89, 87,65,78,56]

frutas.append("sandia")#para agregar un elemento a la lista
frutas.insert(0,"papaya")#para agregar un elemento en una posicion especifica de la lista
frutas.extend(["mango","kiwi","lulo"])#agregar multiples elementos a la lista
frutas[8] = "mora" # editar un elemento de la lista
frutas.remove("papaya")#para remover un elemento de la lista

del frutas[7]#para eliminar un elemento de la lista con el numero del elemento
del frutas[0:4]#eliminmos por rangos

frutas.clear()

print(frutas)
# nuevafruta = frutas.pop(0)# me salal de la lista el elemento y lo agrega a una varible

# print(frutas)
# print(nuevafruta)

# for i in frutas:
#     print(i)

###-------------------------EJERCICIO 1-------------------------------------------------------------
# Escribe un programa en Python que permita al usuario crear una lista de compras. 
# El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno 
# y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, 
# el programa debe imprimir la lista completa de compras en orden.
# Requisitos:
# El programa debe permitir al usuario ingresar productos hasta que decida detenerse.
# Después de ingresar cada producto, el usuario debe ser preguntado si desea agregar otro producto.
# Si el usuario decide que no quiere agregar más productos, el programa debe mostrar la lista completa de compras.

#
'''Introduce un producto para la lista de compras: Leche
Quieres agregar otro producto? (sí/no): sí
Introduce un producto para la lista de compras: Pan
¿Quieres agregar otro producto? (sí/no): sí
Introduce un producto para la lista de compras: Huevos
¿Quieres agregar otro producto? (sí/no): no

Tu lista de compras es:
- Leche
- Pan
- Huevos'''

# lista = []
# while True:
#     producto = input("Ingrese su producto a la lista de compras: ")

#     lista.append(producto)

#     continuar = input("¿quiere agregar otro producto?(si / no): ").lower() #convertir mayusculas a minisculas

#     if continuar == "no":
#         break

# print("---\n Tu lista de compras es:-----")

# for item in lista:
#     print(f"-{item}")

#--------------------EJERCICIO 2-----------------------------------------------
"""Escribe un programa en Python que solicite al usuario ingresar una lista de números enteros.
Luego, el programa debe calcular e imprimir la suma de todos los números ingresados. 
El programa debe continuar solicitando números hasta que el usuario decida dejar de ingresar más.
Requisitos:
El programa debe permitir al usuario ingresar números uno por uno.
Después de ingresar cada número, el usuario debe ser preguntado si desea agregar otro número.
Si el usuario decide que no quiere agregar más números, el programa debe calcular y mostrar 
la suma total de los números ingresados."""

#-----------------------------EJERCICIO 3--------------------------------------------------
"""Escribe un programa en Python para gestionar una lista de contactos. 
El programa debe permitir al usuario realizar las siguientes operaciones:

Agregar un contacto a la lista, incluyendo un nombre y un número de teléfono.
Eliminar un contacto de la lista especificando el nombre del contacto.
Mostrar todos los contactos en la lista, con el formato "Nombre: Número de teléfono".
El programa debe mostrar un menú con las opciones disponibles y seguir funcionando hasta 
que el usuario elija salir. Asegúrate de manejar situaciones en las que el usuario intente
eliminar un contacto que no está en la lista y que el programa informe adecuadamente al usuario.

Requisitos:
El programa debe permitir al usuario ingresar contactos con un nombre y un número de teléfono.
Debe ser posible eliminar un contacto buscando por el nombre.
Debe mostrar todos los contactos en la lista en un formato claro.
El programa debe seguir ejecutándose hasta que el usuario decida salir."""

#---------------------------EJERCICIO 4------------------------------------------------------------------
"""Escribe un programa en Python que permita al usuario crear una lista de sus películas favoritas.
El programa debe permitir al usuario realizar las siguientes acciones:

Agregar una película a la lista.
Eliminar una película especificando su nombre.
Mostrar todas las películas en la lista.
Buscar si una película específica está en la lista.
El programa debe ofrecer estas opciones en un menú y continuar funcionando hasta que el usuario decida salir."""

#---------------------------EJERCICIO 5------------------------------------------------------------------
"""Escribe un programa en Python para gestionar una lista de tareas pendientes. El programa debe implementar un CRUD 
(Crear, Leer, Actualizar, Eliminar) para las tareas y permitir al usuario realizar las siguientes acciones:

Crear una nueva tarea: Añadir una tarea a la lista con una descripción y una fecha de vencimiento.
Leer todas las tareas: Mostrar todas las tareas actuales, incluyendo su descripción y fecha de vencimiento.
Actualizar una tarea: Modificar la descripción y/o la fecha de vencimiento de una tarea existente especificando 
su número de identificación.
Eliminar una tarea: Eliminar una tarea de la lista especificando su número de identificación.
El programa debe ofrecer un menú de opciones y seguir funcionando hasta que el usuario decida salir. Asegúrate 
de manejar situaciones en las que el usuario intente realizar acciones sobre tareas que no existen y proporciona
mensajes adecuados.

Requisitos:

El programa debe permitir al usuario ingresar una descripción y una fecha de vencimiento para cada nueva tarea.
Cada tarea debe tener un identificador único que se utiliza para actualizar o eliminar la tarea.
El programa debe mostrar todas las tareas en un formato claro.
El usuario debe poder actualizar la descripción y/o la fecha de vencimiento de una tarea.
El usuario debe poder eliminar una tarea especificando su identificador."""



















