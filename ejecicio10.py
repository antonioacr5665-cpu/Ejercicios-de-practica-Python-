palabra = input("Ingrese una palabra: ").strip()
if palabra:
    cantidad = len(palabra)
    print(f"Analisis de la palabra:")
    print(f"Palabra: {palabra}")
    print(f"Cantidad de caracteres: {cantidad}")
    print(f"Caracteres individuales: {list(palabra)}")

else:
    print("Error: No se ingreso ninguna palabra.")

