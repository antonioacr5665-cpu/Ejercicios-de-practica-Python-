try:
    numero = int(input(" Por favor, ingrese un número entero: "))
    doble = numero * 2
    print(f"El doble de {numero} es {doble}")
except ValueError:
    print("Error: Entrada no válida. Por favor, ingrese un número entero.")