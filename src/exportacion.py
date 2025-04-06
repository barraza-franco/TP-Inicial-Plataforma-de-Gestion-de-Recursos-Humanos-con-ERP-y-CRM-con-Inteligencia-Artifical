def guardar_datos_csv(recomendaciones):
    from datetime import datetime   # ⏰ Para generar nombres únicos usando fecha y hora
    import pandas as pd             # 📦 Para convertir datos a DataFrame y guardarlos como CSV

    # 🔢 Obtenemos el timestamp actual para usarlo en el nombre del archivo
    ahora = datetime.now().strftime("%Y%m%d_%H%M")

    # 📝 Definimos la ruta y el nombre del archivo de salida
    nombre_archivo = f"data/resultados-recomendaciones/recomendaciones_empleados_{ahora}.csv"

    # 🧱 Convertimos la lista de recomendaciones (diccionarios) a un DataFrame
    recomendaciones_df = pd.DataFrame(recomendaciones)

    # 💾 Guardamos el DataFrame como archivo CSV, sin incluir el índice de pandas
    recomendaciones_df.to_csv(nombre_archivo, index=False)

    # ✅ Imprimimos confirmación en consola
    print(f"\n💾 Archivo '{nombre_archivo}' guardado con éxito.")

    # 🔁 Retornamos la ruta al archivo para poder usarlo desde la interfaz
    return nombre_archivo
