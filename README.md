# README.md

## 📦 Configuración del entorno y ejecución del proyecto

Este proyecto agrupa empleados del sector IT en clusters según su rol, tecnología y seniority, y les sugiere cursos de mejora personalizados.

---
### ✅ Requisitos
- Python 3.12
- pip habilitado (`py -m ensurepip` si no está disponible)

---
### 🔧 1. Crear entorno virtual 

```bash
py -m venv sklearn-env
```

Activar el entorno virtual:

```bash
.\sklearn-env\Scripts\activate
```

---

### 📥 2. Instalar dependencias

Instalar librerías necesarias desde `dependencias.txt`:

```bash
py -m pip install -r dependencias.txt
```

---

### 🚀 3. Ejecutar el programa

Desde la raíz del proyecto, ejecutar:

```bash
py /main.py
```

Esto generará un archivo con recomendaciones en la carpeta:

```
data/resultados_recomendaciones/
```

El archivo tendrá un nombre como:
```
recomendaciones_empleados_20250330_1542.csv
```

---

