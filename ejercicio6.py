respuesta = input("Tienes Internet en casa (1 = si,0 = no): ")

try:
    internet_casa = bool(int(respuesta))
    print(f"resultado: {internet_casa}")
    print(f"tipo de dato: {type(internet_casa)}")
except ValueError:
    print("Por favor, ingresa 1 para 'si' o 0 para 'no'.")
