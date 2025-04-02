import os
import webbrowser
from utils.file_loader import load_json_from_file
from src.clustering import transformar_empleados, encontrar_mejor_k_clusters, entrenar_modelo_final
from src.recomendaciones import generar_recomendaciones
from src.exportacion import guardar_datos_csv
from src.visualizacion import visualizacion_2D_PCA

# -----------------------------------------------------------------------------------
# 1. Carga inicial de datos
empleados = load_json_from_file("data/empleados.json")
cursos_base = load_json_from_file("data/cursos-base.json")
cursos_links = load_json_from_file("data/cursos-link.json")

# -----------------------------------------------------------------------------------
# 2. Transformar datos en variables numéricas
df_empleados, X = transformar_empleados(empleados)

# -----------------------------------------------------------------------------------
# 3. Encontrar mejor cantidad de clusters con Silhouette Score
mejor_k = encontrar_mejor_k_clusters(X, range(2, 6))

# -----------------------------------------------------------------------------------
# 4. Entrenar modelo final con mejor k
modelo_final, df_empleados["cluster"] = entrenar_modelo_final(X, mejor_k)

# -----------------------------------------------------------------------------------
# 5. Recomendaciones personalizadas por cluster y empleado
recomendaciones = generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados)

# -----------------------------------------------------------------------------------
# 6. Guardar recomendaciones en CSV con fecha y hora
archivo_recomendaciones = guardar_datos_csv(recomendaciones)

# -----------------------------------------------------------------------------------
# 7. Abrir el archivo CSV en una nueva pestaña
ruta_absoluta = os.path.abspath(archivo_recomendaciones)
webbrowser.open(f"file://{ruta_absoluta}")

# -----------------------------------------------------------------------------------
# 8. Visualización 2D de los clusters con PCA
visualizacion_2D_PCA(df_empleados, X)

# -----------------------------------------------------------------------------------
# 9. Fin del script
print("\n✅ Script finalizado con éxito.")
