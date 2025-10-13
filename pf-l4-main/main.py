num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
num3 = float(input("Introduce el tercer número: "))
operacion = input("Escribe la operación que deseas realizar (por ejemplo: 2 + 4 - 3): ")
tipo = input("Introduce el tipo de operación (suma, resta, multiplicación, división, módulo): ")

resultado = num1 + num2
print("El resultado de la suma es:", resultado)

resultado = num2 - num1
print("El resultado de la resta es:", resultado)

resultado = num1 * num2
print("El resultado de la multiplicación es:", resultado)   

resultado = num1 / num2
print("El resultado de la división es:", resultado)

resultado = num1 % num2
print("El resultado del módulo es:", resultado)

if tipo == "suma":
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)
elif tipo == "resta":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)
elif tipo == "multiplicación":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)   
elif tipo == "división":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("No se puede dividir entre 0.")
elif tipo == "módulo":
    if num2 != 0:
        resultado = num1 % num2
        print("El resultado del módulo es:", resultado)
    else:
        print("No se puede calcular el módulo con divisor 0.")

resultado = num1 + num2 + num3
print("El resultado de la suma es:", resultado)

resultado = eval(operacion)

print("El resultado es:", resultado)