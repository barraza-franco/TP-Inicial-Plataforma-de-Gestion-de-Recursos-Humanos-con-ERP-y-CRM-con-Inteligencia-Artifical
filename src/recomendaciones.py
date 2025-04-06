def generar_recomendaciones(empleados, cursos_base, cursos_links, df_empleados):
    recomendaciones = []  # Lista que va a almacenar todas las recomendaciones generadas

    # 🔁 Recorremos cada fila del DataFrame de empleados con su cluster asignado
    for index_cluster, row in df_empleados.iterrows():
        # Obtenemos el número de cluster del empleado actual
        cluster = row["cluster"]

        # Accedemos al JSON original para obtener seniority, tecnología y rol
        seniority = empleados[index_cluster]["seniority"]
        tecnologia = empleados[index_cluster]["tecnologia"]
        rol = empleados[index_cluster]["rol"]

        # 📚 Verificamos si hay cursos disponibles para esa tecnología
        if tecnologia not in cursos_base:
            # Si no hay cursos, generamos un mensaje personalizado
            curso = "No tenemos cursos disponibles para: " + rol + " " + tecnologia
            link = "-"
        else:
            # Si hay cursos, los asignamos según el seniority del empleado
            if seniority == "Junior":
                curso = cursos_base[tecnologia][0]  # Curso nivel intermedio
            elif seniority == "Semi Senior":
                curso = cursos_base[tecnologia][1]  # Curso nivel avanzado
            else:
                curso = cursos_base[tecnologia][2]  # Curso complementario para Senior

            # Obtenemos el link al curso desde el diccionario (o uno genérico si no está)
            link = cursos_links.get(curso, "https://udeUngs.com/no-curso")

        # 📋 Agregamos la recomendación generada a la lista
        recomendaciones.append({
            "rol": rol,
            "tecnologia": tecnologia,
            "seniority": seniority,
            "cluster": cluster,
            "curso_recomendado": curso,
            "link": link
        })

    # ✅ Devolvemos la lista completa con las recomendaciones
    return recomendaciones
