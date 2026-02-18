# Bucle for - Examples
contador = 0

for contador in range(0,5):
    print(f"voy por el " + str(contador))
          
    resultado = resultado + contador
    print(f"El resultado es: {resultado}")    


# 1. Iterating through a list
print("1. Iterating through a list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# 2. Iterating through a range
print("\n2. Iterating through a range:")
for i in range(5):
    print(i)

# 3. Iterating with start and stop
print("\n3. Range with start and stop:")
for i in range(1, 4):
    print(i)

# 4. Iterating with step
print("\n4. Range with step:")
for i in range(0, 10, 2):
    print(i)

# 5. Iterating through a string
print("\n5. Iterating through a string:")
word = "Python"
for letter in word:
    print(letter)

# 6. Using enumerate to get index and value
print("\n6. Using enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 7. Nested for loop
print("\n7. Nested for loop:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")