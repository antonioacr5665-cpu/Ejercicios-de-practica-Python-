def mostrar_promedio_visual():
    print("=" * 40)
    print(" " * 10 + "Calculadora de Promedio") 
    print("=" * 40)

    try:
        mum1 = float(input("📊 ingresa el primer numero"))
        mum2 = float(input("📊 ingresa el segundo numero"))

        suma = mum1 + mum2
        promedio = suma / 2

        print("\n" + "=" * 40)
        print("PROCESO DE CALCULO")
        print(f"({mum1} + {mum2}) / 2 = {promedio}")
        print("_" * 40)

        print(f"\n🎯 EL PROMEDIO ES: {promedio:.2f}")
        print("=" * 40)

    except ValueError:
        print("\n❌ Error: Debe ingresar un número real válido.")

        mostrar_promedio_visual()
        input("\nPresione Enter para continuar...")
