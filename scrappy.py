import requests
from bs4 import BeautifulSoup

# Función para obtener información técnica de la página
def obtener_informacion(url):
    try:
        # Hacer una solicitud a la página
        response = requests.get(url)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Crear un objeto BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Obtener información de cabeceras
            cabeceras = response.headers
            info_tecnica = {
                'URL': url,
                'Status Code': response.status_code,
                'Server': cabeceras.get('Server'),
                'Content-Type': cabeceras.get('Content-Type'),
                'X-Powered-By': cabeceras.get('X-Powered-By'),
                'Plugins': cabeceras.get('X-Plugins')  # Cambia esto según la página
            }

            # Mostrar la información
            for clave, valor in info_tecnica.items():
                print(f"{clave}: {valor}")

            return info_tecnica

        else:
            print(f"Error al acceder a la página: {response.status_code}")
            return None

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

# Función para guardar la información en un archivo
def guardar_en_archivo(informacion, nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            for clave, valor in informacion.items():
                archivo.write(f"{clave}: {valor}\n")
        print(f"Información guardada en {nombre_archivo}")
    except Exception as e:
        print(f"Ocurrió un error al guardar el archivo: {e}")

# Función principal
def main():
    url = input("Introduce la URL de la página que deseas scrappear: ")

    # Obtener información de la página
    info = obtener_informacion(url)

    if info:
        # Preguntar si se quiere guardar la información
        guardar = input("¿Deseas guardar la información en un archivo? (s/n): ").strip().lower()
        if guardar == 's':
            nombre_archivo = input("Introduce el nombre del archivo (con extensión .txt): ")
            guardar_en_archivo(info, nombre_archivo)

# Ejecutar el programa
if __name__ == "__main__":
    main()
