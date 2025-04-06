# Importamos los módulos necesarios:
import json          # Para trabajar con archivos JSON
import os            # Para verificar si el archivo existe

# Definimos una función para cargar un archivo JSON desde una ruta específica
def load_json_from_file(file_path):
    # Verificamos si el archivo existe en la ruta proporcionada
    if not os.path.exists(file_path):
        # Si no existe, lanzamos una excepción informativa
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    
    # Si el archivo existe, lo abrimos en modo lectura con codificación UTF-8
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            # Intentamos cargar el contenido como JSON
            return json.load(file)
        except json.JSONDecodeError as e:
            # Si hay un error de formato en el JSON, lanzamos una excepción detallada
            raise ValueError(f"Error al parsear el archivo JSON {file_path}: {e}")
