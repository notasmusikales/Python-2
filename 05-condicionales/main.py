"""
    # Condicional IF en Python
    
    si se cumplen una condición hacer esto
    
    si no se cumple hacer esto otro
    
    # Operadores de comparación
    == igual a
    != diferente a
    > mayor que
    < menor que
    >= mayor o igual que
    <= menor o igual que
    
    # Operadores lógicos
    and (y)
    or (o)
    
"""

# print("\n######### Ejemplo 1 ##########")
# color = input("Adivina mi color favorito: ")
    
# if color == "azul":
#     print("Ese color es mi favorito")
# else:
#     print("Ese color no es mi favorito")
# # Operadores de comparación
# """
# print("######### Ejemplo 2 ##########")
# == igual a
# != diferente a 
# > mayor que
# < menor que
# >= mayor o igual que
# <= menor o igual que    
# num1 = int(input("Ingrese un numero: "))
# num2 = int(input("Ingrese otro numero: "))
# """

# print("\n######### Ejemplo 2 ##########")
#  # year: 2026
# year = int(input("Ingrese el año actual: "))
# if year >= 2027:
#     print("Estamos en el futuro")
# elif year == 2026:
#     print("Estamos en el presente")
# else:
#     print("Estamos en el pasado")
    
# print("\n######### Ejemplo 3 ##########")

# nombre = "Noel"
# ciudad = "Santa Cruz"
# pais = "España"
# edad = 35
# mayoria_edad = 18
# if edad >= mayoria_edad:
#     print(f"{nombre} es mayor de edad")
#     if pais != "España":
#         print("El país de residencia no es España")
#     else:
#         print(f"El país de residencia es España en la ciudad de {ciudad}")
# else:
#     print(f"{nombre} no es mayor de edad")
    
   
# print("\n######### Ejemplo 4 ##########")

# dia = int(input("Ingrese el día de la semana (1-7): "))

# if dia == 1:
#     print("Lunes")
# else:    
#     if dia == 2:
#         print("Es Martes")
#     else:
#         if dia == 3:
#             print("Es Miércoles")
#         else:
#             if dia == 4:
#                 print("Es Jueves")
#             else:
#                 if dia == 5:
#                     print("Es Viernes")
#                 else:
#                     if dia == 6:
#                         print("Es Sábado")
#                     else:
#                         if dia == 7:
#                             print("Es Domingo")
#                         else:
#                             print("Número de día no válido")
                
                
# # -------- Otra forma de hacer el mismo ejemplo usando elif ----
# print("\n######### Ejemplo 4 con elif ##########")

# dia = int(input("Ingrese el día de la semana (1-7): "))

# if dia == 1:
#     print("Lunes")
# elif dia == 2:
#     print("Martes")
# elif dia == 3:
#     print("Miércoles")
# elif dia == 4:
#     print("Jueves")
# elif dia == 5:
#     print("Viernes")
# elif dia == 6:
#     print("Sábado")
# elif dia == 7:
#     print("Domingo")
# else:
#     print("Número de día no válido")
    
print("\n######### Ejemplo 5 ##########")  
edad_minima = 18
edad_maxima = 65
valor = int(input("Tienes edad de trabajar? Ingrese su edad: "))
print(type(valor))
edad_oficial = int(valor)
print(type(edad_oficial))

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Estas en edad de trabajar")
else:
    print("No estas en edad de trabajar")
    
print("\n######### Ejemplo 6 ##########")
pais = input("Dime un país de habla hispana: ")

if pais == "México" or pais == "España" or pais == "Colombia":
    print(f"El país {pais} es de habla hispana")
else:
    print(f"El país {pais} no es de habla hispana :(")
    ##########################
    if pais != "México" and pais != "España" and pais != "Colombia":
    print(f"El país {pais} es de habla hispana")