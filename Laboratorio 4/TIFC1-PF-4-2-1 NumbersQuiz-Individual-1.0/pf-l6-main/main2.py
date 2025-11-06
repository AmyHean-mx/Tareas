def trivia_fetch(num):
    """
    Esta función recibe un número y devuelve un diccionario con una trivia sobre ese número.
    """
    trivia = {
        1: "1 es el primer número natural.",
        2: "2 es el único número par que es primo.",
        3: "3 es el número de lados de un triángulo.",
        4: "4 representa las estaciones del año.",
        5: "5 son los sentidos del ser humano.",
        6: "6 es el número de caras de un cubo.",
        7: "7 es considerado un número de buena suerte.",
        8: "8 es el número de planetas en el sistema solar.",
        9: "9 es un número cuadrado perfecto (3x3).",
        10: "10 es la base del sistema decimal."
    }

    # Si el número está en el diccionario, devuelve su trivia, si no, devuelve un mensaje por defecto
    fact = trivia.get(num, f"No tengo una trivia para el número {num}.")
    return {
        "number": num,
        "fact": fact
    }


def main():
    print("¡Bienvenido al Quiz de Números!")
    try:
        numero = int(input("Ingresa un número del 1 al 10: "))
        resultado = trivia_fetch(numero)
        print(f"\nTrivia sobre el número {resultado['number']}: {resultado['fact']}")
    except ValueError:
        print("Por favor, ingresa un número válido.")


if __name__ == "__main__":
    main()
