caracter = input("ingresa un caracter: ").strip()

if len(caracter) == 1: 
        if caracter.ipper() ==  'A':
                print("correcto")
        else: 
                print(f" incorrecto. se esperaba 'A' pero se ingreso '{caracter}'")
else:
        print("error: debe ingresar un solo caracter") 