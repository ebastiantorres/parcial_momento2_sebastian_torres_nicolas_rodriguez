gastos = []


def registrar_gasto():
    print("\n--- REGISTRAR GASTO ---")

    placa = input("Ingrese la placa: ").strip().upper()
    concepto = input("Ingrese el concepto: ").strip()

    try:
        valor = float(input("Ingrese el valor: "))

        if valor <= 0:
            print("El valor debe ser mayor a 0.")
            return

    except ValueError:
        print("Debe ingresar un número válido.")
        return

    gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente.\n")


def mostrar_total_gastos():
    if not gastos:
        print("\nNo hay gastos registrados.\n")
        return

    total = 0

    for gasto in gastos:
        total += gasto["valor"]

    print(f"\nTotal acumulado: ${total:.2f}\n")


def buscar_por_placa():
    print("\n--- BUSCAR GASTOS POR PLACA ---")

    placa_buscar = input("Ingrese la placa: ").strip().upper()

    encontrados = []

    for gasto in gastos:
        if gasto["placa"] == placa_buscar:
            encontrados.append(gasto)

    if encontrados:
        for gasto in encontrados:
            print("-------------------")
            print(f"Placa: {gasto['placa']}")
            print(f"Concepto: {gasto['concepto']}")
            print(f"Valor: ${gasto['valor']:.2f}")
    else:
        print("No se encontraron gastos para esa placa.")


def editar_gasto():
    print("\n--- EDITAR GASTO ---")

    placa = input("Ingrese la placa del gasto a editar: ").strip().upper()

    for gasto in gastos:
        if gasto["placa"] == placa:

            nuevo_concepto = input("Nuevo concepto: ").strip()

            try:
                nuevo_valor = float(input("Nuevo valor: "))

                if nuevo_valor <= 0:
                    print("El valor debe ser mayor a 0.")
                    return

            except ValueError:
                print("Debe ingresar un número válido.")
                return

            gasto["concepto"] = nuevo_concepto
            gasto["valor"] = nuevo_valor

            print("Gasto actualizado correctamente.")
            return

    print("No se encontró esa placa.")


while True:
    print("\n===== CONTROL DE GASTOS =====")
    print("1. Registrar gasto")
    print("2. Mostrar total de gastos")
    print("3. Buscar por placa")
    print("4. Editar gasto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_gasto()

    elif opcion == "2":
        mostrar_total_gastos()

    elif opcion == "3":
        buscar_por_placa()

    elif opcion == "4":
        editar_gasto()

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")