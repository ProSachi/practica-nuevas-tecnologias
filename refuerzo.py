
# mi_lista = [1, "Hola", 3.14, True]

# print(mi_lista[0])      # Acceso por índice: 1
# mi_lista.append("nuevo") # Añadir elemento
# print(mi_lista)         # Salida: [1, 'Hola', 3.14, True, 'nuevo']

# mi_lista.append("Pan") # Añade al final 
# mi_lista.pop() # Quita del final 
# print(len(mi_lista)) # Obtiene el tamaño

# for item in mi_lista:
#     print(item)
#     print("Siguiente: \n")
# print("Una sola vez: \n")


# mi_diccionario = {
#     "nombre": "Ana", 
#     "edad": 28, 
#     "ciudad": {
#         "pais": "Ana", 
#         "barrio": 28, 
#         "direccion": {
#             "Interior" : "404"
#         }
#     }
#     }
# print(mi_diccionario)

# una_lista= [
#     {
#     "nombre": "Ana", 
#     "edad": 28, 
#     "ciudad": "Madrid"
#     },
#     {
#     "nombre": "Ana", 
#     "edad": 28, 
#     "ciudad": "Madrid"
#     },
#     {
#     "nombre": "Ana", 
#     "edad": 28, 
#     "ciudad": "Madrid"
#     }
# ]

# otro_diccionario = {
#     "ciudades": [1, "Hola", 3.14, True],
#     "Poblacion": [1, "Hola", 3.14, True]
# }

# print(mi_diccionario["nombre"]) # Acceso por clave: Ana
# mi_diccionario["edad"] = 29     # Modificar valor
# mi_diccionario["pais"] = "España" # Añadir nuevo par
# print(mi_diccionario)
# # Salida: {'nombre': 'Ana', 'edad': 29, 'ciudad': 'Madrid', 'pais': 'España'}



resultados_evaluacion = {
    "modulo": "Fundamentos",
    "calificaciones": [80, 90, 95, 70]
}
# Intento de extracción:
nota_mas_alta = resultados_evaluacion["calificaciones"][2]
print(nota_mas_alta)
