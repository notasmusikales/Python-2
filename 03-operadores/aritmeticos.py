# Operadores aritmeticos
n01= 100
n02= 50 # operador de asignacion

suma = n01 + n02
resta = n01 - n02
mult = n01 * n02
div = n01 / n02
resto = n01 % n02

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", mult)
print("La division es: ", div) 
print("El resto es: ", resto)

print("La suma es: " + str(suma)) #concatenar texto con numero convirtiendo el numero a string
print("La resta es: " + str(resta)) #concatenar texto con numero convirtiendo el numero a string
print("La multiplicacion es: " + str(mult)) #concatenar texto con numero convirtiendo el numero a string
print("La division es: " + str(div)) #concatenar texto con numero convirtiendo el numero a string
print("El resto es: " + str(resto)) #concatenar texto con numero convirtiendo el numero a string

print(f"La suma es: {suma}") #otra forma de concatenar texto con numero usando f-string
print(f"La resta es: {resta}") #otra forma de concatenar texto con numero usando f-string
print(f"La multiplicacion es: {mult}") #otra forma de concatenar texto con numero usando f-string
print(f"La division es: {div}") #otra forma de concatenar texto con numero usando f-string 
print("El resto es: {}" .format(resto)) #otra forma de concatenar texto con numero usando format