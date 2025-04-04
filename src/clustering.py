# Transformar datos en variables numéricas
def transformar_empleados(empleados):
    import pandas as pd
    df = pd.DataFrame(empleados)
    #Cada valor único de rol y tecnologia se transforma en una columna con 1 o 0 según si el empleado tiene esa característica o no.
    df = pd.get_dummies(df, columns=["rol", "tecnologia"]) 
    df["seniority_num"] = df["seniority"].map({"Junior": 0, "Semi Senior": 1, "Senior": 2}) 
    return df, df.drop(columns=["seniority"])

# Encontrar mejor cantidad de clusters con Silhouette Score
def encontrar_mejor_k_clusters(X, k_range):
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_score
    import numpy as np
    scores = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=0)
        etiquetas = kmeans.fit_predict(X)
        score = silhouette_score(X, etiquetas)
        scores.append(score)
        print(f"k = {k} → Silhouette Score: {score:.4f}")
    mejor_k = k_range[np.argmax(scores)]
    print(f"\n✅ Mejor cantidad de clusters: {mejor_k}")
    return mejor_k

# Entrenar modelo final con mejor k
def entrenar_modelo_final(X, mejor_k):
    from sklearn.cluster import KMeans
    modelo_final = KMeans(n_clusters=mejor_k, random_state=0)
    etiquetas = modelo_final.fit_predict(X)
    return  etiquetas

