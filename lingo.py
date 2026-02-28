def jugar_lingo():
    secreta = "tiger"  # Puedes cambiarla por cualquier palabra de 5 letras
    intento = input("Introduce una palabra de 5 letras: ").lower()
    pista = ""

    # Recorremos cada posición de la palabra (0 a 4)
    for i in range(5):
        if intento[i] == secreta[i]:
            # Letra correcta en posición correcta
            pista += f"[{intento[i]}]"
        elif intento[i] in secreta:
            # Letra está en la palabra pero en otra posición
            pista += f"({intento[i]})"
        else:
            # La letra no está
            pista += intento[i]
    
    print(f"Clue: {pista}")

# Llamamos a la función
jugar_lingo()