import random

numero_secreto = random.randint(1, 10)
intentos = 3

print("Adivina el número entre 1 y 10. Tienes 3 intentos.")

for i in range(intentos):
    intento = int(input("Ingresa tu número: "))
    if intento == numero_secreto:
        print("🎉 ¡Correcto! Adivinaste el número.")
        break
    else:
        print("❌ Incorrecto.")
        if i < intentos - 1:
            print("Te quedan", intentos - i - 1, "intentos.")
else:
    print("Se acabaron tus intentos. El número era:", numero_secreto)
