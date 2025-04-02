import pandas as pd
import matplotlib.pyplot as plt
import os
import webbrowser
from datetime import datetime
from sklearn.decomposition import PCA
from utils.file_loader import load_json_from_file
from src.clustering import transformar_empleados, encontrar_mejor_k_clusters, entrenar_modelo_final
from src.recomendaciones import generar_recomendaciones

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

# 6. Recomendaciones personalizadas por cluster y empleado
recomendaciones = generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados)

# 7. Guardar recomendaciones en CSV con fecha y hora
ahora = datetime.now().strftime("%Y%m%d_%H%M")
nombre_archivo = f"data/resultados-recomendaciones/recomendaciones_empleados_{ahora}.csv"
recomendaciones_df = pd.DataFrame(recomendaciones)
recomendaciones_df.to_csv(nombre_archivo, index=False)
print(f"\n💾 Archivo '{nombre_archivo}' guardado con éxito.")

# 8. Abrir el archivo CSV en una nueva pestaña
ruta_absoluta = os.path.abspath(nombre_archivo)
webbrowser.open(f"file://{ruta_absoluta}")

# -----------------------------------------------------------------------------------
# 9. Visualización 2D con PCA

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
df_empleados["PCA1"] = X_pca[:, 0]
df_empleados["PCA2"] = X_pca[:, 1]

colores = ["red", "green", "blue", "purple", "orange"]
plt.figure(figsize=(10, 6))
for i in sorted(df_empleados["cluster"].unique()):
    grupo = df_empleados[df_empleados["cluster"] == i]
    plt.scatter(grupo["PCA1"], grupo["PCA2"], color=colores[i], label=f"Cluster {i}")

plt.title("Clusters de empleados tecnológicos (PCA 2D)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# -----------------------------------------------------------------------------------
# 10. Fin del script
print("\n✅ Script finalizado con éxito.")
