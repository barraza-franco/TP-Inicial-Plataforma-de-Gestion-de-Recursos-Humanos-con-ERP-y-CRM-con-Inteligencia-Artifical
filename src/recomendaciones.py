def generar_recomendaciones(df_empleados, empleados, cursos_base, cursos_links):
    """
    Recomienda un curso basado en la mejor habilidad del empleado.
    """
    recomendaciones = []

    columnas_habilidades = df_empleados.select_dtypes(include=["float", "int"]).columns
    columnas_habilidades = [c for c in columnas_habilidades if c not in ["PCA1", "PCA2", "cluster", "seniority_num"]]

    for i, row in df_empleados.iterrows():
        # Detectar su mejor habilidad
        habilidad_top = row[columnas_habilidades].sort_values(ascending=False).index[0]
        seniority = empleados[i]["seniority"]

        # Seleccionar curso según seniority
        if habilidad_top in cursos_base:
            if seniority == "Junior":
                curso = cursos_base[habilidad_top][0]
            elif seniority == "Semi Senior":
                curso = cursos_base[habilidad_top][1] if len(cursos_base[habilidad_top]) > 1 else cursos_base[habilidad_top][0]
            else:
                curso = cursos_base[habilidad_top][-1]
            link = cursos_links.get(curso, "-")
        else:
            curso = "Sin curso disponible"
            link = "-"
        
        recomendaciones.append({
            "rol": empleados[i]["rol"],
            "tecnologia": empleados[i]["tecnologia"],
            "seniority": seniority,
            "cluster": row["cluster"],
            "habilidad_destacada": habilidad_top,
            "curso_recomendado": curso,
            "link": link
        })

    return recomendaciones
