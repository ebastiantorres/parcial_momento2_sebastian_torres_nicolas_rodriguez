def editar_gasto():
    print("\n--- EDITAR GASTO ---")

    placa = input("Ingrese la placa del gasto a editar: ")

    for gasto in gastos:
        if gasto["placa"] == placa:

            nuevo_concepto = input("Nuevo concepto: ")

            try:
                nuevo_valor = float(input("Nuevo valor: "))
            except ValueError:
                print("Debe ingresar un número válido.")
                return

            gasto["concepto"] = nuevo_concepto
            gasto["valor"] = nuevo_valor

            print("Gasto actualizado correctamente.")
            return

    print("No se encontró esa placa.")