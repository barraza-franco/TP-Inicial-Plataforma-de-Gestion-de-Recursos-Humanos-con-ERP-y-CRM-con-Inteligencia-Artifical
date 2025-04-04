from utils.file_loader import load_json_from_file
from src.clustering import transformar_empleados, encontrar_mejor_k_clusters, entrenar_modelo_final
from src.recomendaciones import generar_recomendaciones
from src.exportacion import guardar_datos_csv
from src.visualizacion import visualizacion_2D_PCA
import pandas as pd



def ejecutar_logica(empleados):
    df_empleados, X = transformar_empleados(empleados)
    mejor_k = encontrar_mejor_k_clusters(X, range(2, 6))


     
    modelo_final = entrenar_modelo_final(X, mejor_k)

    df_empleados["cluster"] = modelo_final

    
    cursos_base = load_json_from_file("data/cursos-base.json")
    cursos_links = load_json_from_file("data/cursos-link.json")
    recomendaciones = generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados)
    recomendaciones_df = pd.DataFrame(recomendaciones)

    nombre_archivo = guardar_datos_csv(recomendaciones)

    fig = visualizacion_2D_PCA(df_empleados, X)

    return recomendaciones_df, df_empleados, X, mejor_k, modelo_final, nombre_archivo, fig