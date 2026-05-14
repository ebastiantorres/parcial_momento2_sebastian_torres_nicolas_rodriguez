
gastos = []


def registrar_gasto():
    print("\n--- REGISTRAR GASTO ---")

    placa = input("Ingrese la placa: ")
    concepto = input("Ingrese el concepto: ")
    valor = float(input("Ingrese el valor: "))

    gasto = {
        "placa": placa,
        "concepto": concepto,
        "valor": valor
    }

    gastos.append(gasto)

    print("Gasto registrado correctamente.\n")


def mostrar_total_gastos():
    total = 0

    for gasto in gastos:
        total += gasto["valor"]

    print(f"\nTotal acumulado: ${total}\n")


def buscar_por_placa():
    print("\n--- BUSCAR GASTOS POR PLACA ---")

    placa_buscar = input("Ingrese la placa: ")

    encontrado = False

    for gasto in gastos:
        if gasto["placa"] == placa_buscar:
            print("-------------------")
            print(f"Placa: {gasto['placa']}")
            print(f"Concepto: {gasto['concepto']}")
            print(f"Valor: ${gasto['valor']}")
            encontrado = True

    if not encontrado:
        print("No se encontraron gastos para esa placa.")


while True:
    print("\n===== CONTROL DE GASTOS =====")
    print("1. Registrar gasto")
    print("2. Mostrar total de gastos")
    print("3. Buscar por placa")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_gasto()

    elif opcion == "2":
        mostrar_total_gastos()

    elif opcion == "3":
        buscar_por_placa()

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")
