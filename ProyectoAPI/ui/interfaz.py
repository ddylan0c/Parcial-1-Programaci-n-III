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
    print(
        "\n(Asegúrese de ingresar los datos correctamente, con acentos y sin errores tipográficos.)\n"
    )

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


def mostrar_resultados(df_registros, resumen_medianas):
    """Muestra primero la tabla con los N registros individuales

    y posteriormente la tabla con las medianas de las variables edáficas.
    """
    print("\n" + "=" * 70)
    print("                    RESULTADOS DE LA CONSULTA")
    print("=" * 70)

    if df_registros is None or df_registros.empty:
        print(
            "\n No se encontraron registros con los criterios ingresados."
        )
        print("Por favor, verifique el Departamento, Municipio o Cultivo.")
        print("=" * 70 + "\n")
        return

    # --- TABLA 1: REGISTROS OBTENIDOS ---
    print(f"\n REGISTROS CONSULTADOS ({len(df_registros)}):")

    col_topo = (
        "Topografia" if "Topografia" in df_registros.columns else "Topología"
    )

    tabla_registros = []
    for idx, fila in df_registros.reset_index(drop=True).iterrows():
        tabla_registros.append([
            idx + 1,
            fila.get("Departamento", "N/A"),
            fila.get("Municipio", "N/A"),
            fila.get("Cultivo", "N/A"),
            fila.get(col_topo, "N/A"),
            fila.get("pH agua:suelo 2,5:1,0", "N/A"),
            fila.get("Fósforo (P) Bray II mg/kg", "N/A"),
            fila.get("Potasio (K) intercambiable cmol(+)/kg", "N/A"),
        ])

    headers_registros = [
        "#",
        "Departamento",
        "Municipio",
        "Cultivo",
        "Topología",
        "pH",
        "Fósforo (P)",
        "Potasio (K)",
    ]

    print(
        tabulate(
            tabla_registros,
            headers=headers_registros,
            tablefmt="fancy_grid",
            stralign="center",
        )
    )

    # --- TABLA 2: MEDIANAS CALCULADAS ---
    print("\n MEDIANAS CALCULADAS DE LAS VARIABLES EDÁFICAS:")

    tabla_medianas = [[
        resumen_medianas.get("Departamento"),
        resumen_medianas.get("Municipio"),
        resumen_medianas.get("Cultivo"),
        resumen_medianas.get("Topología"),
        resumen_medianas.get("Mediana pH"),
        resumen_medianas.get("Mediana Fósforo (P)"),
        resumen_medianas.get("Mediana Potasio (K)"),
    ]]

    headers_medianas = [
        "Departamento",
        "Municipio",
        "Cultivo",
        "Topología",
        "Mediana pH",
        "Mediana P",
        "Mediana K",
    ]

    print(
        tabulate(
            tabla_medianas,
            headers=headers_medianas,
            tablefmt="fancy_grid",
            stralign="center",
        )
    )
    print("=" * 70 + "\n")