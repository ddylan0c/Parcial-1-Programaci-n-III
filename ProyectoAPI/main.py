# main.py
from api.obtencion_datos import consultar_variables_edaficas
from ui.interfaz import mostrar_resultados, solicitar_datos_entrada


def main():
    # 1. Obtener datos de la UI
    departamento, municipio, cultivo, registros = solicitar_datos_entrada()

    # 2. Consultar y procesar en el módulo de API
    resultado = consultar_variables_edaficas(
        departamento, municipio, cultivo, registros
    )

    # 3. Mostrar el resultado en la UI
    mostrar_resultados(resultado)


if __name__ == "__main__":
    main()