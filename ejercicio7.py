def obtener_letras():
    """solicita y valida que el usuario ingrese axactamente una letra"""
    while True: 
        entrada = input("Escribe una letra:").strip()

        if len(entrada) == 1 and entrada.isalpha():
            return entrada.upper()
        else:
            print("Error: Debes ingresar exactamente una letra. intenta nuevamente")

            letra = obtener_letras()
            print(f"\n✓ La letra validada: {letra}")

