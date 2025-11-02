
def sumar_numeros():
    try: 
        print("=== SUMADORA DE NUMEROS ENTEROS ===")
        numero1 = int(input("Ingrese el primer número entero: "))
        numero2 = int(input("Ingrese el segundo número entero: "))
        suma = numero1 + numero2

        print(f"\nResultado:")
        print(f"{numero1} + {numero2} = {suma}")

    except ValueError:
        print("Error: Entrada no válida. Por favor, ingrese números enteros.")