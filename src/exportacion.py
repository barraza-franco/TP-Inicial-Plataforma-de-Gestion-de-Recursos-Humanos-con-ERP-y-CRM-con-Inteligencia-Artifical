def guardar_datos_csv(recomendaciones):
    from datetime import datetime
    import pandas as pd
    ahora = datetime.now().strftime("%Y%m%d_%H%M")
    nombre_archivo = f"data/resultados-recomendaciones/recomendaciones_empleados_{ahora}.csv"
    recomendaciones_df = pd.DataFrame(recomendaciones)
    recomendaciones_df.to_csv(nombre_archivo, index=False)
    print(f"\n💾 Archivo '{nombre_archivo}' guardado con éxito.")
    return nombre_archivo

