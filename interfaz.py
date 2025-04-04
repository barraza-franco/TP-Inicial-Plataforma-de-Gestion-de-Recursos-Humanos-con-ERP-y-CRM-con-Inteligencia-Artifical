# streamlit_app.py
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

from utils.file_loader import load_json_from_file
from src.clustering import transformar_empleados, encontrar_mejor_k_clusters, entrenar_modelo_final
from src.recomendaciones import generar_recomendaciones
from src.exportacion import guardar_datos_csv
from src.visualizacion import visualizacion_2D_PCA

st.set_page_config(page_title="Clustering de Empleados", layout="centered")
st.title("🔍 Clustering de empleados y recomendación de cursos")
st.markdown("Subí un archivo `.json` con empleados para agruparlos y sugerir cursos.")

uploaded_file = st.file_uploader("📁 Subí tu archivo JSON", type="json")

if uploaded_file:
    empleados = json.load(uploaded_file)
    st.success("✅ Archivo cargado correctamente")
    st.json(empleados[:5])

    if st.button("Ejecutar análisis"):
        df_empleados, X = transformar_empleados(empleados)

        mejor_k = encontrar_mejor_k_clusters(X, range(2, 6))
        st.info(f"🔢 Mejor cantidad de clusters: {mejor_k}")

        modelo_final, etiquetas = entrenar_modelo_final(X, mejor_k)
        df_empleados["cluster"] = etiquetas



        cursos_base = load_json_from_file("data/cursos-base.json")
        cursos_links = load_json_from_file("data/cursos-link.json")
        recomendaciones = generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados)
        recomendaciones_df = pd.DataFrame(recomendaciones)
        st.subheader("📋 Recomendaciones generadas")
        st.dataframe(recomendaciones_df)

        # Descargar CSV
        nombre_archivo = f"recomendaciones_empleados_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        recomendaciones_df.to_csv(nombre_archivo, index=False)
        with open(nombre_archivo, "rb") as f:
            st.download_button("📥 Descargar CSV", f, file_name=nombre_archivo)

        # Visualización de clusters
        st.subheader("📊 Visualización de clusters")
        fig = visualizacion_2D_PCA(df_empleados, X)
        st.pyplot(fig)
