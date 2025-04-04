def visualizacion_2D_PCA(df_empleados, X):
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA

    # Reducimos a 2 dimensiones para graficar
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    df_empleados["PCA1"] = X_pca[:, 0]
    df_empleados["PCA2"] = X_pca[:, 1]

    # Creamos la figura y los ejes
    fig, ax = plt.subplots(figsize=(10, 6))
    colores = ["red", "green", "blue", "purple", "orange"]

    for i in sorted(df_empleados["cluster"].unique()):
        grupo = df_empleados[df_empleados["cluster"] == i]
        ax.scatter(grupo["PCA1"], grupo["PCA2"], color=colores[i % len(colores)], label=f"Cluster {i}")

    ax.set_title("Clusters de empleados tecnológicos (PCA 2D)")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    return fig  # ✅ Esto permite usarlo con st.pyplot(fig)
