# streamlit_app.py

# 🔧 Importamos las librerías necesarias
import streamlit as st                         # Para construir la interfaz web
import pandas as pd                            # Para manipular DataFrames
import json                                    # Para trabajar con archivos JSON
import matplotlib.pyplot as plt                # Para generar gráficos
import numpy as np                             # (opcional, si se necesita para operaciones numéricas)
from datetime import datetime                  # Para generar nombres con fecha/hora
import os                                      # Para trabajar con rutas de archivos

# 🧠 Importamos la función central de lógica del proyecto (modularizado)
from src.logica import ejecutar_logica

# ⚙️ Configuramos la interfaz principal de Streamlit
st.set_page_config(page_title="Clustering de Empleados", layout="centered")
st.title("🔍 Clustering de empleados y recomendación de cursos")
st.markdown("Subí un archivo `.json` con empleados para agruparlos y sugerir cursos.")

# 📥 Componente para cargar un archivo JSON desde la interfaz
uploaded_file = st.file_uploader("📁 Subí tu archivo JSON", type="json")

# Si se sube un archivo:
if uploaded_file:
    empleados = json.load(uploaded_file)           # Leemos el archivo JSON
    st.success("✅ Archivo cargado correctamente")
    st.json(empleados[:5])                         # Mostramos los primeros 5 empleados cargados

    # Botón que ejecuta el análisis completo
    if st.button("Ejecutar análisis"):

        # Ejecutamos toda la lógica desde una función centralizada (modular)
        recomendaciones_df, df_empleados, X, mejor_k, modelo_final, nombre_archivo, fig = ejecutar_logica(empleados)

        # 📋 Mostramos la tabla con las recomendaciones generadas
        st.subheader("📋 Recomendaciones generadas")
        st.dataframe(recomendaciones_df)
        
        # 💾 Permitimos descargar el archivo CSV generado
        with open(nombre_archivo, "rb") as f:
            st.download_button("📥 Descargar CSV", f, file_name=nombre_archivo)

        # 📊 Mostramos el gráfico 2D de clusters (PCA)
        st.subheader("📊 Visualización de clusters")
        st.pyplot(fig)
