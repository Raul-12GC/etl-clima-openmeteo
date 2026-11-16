##Librerias
import requests
import csv


##Configuración
url = "https://api.open-meteo.com/v1/forecast"
parametros = {
    "latitude": 7.0292,
    "longitude": -71.4281,
    "daily": ["temperature_2m_max", "temperature_2m_min", "rain_sum"],
    "timezone": "America/Bogota",
}
 
def peticion_api():
    r = requests.get(url, params= parametros, timeout= 10 )
    r.raise_for_status() #validación de estatus
    return r.json()

def transformar_datos(datos):
    "Convertir JSON en listas"
    lista_datos = []
    for i in range(len(datos["daily"]["time"])):
        lista_datos.append([
            datos["daily"]["time"][i],
            datos["daily"]["temperature_2m_max"][i],
            datos["daily"]["temperature_2m_min"][i],
            datos["daily"]["rain_sum"][i]
            
            ])
    return lista_datos


def guardar_datos_csv(datos, archivo= "datos_clima.csv"):
    with open(archivo,"w", newline= "", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        writer.writerow(["Fecha", "Tem_max", "Tem_min", "Rain_sum"])
        writer.writerows(datos)
    return archivo

def main():
    try:
        peticion = peticion_api()
        procesar_datos = transformar_datos (peticion)
        guardar_datos = guardar_datos_csv (procesar_datos)
        print("La ejecución fue exitosa")
    except requests.exceptions.RequestException as e:
        print(f"Error en la conexión o de respuesta de la API: {e}")
    except KeyError as e:
        print(f"La estructura del JSON cambió no se encuentra la clave: {e}")
    except PermissionError as e: 
        print(f"No tienes permisos (¿tienes el Excel abierto?): {e}")  
    except Exception as e: 
        print(f"Ocurrió un erro inesperado: {e}")
         
if __name__ == "__main__":
    main()
    