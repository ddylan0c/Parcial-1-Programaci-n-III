# main.py
from api.obtencion_datos import consultar_variables_edaficas
from ui.interfaz import mostrar_resultados, solicitar_datos_entrada


def main():
    # 1. Obtener datos de la UI
    departamento, municipio, cultivo, registros = solicitar_datos_entrada()

    # 2. Consultar registros y calcular medianas en el módulo API
    df_registros, resumen_medianas = consultar_variables_edaficas(
        departamento, municipio, cultivo, registros
    )

    # 3. Mostrar las tablas en la UI
    mostrar_resultados(df_registros, resumen_medianas)


if __name__ == "__main__":
    main()