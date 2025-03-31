import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import webbrowser
from datetime import datetime
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score

# -----------------------------------------------------------------------------------
# 1. Dataset de 50 empleados tecnologicos (solo Desarrolladores, QA, UX, Scrum Master)

empleados = [
    {"rol": "Desarrollador", "tecnologia": "Python", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "Python", "seniority": "Semi Senior"},
    {"rol": "Desarrollador", "tecnologia": "Python", "seniority": "Senior"},
    {"rol": "Desarrollador", "tecnologia": "Java", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "Java", "seniority": "Senior"},
    {"rol": "Desarrollador", "tecnologia": "Java", "seniority": "Semi Senior"},
    {"rol": "Desarrollador", "tecnologia": "JavaScript", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "JavaScript", "seniority": "Semi Senior"},
    {"rol": "Desarrollador", "tecnologia": "JavaScript", "seniority": "Senior"},
    {"rol": "QA Manual", "tecnologia": "Web", "seniority": "Junior"},
    {"rol": "QA Manual", "tecnologia": "Web", "seniority": "Semi Senior"},
    {"rol": "QA Manual", "tecnologia": "Web", "seniority": "Senior"},
    {"rol": "QA Automation", "tecnologia": "Selenium", "seniority": "Junior"},
    {"rol": "QA Automation", "tecnologia": "Selenium", "seniority": "Semi Senior"},
    {"rol": "QA Automation", "tecnologia": "Selenium", "seniority": "Senior"},
    {"rol": "QA Automation", "tecnologia": "Cypress", "seniority": "Junior"},
    {"rol": "QA Automation", "tecnologia": "Cypress", "seniority": "Semi Senior"},
    {"rol": "QA Automation", "tecnologia": "Cypress", "seniority": "Senior"},
    {"rol": "Scrum Master", "tecnologia": "Scrum", "seniority": "Junior"},
    {"rol": "Scrum Master", "tecnologia": "Scrum", "seniority": "Senior"},
    {"rol": "Scrum Master", "tecnologia": "Scrum", "seniority": "Semi Senior"},
    {"rol": "QA Manual", "tecnologia": "Mobile", "seniority": "Junior"},
    {"rol": "QA Manual", "tecnologia": "Mobile", "seniority": "Senior"},
    {"rol": "QA Automation", "tecnologia": "Python", "seniority": "Semi Senior"},
    {"rol": "QA Automation", "tecnologia": "Java", "seniority": "Junior"},
    {"rol": "QA Automation", "tecnologia": "Java", "seniority": "Semi Senior"},
    {"rol": "QA Automation", "tecnologia": "Java", "seniority": "Senior"},
    {"rol": "Desarrollador", "tecnologia": "Node.js", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "Node.js", "seniority": "Semi Senior"},
    {"rol": "Desarrollador", "tecnologia": "Node.js", "seniority": "Senior"},
    {"rol": "Desarrollador", "tecnologia": "PHP", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "PHP", "seniority": "Senior"},
    {"rol": "Desarrollador", "tecnologia": ".NET", "seniority": "Semi Senior"},
    {"rol": "Desarrollador", "tecnologia": ".NET", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": ".NET", "seniority": "Senior"},
    {"rol": "QA Automation", "tecnologia": "Cypress", "seniority": "Junior"},
    {"rol": "QA Automation", "tecnologia": "Cypress", "seniority": "Senior"},
    {"rol": "Desarrollador", "tecnologia": "SQL", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "SQL", "seniority": "Senior"},
    {"rol": "UX", "tecnologia": "UX/UI", "seniority": "Junior"},
    {"rol": "UX", "tecnologia": "UX/UI", "seniority": "Semi Senior"},
    {"rol": "UX", "tecnologia": "UX/UI", "seniority": "Senior"},
    {"rol": "UX", "tecnologia": "UX/UI", "seniority": "Junior"},
    {"rol": "UX", "tecnologia": "UX/UI", "seniority": "Senior"},
    {"rol": "UX", "tecnologia": "UX/UI", "seniority": "Semi Senior"},
    {"rol": "Desarrollador", "tecnologia": "Java", "seniority": "Junior"},
    {"rol": "Desarrollador", "tecnologia": "Python", "seniority": "Senior"},
    {"rol": "QA Manual", "tecnologia": "Mobile", "seniority": "Semi Senior"},
    {"rol": "QA Automation", "tecnologia": "Selenium", "seniority": "Semi Senior"},
    {"rol": "Scrum Master", "tecnologia": "Scrum", "seniority": "Junior"}
]

# -----------------------------------------------------------------------------------
# 2. Transformar datos en variables numéricas

def transformar_empleados(empleados):
    df = pd.DataFrame(empleados)
    #Cada valor único de rol y tecnologia se transforma en una columna con 1 o 0 según si el empleado tiene esa característica o no.
    df = pd.get_dummies(df, columns=["rol", "tecnologia"]) 
    df["seniority_num"] = df["seniority"].map({"Junior": 0, "Semi Senior": 1, "Senior": 2}) 
    return df, df.drop(columns=["seniority"])

df_empleados, X = transformar_empleados(empleados)

# -----------------------------------------------------------------------------------
# 3. Encontrar mejor cantidad de clusters con Silhouette Score

scores = []
k_range = range(2, 6)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=0)
    etiquetas = kmeans.fit_predict(X)
    score = silhouette_score(X, etiquetas)
    scores.append(score)
    print(f"k = {k} → Silhouette Score: {score:.4f}")

mejor_k = k_range[np.argmax(scores)]
print(f"\n✅ Mejor cantidad de clusters: {mejor_k}")

# -----------------------------------------------------------------------------------
# 4. Entrenar modelo final con mejor k

modelo_final = KMeans(n_clusters=mejor_k, random_state=0)
df_empleados["cluster"] = modelo_final.fit_predict(X) 

# -----------------------------------------------------------------------------------
# 5. Cursos base por tecnología y nivel de seniority

cursos_base = {
    "Python": ["Python Intermedio", "Python Avanzado", "Machine Learning con Python"],
    "Java": ["Java Intermedio", "Java Avanzado", "Spring Boot"],
    "JavaScript": ["JS Intermedio", "JS Avanzado", "React"],
    "Cypress": ["Cypress Intermedio", "Cypress Avanzado", "Test Automation Frameworks"],
    "Selenium": ["Selenium Intermedio", "Selenium Avanzado", "Automatización con Python"],
    "Scrum": ["Scrum Intermedio", "Scrum Avanzado", "Gestión Ágil de Proyectos"],
    "PHP": ["PHP Intermedio", "PHP Avanzado", "Laravel"],
    ".NET": [".NET Intermedio", ".NET Avanzado", "Microservicios con .NET"],
    "SQL": ["SQL Intermedio", "SQL Avanzado", "Optimización de Consultas"],
    "Node.js": ["Node Intermedio", "Node Avanzado", "APIs con Express"],
    "UX/UI": ["UX/UI Intermedio", "UX Research", "Design Systems Avanzado"],
    "Web": ["Testing Web Intermedio", "Testing Web Avanzado", "Usabilidad Web"],
    "Mobile": ["Testing Mobile Intermedio", "Testing Mobile Avanzado", "Automatización Mobile"]
}

cursos_links = {
    "Python Intermedio": "https://udeUngs.com/python-intermedio",
    "Python Avanzado": "https://udeUngs.com/python-avanzado",
    "Machine Learning con Python": "https://udeUngs.com/ml-python",
    "Java Intermedio": "https://udeUngs.com/java-intermedio",
    "Java Avanzado": "https://udeUngs.com/java-avanzado",
    "Spring Boot": "https://udeUngs.com/spring-boot",
    "UX/UI Intermedio": "https://udeUngs.com/uxui-intermedio",
    "UX Research": "https://udeUngs.com/ux-research",
    "Design Systems Avanzado": "https://udeUngs.com/design-systems",
}

# -----------------------------------------------------------------------------------
# 6. Recomendaciones personalizadas por cluster y empleado

recomendaciones = []

for index_cluster, row in df_empleados.iterrows():
    cluster = row["cluster"]
    seniority = empleados[index_cluster]["seniority"]
    tecnologia = empleados[index_cluster]["tecnologia"]
    rol = empleados[index_cluster]["rol"]

    if tecnologia not in cursos_base:
        curso = "Curso no disponible"
        link = "-"
    else:
        if seniority == "Junior":
            curso = cursos_base[tecnologia][0]
        elif seniority == "Semi Senior":
            curso = cursos_base[tecnologia][1]
        else:
            curso = cursos_base[tecnologia][2]
        link = cursos_links.get(curso, "https://udeUngs.com/no-curso")

    recomendaciones.append({
        "rol": rol,
        "tecnologia": tecnologia,
        "seniority": seniority,
        "cluster": cluster,
        "curso_recomendado": curso,
        "link": link
    })

# 7. Guardar recomendaciones en CSV con fecha y hora
ahora = datetime.now().strftime("%Y%m%d_%H%M")
nombre_archivo = f"data/resultados-recomendaciones/recomendaciones_empleados_{ahora}.csv"
recomendaciones_df = pd.DataFrame(recomendaciones)
recomendaciones_df.to_csv(nombre_archivo, index=False)
print(f"\n💾 Archivo '{nombre_archivo}' guardado con éxito.")

# 8. Abrir el archivo CSV en una nueva pestaña
ruta_absoluta = os.path.abspath(nombre_archivo)
webbrowser.open(f"file://{ruta_absoluta}")

# -----------------------------------------------------------------------------------
# 9. Visualización 2D con PCA

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

# -----------------------------------------------------------------------------------
# 10. Fin del script
print("\n✅ Script finalizado con éxito.")
