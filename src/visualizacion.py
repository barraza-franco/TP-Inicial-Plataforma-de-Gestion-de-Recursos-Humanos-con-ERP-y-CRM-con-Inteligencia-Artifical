def visualizacion_2D_PCA(df_empleados, X):
    import matplotlib.pyplot as plt
    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)

    df_empleados["PCA1"] = X_pca[:, 0]
    df_empleados["PCA2"] = X_pca[:, 1]

    fig, ax = plt.subplots(figsize=(10, 6))
    colores = ["red", "green", "blue", "purple", "orange", "cyan", "brown"]

    for i in sorted(df_empleados["cluster"].unique()):
        grupo = df_empleados[df_empleados["cluster"] == i]
        ax.scatter(
            grupo["PCA1"],
            grupo["PCA2"],
            color=colores[i % len(colores)],
            label=f"Cluster {i}",
            alpha=0.7
        )
        for _, row in grupo.iterrows():
            etiqueta = f"{row['rol_original']} ({row['seniority']})"
            ax.text(row["PCA1"] + 0.02, row["PCA2"] + 0.02, etiqueta, fontsize=7)

    ax.set_title("Clusters por nivel de habilidades")
    ax.set_xlabel("PCA 1")
    ax.set_ylabel("PCA 2")
    ax.legend()
    ax.grid(True)
    fig.tight_layout()
    return fig
