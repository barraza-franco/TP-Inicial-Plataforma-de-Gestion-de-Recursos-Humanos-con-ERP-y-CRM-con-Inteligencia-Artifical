def transformar_empleados(empleados):
    """
    Transforma empleados usando solo sus habilidades como base para clustering.

    Returns:
        df_empleados: DataFrame completo (con rol, seniority, etc. para visualización)
        X: DataFrame con solo columnas de habilidades (float) para entrenar el modelo
    """
    import pandas as pd

    # Cargar en DataFrame
    df = pd.DataFrame(empleados)

    # Guardar columnas originales útiles para visualización
    df["rol_original"] = df["rol"]
    df["tecnologia_original"] = df["tecnologia"]

    # Expandimos las habilidades como columnas (con valores float)
    habilidades_df = df["habilidades"].apply(pd.Series).fillna(0)

    # Reemplazamos el DataFrame de entrada
    df = pd.concat([df.drop(columns=["habilidades"]), habilidades_df], axis=1)

    # Solo usamos las habilidades como X para clustering
    columnas_habilidades = habilidades_df.columns.tolist()
    X = df[columnas_habilidades]

    return df, X



# 🔍 Busca el mejor número de clusters evaluando diferentes valores de k con Silhouette Score
def encontrar_mejor_k_clusters(X, k_range):
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    import numpy as np

    scores = []  # Almacenamos el score de cada valor de k

    # 🔄 Probamos diferentes cantidades de clusters
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=0)
        etiquetas = kmeans.fit_predict(X)
        score = silhouette_score(X, etiquetas)  # Cuanto más alto, mejor
        scores.append(score)
        print(f"k = {k} → Silhouette Score: {score:.4f}")

    # 🏆 Elegimos el k con mejor puntuación
    mejor_k = k_range[np.argmax(scores)]
    print(f"\n✅ Mejor cantidad de clusters: {mejor_k}")

    return mejor_k

# 🧠 Entrena un modelo KMeans con la mejor cantidad de clusters encontrada
def entrenar_modelo_final(X, mejor_k):
    from sklearn.cluster import KMeans
    modelo_final = KMeans(n_clusters=mejor_k, random_state=0)

    # Entrenamos el modelo y obtenemos las etiquetas de cluster
    etiquetas = modelo_final.fit_predict(X)

    # 🔁 Devolvemos las etiquetas (número de cluster asignado a cada fila)
    return etiquetas
