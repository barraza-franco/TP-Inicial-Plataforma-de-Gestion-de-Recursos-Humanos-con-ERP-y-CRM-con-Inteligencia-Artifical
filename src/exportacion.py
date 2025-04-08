def guardar_datos_csv(recomendaciones, df_empleados):
    """
    Guarda un archivo CSV combinando:
    - Las recomendaciones por empleado
    - El cluster asignado
    - Y todas las habilidades con sus niveles (para referencia)
    """
    import pandas as pd
    from datetime import datetime
    import os

    ahora = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_archivo = f"data/resultados-recomendaciones/recomendaciones_empleados_{ahora}.csv"
    os.makedirs("data/resultados-recomendaciones", exist_ok=True)

    # Convertimos recomendaciones a DataFrame
    df_recomendaciones = pd.DataFrame(recomendaciones)

    # Filtramos solo columnas de habilidades (float entre 0 y 1)
    columnas_habilidad = df_empleados.select_dtypes(include=["float", "int"]).columns
    columnas_habilidad = [col for col in columnas_habilidad if col not in ["PCA1", "PCA2", "cluster"]]

    # Tomamos solo las columnas de habilidades
    df_habilidades = df_empleados[columnas_habilidad].reset_index(drop=True)

    # Combinamos ambos
    df_final = pd.concat([df_recomendaciones.reset_index(drop=True), df_habilidades], axis=1)

    # Guardamos a CSV
    df_final.to_csv(nombre_archivo, index=False)
    print(f"💾 Archivo guardado: {nombre_archivo}")

    return nombre_archivo
