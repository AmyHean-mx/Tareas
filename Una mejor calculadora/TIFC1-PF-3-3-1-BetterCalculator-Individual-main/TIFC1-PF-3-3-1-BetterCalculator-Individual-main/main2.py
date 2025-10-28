def addmultiplenumbers(numbers):
    """Suma todos los números de una lista."""
    return sum(numbers)

def multiplymultiplenumbers(numbers):
    """Multiplica todos los números de una lista."""
    result = 1
    for num in numbers:
        result *= num
    return result

def isiteven(num):
    """Devuelve True si el número es par, False si es impar o no entero."""
    if isinstance(num, int) and num % 2 == 0:
        return True
    elif isinstance(num, float) and num.is_integer() and int(num) % 2 == 0:
        return True
    else:
        return False

def isitaninteger(num):
    """Devuelve True si el número es entero, False en caso contrario."""
    return isinstance(num, int) or (isinstance(num, float) and num.is_integer())

def main():
    print("Bienvenido a tu calculadora mejorada")
    print("Opciones:")
    print("1. Sumar múltiples números")
    print("2. Multiplicar múltiples números")
    print("3. Verificar si un número es par")
    print("4. Verificar si un número es entero")
    
    opcion = input("Selecciona una opción (1-4): ")

    if opcion in ["1", "2"]:
        nums = input("Introduce los números separados por espacio: ")
        numeros = [float(x) for x in nums.split()]
        
        if opcion == "1":
            print("Resultado:", addmultiplenumbers(numeros))
        else:
            print("Resultado:", multiplymultiplenumbers(numeros))
    
    elif opcion == "3":
        num = float(input("Introduce un número: "))
        print("¿Es par?:", isiteven(num))
    
    elif opcion == "4":
        num = float(input("Introduce un número: "))
        print("¿Es entero?:", isitaninteger(num))
    
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
