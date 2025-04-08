# streamlit_app.py

# 🔧 Importamos las librerías necesarias
import streamlit as st
import pandas as pd
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

# 🧠 Importamos la función central de lógica del proyecto (modularizado)
from src.logica import ejecutar_logica

# ⚙️ Configuración de la página
st.set_page_config(page_title="Clustering de Empleados", layout="centered")
st.title("🔍 Clustering de empleados y recomendación de cursos")
st.markdown("Subí un archivo `.json` con empleados para agruparlos y sugerir cursos.")

# 📥 Subida de archivo JSON
uploaded_file = st.file_uploader("📁 Subí tu archivo JSON", type="json")

if uploaded_file:
    empleados = json.load(uploaded_file)
    st.success("✅ Archivo cargado correctamente")
    st.json(empleados[:5])

    if st.button("Ejecutar análisis"):
        # Ejecutamos la lógica del sistema
        recomendaciones_df, df_empleados, X, mejor_k, modelo_final, nombre_archivo, fig = ejecutar_logica(empleados)

        # 📋 Mostramos las recomendaciones
        st.subheader("📋 Recomendaciones generadas")
        st.dataframe(recomendaciones_df)

        # 💾 Descargar CSV con recomendaciones
        st.subheader("📥 Descargar resultados")
        with open(nombre_archivo, "rb") as f:
            st.download_button(
                label="Descargar CSV",
                data=f,
                file_name=nombre_archivo,
                mime="text/csv"
            )

        # 📊 Mostrar gráfico de clusters
        st.subheader("📊 Visualización de clusters")
        st.pyplot(fig)
