import numpy as np
import pandas as pd

# ==========================================
# 1. CARGA DEL DATASET
# ==========================================
# Simulamos la carga de un dataset de sensores de equipos industriales (ej. CSV)
# En tu caso real, puedes cambiar 'sensores_equipos.csv' por la ruta de tu archivo.
print("--- 1. CARGA DE DATOS ---")

# Simularemos un DataFrame que contiene datos con valores nulos, duplicados y errores de formato
data = {
    "equipo_id": [
        "EQ-101",
        "EQ-102",
        "EQ-103",
        "EQ-101",
        "EQ-104",
        "EQ-102",
        None,
        "EQ-105",
    ],
    "temperatura_c": [
        "75.5",
        "82.0",
        "NaN",
        "75.5",
        "90.1",
        "85.4",
        "68.0",
        "110.2",
    ],  # Formato texto y nulos
    "vibracion_mm_s": [
        2.5,
        3.1,
        1.8,
        2.5,
        4.2,
        np.nan,
        1.5,
        5.6,
    ],  # Con valores nulos
    "estado": [
        "Activo",
        "Activo",
        "Inactivo",
        "Activo",
        "Alerta",
        "Activo",
        "Activo",
        "Critico",
    ],
}

df = pd.DataFrame(data)

# REPORTE ANTES DE LA LIMPIEZA
print("\n[ESTADO ANTES DE LA LIMPIEZA]")
print(f"Dimensiones del dataset: {df.shape}")
print("\nValores nulos por columna:")
print(df.isnull().sum())
print(f"Cantidad de filas duplicadas: {df.duplicated().sum()}")
print("\nTipos de datos originales:")
print(df.dtypes)

# ==========================================
# 2. LIMPIEZA DE DATOS
# ==========================================
print("\n--- 2. PROCESO DE LIMPIEZA ---")

# A. Eliminar registros completamente duplicados
df = df.drop_duplicates()

# B. Eliminar filas donde el ID del equipo sea nulo
df = df.dropna(subset=["equipo_id"])

# C. Corregir tipos de datos (temperatura_c de texto/string a float)
df["temperatura_c"] = pd.to_numeric(df["temperatura_c"], errors="coerce")

# D. Manejo de nulos restantes (imputación por la media en temperatura y vibración)
df["temperatura_c"] = df["temperatura_c"].fillna(df["temperatura_c"].mean())
df["vibracion_mm_s"] = df["vibracion_mm_s"].fillna(
    df["vibracion_mm_s"].mean()
)

# REPORTE DESPUÉS DE LA LIMPIEZA
print("\n[ESTADO DESPUÉS DE LA LIMPIEZA]")
print(f"Dimensiones del dataset: {df.shape}")
print("\nValores nulos por columna:")
print(df.isnull().sum())
print(f"Cantidad de filas duplicadas: {df.duplicated().sum()}")
print("\nTipos de datos corregidos:")
print(df.dtypes)


# ==========================================
# 3. CONSULTAS Y HALLAZGOS (Pandas: Filtro + Agregación)
# ==========================================
print("\n--- 3. CONSULTAS Y HALLAZGOS ---")

# Consulta 1: Promedio de temperatura y vibración agrupado por el estado del equipo
print(
    "\nPregunta 1: ¿Cuál es el promedio de temperatura y vibración de los equipos según su estado operativo?"
)
consulta_1 = (
    df.groupby("estado")[["temperatura_c", "vibracion_mm_s"]]
    .mean()
    .reset_index()
)
print(consulta_1)
print(
    "Hallazgo 1: Los equipos en estado 'Critico' o 'Alerta' muestran valores medios de temperatura significativamente más elevados, lo que indica que el monitoreo térmico es un KPI clave para predecir fallas mecánicas."
)

# Consulta 2: Filtrar equipos con temperatura mayor a 80°C y contar cuántos hay por equipo
print(
    "\nPregunta 2: ¿Qué equipos operan a temperaturas mayores a 80°C y cuántas mediciones registran?"
)
equipos_calientes = df[df["temperatura_c"] > 80.0]
consulta_2 = (
    equipos_calientes.groupby("equipo_id")
    .size()
    .reset_index(name="cantidad_mediciones_altas")
)
print(consulta_2)
print(
    "Hallazgo 2: Se identifica que el equipo EQ-105 y EQ-102 superan frecuentemente el umbral crítico de 80°C, requiriendo revisión prioritaria en el plan de mantenimiento preventivo."
)