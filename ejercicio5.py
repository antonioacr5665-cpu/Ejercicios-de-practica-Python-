try:
    print("=== Verificador de Mayoría de Edad ===")
    edad = int(input("📅\ Ingresa tu edad: "))

    if edad >= 18:
        print("🎉 Eres mayor de edad.")
    else:
        print("🚫 Eres menor de edad.")

        
except ValueError:
    print("❌ Error: Debe ingresar un número válido.")