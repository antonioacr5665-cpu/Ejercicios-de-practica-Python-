try:
    print("=== Calculadora de Mitad ===")
    numero = float(input("Ingrese un número Real (decimal): "))
    mitad = numero / 2

    print(f"\nResultado:")
    print(f"Numero ingresado: {numero}")
    print(f"Mitad: {mitad}")

except ValueError:
    print("Error: Debe ingresar un número real válido.")