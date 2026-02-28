def jugar_lingo():
    secreta = "tiger"
    print("¡Bienvenido al Lingo! Intenta adivinar la palabra de 5 letras.")

    while True:
        intento = input("\nIntroduce tu intento: ").lower()
        
        # Validación de longitud
        if len(intento) != 5:
            print("Error: La palabra debe tener exactamente 5 letras.")
            continue

        # Si adivina la palabra, termina el juego
        if intento == secreta:
            print(f"Clue: [t][i][g][e][r]")
            print("¡Felicidades! Has ganado.")
            break

        pista = ""
        # Comparamos letra por letra
        for i in range(5):
            if intento[i] == secreta[i]:
                pista += f"[{intento[i]}]"
            elif intento[i] in secreta:
                pista += f"({intento[i]})"
            else:
                pista += intento[i]
        
        print(f"Clue: {pista}")

# Ejecutar el juego
jugar_lingo()