intentos = 0
limite_intentos = 3

while True:   
    intentos += 1
    print(f"intento numero {intentos}: Contraseña incorrecta.")
    if intentos >= limite_intentos: 
        print("Has alcanzado el limite de intentos.")
        break