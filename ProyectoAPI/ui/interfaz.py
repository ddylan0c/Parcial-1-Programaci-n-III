# ui/interfaz.py
from tabulate import tabulate


def solicitar_datos_entrada():
    """Muestra un menú interactivo en consola para solicitar los cuatro datos requeridos:

    1. Departamento
    2. Municipio
    3. Cultivo
    4. Número de Registros a consultar
    """
    print("=" * 60)
    print("    SISTEMA DE CONSULTA DE VARIABLES EDAFICAS EN COLOMBIA")
    print("=" * 60)

    # 1. Solicitar Departamento
    departamento = input("\nIngrese el Departamento: ").strip()
    while not departamento:
        print(" Error: El departamento no puede estar vacío.")
        departamento = input("Ingrese el Departamento: ").strip()

    # 2. Solicitar Municipio
    municipio = input("Ingrese el Municipio: ").strip()
    while not municipio:
        print(" Error: El municipio no puede estar vacío.")
        municipio = input("Ingrese el Municipio: ").strip()

    # 3. Solicitar Cultivo
    cultivo = input("Ingrese el Cultivo: ").strip()
    while not cultivo:
        print(" Error: El cultivo no puede estar vacío.")
        cultivo = input("Ingrese el Cultivo: ").strip()

    # 4. Solicitar Número de Registros a consultar
    registros = None
    while registros is None:
        try:
            val = int(
                input("Ingrese el Número de Registros a consultar: ").strip()
            )
            if val > 0:
                registros = val
            else:
                print(" Error: Debe ingresar un número entero mayor a 0.")
        except ValueError:
            print(" Error: Debe ingresar un número entero válido.")

    return departamento, municipio, cultivo, registros


def mostrar_resultados(resultado):
    """Recibe un diccionario con los datos procesados y los muestra en una tabla

    por consola utilizando la librería 'tabulate'.
    """
    print("\n" + "=" * 60)
    print("                    RESULTADOS DE LA CONSULTA")
    print("=" * 60)

    if not resultado:
        print(
            "\n No se encontraron registros con los criterios ingresados."
        )
        print("Por favor, verifique el Departamento, Municipio o Cultivo.")
        print("=" * 60 + "\n")
        return

    # Definir los encabezados requeridos por la guía
    headers = [
        "Departamento",
        "Municipio",
        "Cultivo",
        "Topología",
        "Mediana pH",
        "Mediana P (Fósforo)",
        "Mediana K (Potasio)",
    ]

    # Convertir el diccionario de resultados en una fila para la tabla
    tabla_datos = [
        [
            resultado.get("Departamento"),
            resultado.get("Municipio"),
            resultado.get("Cultivo"),
            resultado.get("Topología"),
            resultado.get("Mediana pH"),
            resultado.get("Mediana Fósforo (P)"),
            resultado.get("Mediana Potasio (K)"),
        ]
    ]

    # Imprimir la tabla formateada
    print(
        "\n"
        + tabulate(
            tabla_datos, headers=headers, tablefmt="fancy_grid", stralign="center"
        )
    )
    print("=" * 60 + "\n")