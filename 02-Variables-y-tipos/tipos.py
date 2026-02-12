#tipos
nada = None #NoneType
cadena = "Hola" #str entero = 1 #int flotante = 3.14 #float booleano = True #bool
entero = 100 #entero = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
flotante = 3.14 #flotante = 3.14, 2.71, 1.618, 0.577, 1.414, 2.71828, 3.14159, 1.61803, 0.57721, 1.41421
booleano = True #booleano = True, False
lista = [1, 2, 3] #listtupla = (1, 2, 3) #tuple conjunto = {1, 2, 3} #set diccionario = {"clave": "valor"} #dict 
listastring = ["Hola", "Mundo"] #lista de stringslistaint = [1, 2, 3] #lista de enteros listaflotante = [1.1, 2.2, 3.3] 
#lista de flotantes listabooleano = [True, False, True] #lista de booleanoslistamix = [1, "Hola", 3.14, True] #listamixta
tuplaNoCambia = (1, "Hola", 3.14, True) #tupla es inmutable, no se puede modificar su contenido, pero se puede acceder a sus elementos por su índice
diccionario = {
    "nombre": "Noel", "apellido": "Gonzalez", "clave3": "valor3"} #diccionario con claves y valores

#imprimir variables
print(cadena)
print(tuplaNoCambia)
print(diccionario)
print(nada)

print(entero)
print(flotante)
print(booleano)
print(lista)
print(listastring)



#imprimir el tipo de variable
print(type(cadena))

texto = "Hola soy un texto"
numero = str(778)
numero2 = 3
print (int(numero) + numero2) #concatenar texto con numero convirtiendo el numero a string
print(type(numero)) #el tipo de la variable numero es string
print (texto + " " + str(numero)) #el resultado de la concatenación es un string
print (type(numero)) #el tipo de la variable numero es string

numero3 = int("123") #convertir un string a entero
print (numero3 + 10) #el resultado es 133 porque se ha convertido el string a entero print (type(numero3)) #el tipo de la variable numero3 es entero    

numero3 = float("3.14") #convertir un string a flotante
print (numero3 + 1) #el resultado es 4.14 porque se ha convertido el string a flotante print (type(numero3)) #el tipo de la variable numero3 es flotante
