"""
tiliza un diccionario para gestionar el inventario de una tienda de frutas.
El diccionario almacenará las frutas como claves y sus cantidades como valores.
Implementaremos las funciones para agregar nuevas frutas al inventario, actualizar las cantidades, 
eliminar frutas y mostrar el inventario.
"""

# inventario ={
#     "manzanas": 100,
#     "peras": 40,
#     "naranjas": 60,
#     "papaya": 130
# }

# ##agregar--------------------------------------------------------------
# frutasActualizar = [
#     ("bananos", 20),
#     ("fresas",60),
#     ("piñas", 30)
# ]

# for frutas, cantidad in frutasActualizar:
#     if frutas in inventario:
#         inventario[frutas] += cantidad
#         print(f"se ha agregado {cantidad} unidad de {frutas}. total: {inventario[frutas]} unidades")
#     else:
#         inventario[frutas] = cantidad
#         print(f"{frutas} añadidas al inventario con {cantidad} unidades.")   
        
# print(f"nuevo inventario{inventario}")   
# print("----------------------------------------------------------------------------------------------------")     

# ##eliminar------------------------------------------------------------------
# frutasEliminar = ["fresas", "manzanas"]

# for fruta in frutasEliminar:
#     if fruta in inventario:
#         del inventario[fruta]
#         print(f"{fruta.capitalize()}  elimadas del inventario ")
#     else:
#         print(f"{fruta.capitalize()} no encontadas en el inventario ")    


# print("********\ninventario actual*******")
# for fruta,cantidad in inventario.items():
#     print(f"{fruta}: {cantidad} unidades")

# print(f"inventario final{inventario}")    
#---------------------------------------------------------------------------------------------------------------------
"""
Gestión de Calificaciones de Estudiantes
Supongamos que tienes un grupo de estudiantes y quieres almacenar sus calificaciones
en un diccionario. Luego, puedes agregar nuevas calificaciones, actualizar las existentes
y eliminar estudiantes del registro.
"""
# calificacion = {
#     "juan":[2.4, 3 , 4,5],
#     "pepe": [3.4, 2, 1.4],
#     "carlos": [4.7, 4.2, 4]
# }
# #agregar
# calificacion["juan"].append(4.5)

# #añadir
# calificacion["diego"] = [3.7, 4.2, 3]

# #Actualizar
# calificacion["pepe"][0] = 5

# #eliminar
# del calificacion["carlos"]

# for estudiantes, nota in calificacion.items():
#     print(f"{estudiantes}: {nota}")

"""
Gestión de Inventario de Productos
El usuario podrá:
Agregar un nuevo producto o actualizar la cantidad de un producto existente.
Eliminar un producto del inventario.
Mostrar el inventario actual.
solicitar los datos al usuario
"""

inventario = {}