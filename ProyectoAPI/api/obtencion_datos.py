from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent.parent
RUTA_EXCEL = BASE_DIR / "resultado_laboratorio_suelo.xlsx"


def consultar_variables_edaficas(
    departamento, municipio, cultivo, limite_registros
):
    """Carga los datos del archivo Excel, filtra por los criterios requeridos,

    obtiene N registros y calcula las medianas de pH, P y K.
    """
    if not RUTA_EXCEL.exists():
        return None, None

    # Carga excel en dataframe
    df = pd.read_excel(RUTA_EXCEL)

# compara la info en las columnas con lo ingresado por el usuario
    filtro = (
        (df["Departamento"].astype(str).str.upper() == departamento.upper())
        & (df["Municipio"].astype(str).str.upper() == municipio.upper())
        & (df["Cultivo"].astype(str).str.upper() == cultivo.upper())
    )

    df_filtrado = df[filtro].copy()

    
    if df_filtrado.empty:
        return None, None

    
    if limite_registros > 0:
        df_filtrado = df_filtrado.head(limite_registros)


    # calcular mediana
    val_ph = pd.to_numeric(
        df_filtrado.get("pH agua:suelo 2,5:1,0"), errors="coerce"
    )
    val_p = pd.to_numeric(
        df_filtrado.get("Fósforo (P) Bray II mg/kg"), errors="coerce"
    )
    val_k = pd.to_numeric(
        df_filtrado.get("Potasio (K) intercambiable cmol(+)/kg"), errors="coerce"
    )

    mediana_ph = val_ph.median() if not val_ph.isna().all() else None
    mediana_p = val_p.median() if not val_p.isna().all() else None
    mediana_k = val_k.median() if not val_k.isna().all() else None


    resumen_medianas = {
        "Departamento": departamento,
        "Municipio": municipio,
        "Cultivo": cultivo,
        "Mediana pH": round(mediana_ph, 2) if pd.notnull(mediana_ph) else "N/A",
        "Mediana Fósforo (P)": round(mediana_p, 2)
        if pd.notnull(mediana_p)
        else "N/A",
        "Mediana Potasio (K)": round(mediana_k, 2)
        if pd.notnull(mediana_k)
        else "N/A",
    }

    return df_filtrado, resumen_medianas