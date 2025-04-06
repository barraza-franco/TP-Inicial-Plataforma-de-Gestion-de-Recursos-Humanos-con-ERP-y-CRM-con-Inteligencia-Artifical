def visualizacion_2D_PCA(df_empleados, X):
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA

    # 🎯 Reducimos la dimensionalidad de los datos a 2 componentes principales usando PCA
    # Esto nos permite graficar los datos en un plano 2D
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    # Agregamos las dos componentes principales como nuevas columnas al DataFrame
    df_empleados["PCA1"] = X_pca[:, 0]
    df_empleados["PCA2"] = X_pca[:, 1]

    # 📊 Creamos la figura y los ejes para el gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    colores = ["red", "green", "blue", "purple", "orange"]  # Colores para cada cluster

    # 🔄 Iteramos por cada cluster para graficar los puntos correspondientes
    for i in sorted(df_empleados["cluster"].unique()):
        grupo = df_empleados[df_empleados["cluster"] == i]
        ax.scatter(
            grupo["PCA1"], grupo["PCA2"],
            color=colores[i % len(colores)],
            label=f"Cluster {i}"
        )

    # 🏷️ Personalizamos el gráfico con título, etiquetas y leyenda
    ax.set_title("Clusters de empleados tecnológicos (PCA 2D)")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()

    # 🔁 Retornamos el gráfico para poder mostrarlo con st.pyplot(fig)
    return fig
