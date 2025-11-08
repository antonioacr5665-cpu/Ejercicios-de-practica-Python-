def obtener_nombre():
    """solicita y valida el nombre del usuario """
    while True:
        nombre = input("Por favor, ingresa tu nombre: ").strip()

        if nombre and nombre.replace(' ', '').isalpha():    
            return nombre.title()
        else:
            print("Error: El nombre debe contener solo letras. Inténtalo de nuevo.")
            nombre_valido = obtener_nombre()
            print(f"!Hola, {nombre_valido}! Es un placer tenerte como compañero curso de ciberseguridad.")

