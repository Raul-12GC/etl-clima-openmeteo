# Pipeline ETL: Pronóstico del Clima 🌦️

Script modular en Python que automatiza la extracción, transformación y carga (ETL) de datos meteorológicos a 7 días utilizando la API pública de Open-Meteo.

## 📊 Estructura de salida (`datos_clima.csv`)
El pipeline genera un archivo tabular delimitado por comas con las siguientes columnas:

| Columna | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `Fecha` | Fecha del pronóstico (`YYYY-MM-DD`) | `2026-11-16` |
| `Tem_max` | Temperatura máxima estimada (°C) | `28.5` |
| `Tem_min` | Temperatura mínima estimada (°C) | `19.2` |
| `Rain_sum` | Precipitación acumulada diaria (mm) | `1.4` |

## 📋 ¿Qué hace este proyecto?
1. **Extracción (Extract):** Consulta la API REST de Open-Meteo mediante la librería `requests`, validando códigos de estado HTTP y tiempos de espera (*timeout*).
2. **Transformación (Transform):** Procesa la respuesta en formato JSON, cruza las listas paralelas de fechas, temperaturas y precipitación, y aplica una regla de negocio para clasificar la probabilidad de lluvia.
3. **Carga (Load):** Exporta los datos estructurados a un archivo `.csv` con codificación `utf-8-sig` para asegurar la correcta visualización de tildes y caracteres especiales en Excel.

## 🛠️ Tecnologías utilizadas
* **Python 3**
* **Librería `requests`:** Para peticiones HTTP.
* **Módulo nativo `csv`:** Para la generación de archivos tabulares.

## 🚀 Despliegue y ejecución local
```bash
git clone https://github.com/Raul-12GC/etl-clima-openmeteo.git
cd etl-clima-openmeteo
pip install requests
python Etl_clima.py