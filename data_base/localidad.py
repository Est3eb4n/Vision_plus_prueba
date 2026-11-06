
def localidad():
    id_localidad = ();
    nombre_localidad = ();

    localidad = {
        "id":id_localidad,
        "nombre":nombre_localidad,
    }


    print('''
    1. ingresar una localidad
    2. mostrar la localidad
    ''')

    op = input("Ingrese una opccion:")

    while op == "1":
        try:
            input_id_localidad = input("Ingrese el id de la localidad: ")
            input_id_localidad = int(input_id_localidad)
        except ValueError:
            print("Error: Ingrese un valor válido para el id de la localidad.")
            continue

        try:
            input_nombre_localidad = input("Ingrese el nombre de la localidad: ")
            input_nombre_localidad = str(input_nombre_localidad)
        except ValueError:
            print("Error: Ingrese un valor válido para el nombre de la localidad.")
            continue

        localidad["id"] = input_id_localidad
        localidad["nombre"] = input_nombre_localidad



        print("La localidad ingresada es: ", localidad)
        op = input("Ingrese una opccion:")

    print("La localidad ingresada es: ", localidad)

localidad();