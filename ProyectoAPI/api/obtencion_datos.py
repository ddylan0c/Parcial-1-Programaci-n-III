from pathlib import Path
import pandas as pd

# Definir la ruta del archivo asegurando que lo encuentre desde la raíz
BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_EXCEL = BASE_DIR / "resultado_laboratorio_suelo.xlsx"


def consultar_variables_edaficas(
    departamento, municipio, cultivo, limite_registros
):
    """Carga los datos del archivo Excel, filtra por los criterios requeridos

    y calcula las medianas de pH, Fósforo (P) y Potasio (K).
    """
    # 1. Cargar el archivo de Excel
    df = pd.read_excel(RUTA_EXCEL)

    # Nota: Asegúrate de ajustar los nombres exactos de las columnas según tu Excel
    # Por ejemplo: 'Departamento', 'Municipio', 'Cultivo', 'Topologia', 'pH', 'Fosforo (P)', 'Potasio (K)'

    # 2. Filtrar por departamento, municipio y cultivo (sin importar mayúsculas/minúsculas)
    filtro = (
        (df["Departamento"].astype(str).str.upper() == departamento.upper())
        & (df["Municipio"].astype(str).str.upper() == municipio.upper())
        & (df["Cultivo"].astype(str).str.upper() == cultivo.upper())
    )

    df_filtrado = df[filtro]

    # 3. Limitar la cantidad de registros según lo solicitado por el usuario
    if limite_registros > 0:
        df_filtrado = df_filtrado.head(limite_registros)

    # 4. Verificar si se encontraron registros
    if df_filtrado.empty:
        return None

    # 5. Obtener la topología (primer valor encontrado en los registros filtrados)
    topologia = (
        df_filtrado["Topografia"].iloc[0]
        if "Topografia" in df_filtrado.columns
        else "N/A"
    )

    # 6. Calcular la mediana de las variables edáficas solicitadas (pH, P, K)
    # Convertir a numérico por si vienen valores en texto/string
    mediana_ph = pd.to_numeric(df_filtrado["pH agua:suelo 2,5:1,0"], errors="coerce").median()
    mediana_p = pd.to_numeric(
        df_filtrado["Fósforo (P) Bray II mg/kg"], errors="coerce"
    ).median()  # Cambia por la columna exacta del Excel
    mediana_k = pd.to_numeric(
        df_filtrado["Potasio (K) intercambiable cmol(+)/kg"], errors="coerce"
    ).median()  # Cambia por la columna exacta del Excel

    # 7. Retornar el resultado estructurado
    resultado = {
        "Departamento": departamento,
        "Municipio": municipio,
        "Cultivo": cultivo,
        "Topología": topologia,
        "Mediana pH": round(mediana_ph, 2)
        if pd.notnull(mediana_ph)
        else "N/A",
        "Mediana Fósforo (P)": round(mediana_p, 2)
        if pd.notnull(mediana_p)
        else "N/A",
        "Mediana Potasio (K)": round(mediana_k, 2)
        if pd.notnull(mediana_k)
        else "N/A",
    }

    return resultado