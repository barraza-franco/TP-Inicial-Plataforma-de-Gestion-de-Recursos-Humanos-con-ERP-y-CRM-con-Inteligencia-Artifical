def generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados):
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

    return recomendaciones
