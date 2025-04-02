def visualizacion_2D_PCA(df_empleados, X):
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA
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