def trivia_fetch(num):
    # Devuelve un diccionario con trivia sobre el número dado.
    trivia = {
        42: "El número 42 es conocido como la respuesta a la vida, el universo y todo lo demás.",
        1000: "El número 1000 es un número redondo que representa mil unidades.",
    }

    # Si el número no está en el diccionario, genera un texto genérico
    text = trivia.get(num, f"El número {num} es un número interesante.")

    return {
        "number": num,
        "text": text
    }

def main():
    number = int(input("Introduce un número: "))
    info = trivia_fetch(number)
    print(f"\nDato curioso sobre {info['number']}: {info['text']}")

if __name__ == "__main__":
    main()
