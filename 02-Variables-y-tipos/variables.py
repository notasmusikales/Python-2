""" Una variable es un contenedor de información 
 """

#creación de variables
texto = "Curso ERP/CRM"
texto2 = "Odoo"
numero = 25
decimal = 3.14

#Imprime el contenido de las variables en la consola
print (texto)
print (texto2)
print (numero)
print (decimal)

#concatena el contenido de las variables texto y texto2
nombre = "Noel"
apellido = "Gonzalez"
curso = "ERP/CRM"

print (nombre + " " + apellido + " " + curso)
print (f"{nombre} {apellido} {curso}") #otra forma de concatenar variables
print("Hola {} {} bienvenido al curso de {}".format(nombre, apellido, curso)) #otra forma de concatenar variables
print("Hola soy {} {} estoy en el curso de {}".format(nombre, apellido, curso)) #otra forma de concatenar variables