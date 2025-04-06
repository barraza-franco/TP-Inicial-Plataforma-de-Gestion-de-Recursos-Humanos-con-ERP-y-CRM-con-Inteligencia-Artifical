# 🔄 Transformar empleados en variables numéricas para usar en modelos de Machine Learning
def transformar_empleados(empleados):
    import pandas as pd
    df = pd.DataFrame(empleados)  # Convertimos la lista de empleados (JSON) en un DataFrame

    # 🔁 One-hot encoding: convertimos cada valor único de 'rol' y 'tecnologia'
    # en columnas binarias (1 si lo tiene, 0 si no)
    df = pd.get_dummies(df, columns=["rol", "tecnologia"])

    # 🔢 Convertimos el seniority textual a numérico: Junior=0, Semi Senior=1, Senior=2
    df["seniority_num"] = df["seniority"].map({"Junior": 0, "Semi Senior": 1, "Senior": 2})

    # ✅ Retornamos el DataFrame completo y la versión sin la columna 'seniority' original
    return df, df.drop(columns=["seniority"])

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
