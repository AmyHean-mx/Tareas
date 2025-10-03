# Condicionales if, elif, else

edad = 4

if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

numero = 5
while numero < 21:
    if numero % 15 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")   
    else:
        print(numero)   
    numero += 1

for i in range(1000):
    print("Iteracion numero:", i)