"""¿Qué es un Diccionario de datos?
Un Diccionario es una estructura de datos y un tipo de dato
en Python con características especiales que nos permite almacenar 
cualquier tipo de valor como enteros, cadenas, listas e incluso otras funciones.
Estos diccionarios nos permiten además identificar cada elemento por una clave (Key)."""
# #lista
# lista = ["juan","maria","carlos"]# string o cadena de texto 

# diccionario = { 
#     "nombre": "Diego",
#     "edad":25, 
#     "profesion":"profesor"
#     }

# productos = {
#     "televisor":15.000,
#     "celular":  30.000,
#     "portatil": 160.000
# }

# nombres = {"nombre": "carlos", "edad": 20, "cursos": ["Python","javascript","Nodejs"]}
# #print (nombres)

# # print (nombres["nombre"])
# # print (nombres["edad"])
# # print (nombres["cursos"])
# # print (nombres["cursos"][1])

# notas_estudiantes ={
#     "juan":[2.5, 3, 4.6],
#     "Ana": [3.5,4.6,4.9],
#     "Luis":[4,2.5,3.9]
# }

# print (notas_estudiantes["juan"])
#-------------------------Agregar datos a un diccionario--------------------------------------------------

# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30
#     }

# miDiccionario["profesion"] = "intructora"

# print(miDiccionario)

#-------------------------Editar datos a un diccionario--------------------------------------------------
# miDiccionario["edad"] = 31

# print(miDiccionario)

#-------------------------Eliminar datos a un diccionario--------------------------------------------------

# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30,
#     "profesion": "instructora"
#     }
# print(miDiccionario)

# # del miDiccionario["profesion"]
# # print(miDiccionario)
# prof = miDiccionario.pop("profesion")

# print(prof)
# print(miDiccionario)

#------------------------agregar multiples valores--------------------

# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30,
#     "profesion": "instructora"
#     }

# print(miDiccionario)

# nuevosDatos = {
#     "ciudad": "Cali",
#     "documento": 1234567,
#     "Telefono" : 22222
# }

# print(nuevosDatos)

# for clave, valor in nuevosDatos.items():
#     miDiccionario[clave] = valor

# print(miDiccionario)

#-------------------------metodo update()----------------------------------------------
# miDiccionario = {"nombre": "Diego"}

# #para agregar nuevos datos
# nuevosDatos = {
#     "profesion": "docente",
#     "Cidad": "cali",
#     "telefono": "1242343"
# }
# miDiccionario.update(nuevosDatos)

# print(miDiccionario)
#------------------------Eliminar multiples valores----------------------------------------------

# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30,
#     "profesion": "instructora"
#     }

# claveEliminar = ["edad","profesion"]

# for clave in claveEliminar:
#     if clave in miDiccionario:
#         del miDiccionario[clave]

# print(miDiccionario)        

#-------------------------comprension de diccionarios------------------------------------------
# miDiccionario = {
#     "nombre": "Sara", 
#     "edad": 30,
#     "profesion": "instructora",
#     "ciudad": "Bogota"
#     }
# claveEliminar =["edad", "ciudad"]
# ##creo un nuevo diccionario sin las caves a elimnar
# diccionarioFiltrado = {
#     clave: valor 
#     for clave, valor in miDiccionario.items() 
#     if clave not in claveEliminar}

# print(diccionarioFiltrado)
















