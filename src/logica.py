# 📦 Importamos las funciones necesarias desde nuestros módulos personalizados
from utils.file_loader import load_json_from_file                           # Carga archivos JSON con validación
from src.clustering import transformar_empleados, encontrar_mejor_k_clusters, entrenar_modelo_final
from src.recomendaciones import generar_recomendaciones
from src.exportacion import guardar_datos_csv
from src.visualizacion import visualizacion_2D_PCA
import pandas as pd

# 🚀 Esta función orquesta toda la lógica del análisis y recomendación
def ejecutar_logica(empleados):
    # 🔄 1. Transformamos los datos de entrada (empleados) a formato numérico (X) y tabular (df_empleados)
    df_empleados, X = transformar_empleados(empleados)

    # 🔢 2. Calculamos el mejor número de clusters usando Silhouette Score entre 2 y 5
    mejor_k = encontrar_mejor_k_clusters(X, range(2, 6))

    # 🤖 3. Entrenamos el modelo final con la cantidad óptima de clusters
    modelo_final = entrenar_modelo_final(X, mejor_k)

    # 🧠 4. Asignamos a cada empleado su cluster correspondiente
    df_empleados["cluster"] = modelo_final

    # 📚 5. Cargamos los cursos base y sus links desde archivos JSON externos
    cursos_base = load_json_from_file("data/cursos-base.json")
    cursos_links = load_json_from_file("data/cursos-link.json")

    # 🎯 6. Generamos recomendaciones personalizadas por empleado
    #recomendaciones = generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados)


    recomendaciones = generar_recomendaciones(df_empleados, empleados, cursos_base, cursos_links)
    recomendaciones_df = pd.DataFrame(recomendaciones)

    # 💾 7. Guardamos las recomendaciones como archivo CSV y recuperamos el nombre
    nombre_archivo = guardar_datos_csv(recomendaciones, df_empleados)

    # 📊 8. Generamos un gráfico visual 2D de los clusters usando PCA
    fig = visualizacion_2D_PCA(df_empleados, X)

    # 📤 9. Retornamos todo lo necesario para mostrarlo en la interfaz (Streamlit)
    return recomendaciones_df, df_empleados, X, mejor_k, modelo_final, nombre_archivo, fig
