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