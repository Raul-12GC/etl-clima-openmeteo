# Pipeline ETL: Pronóstico del Clima 🌦️

Script modular en Python que automatiza la extracción, transformación y carga (ETL) de datos meteorológicos a 7 días utilizando la API pública de Open-Meteo.

## 📋 ¿Qué hace este proyecto?
1. **Extracción (Extract):** Consulta la API REST de Open-Meteo mediante la librería `requests`, validando códigos de estado HTTP y tiempos de espera (*timeout*).
2. **Transformación (Transform):** Procesa la respuesta en formato JSON, cruza las listas paralelas de fechas, temperaturas y precipitación, y aplica una regla de negocio para clasificar la probabilidad de lluvia.
3. **Carga (Load):** Exporta los datos estructurados a un archivo `.csv` con codificación `utf-8-sig` para asegurar la correcta visualización de tildes y caracteres especiales en Excel.

## 🛠️ Tecnologías utilizadas
* **Python 3**
* **Librería `requests`:** Para peticiones HTTP.
* **Módulo nativo `csv`:** Para la generación de archivos tabulares.

## 🚀 Cómo ejecutarlo
1. Clona este repositorio o descarga el archivo `Etl_clima.py`.
2. Instala la dependencia necesaria:
   ```bash
   pip install requests