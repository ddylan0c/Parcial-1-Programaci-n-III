from api.obtencion_datos import consultar_variables_edaficas
from ui.interfaz import mostrar_resultados, solicitar_datos_entrada


def main():
    departamento, municipio, cultivo, registros = solicitar_datos_entrada()

    df_registros, resumen_medianas = consultar_variables_edaficas(
        departamento, municipio, cultivo, registros
    )

    mostrar_resultados(df_registros, resumen_medianas)


if __name__ == "__main__":
    main()