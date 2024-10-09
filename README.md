# Scrappy
Un script en Python que realiza web scraping para obtener información técnica de una página web, incluyendo el sistema operativo, plugins y otras cabeceras relevantes

## Cómo funciona el script:
**Solicitar URL**: Pregunta al usuario por la URL de la página que desea scrappear.

**Obtener información**: Hace una solicitud a la página y extrae información técnica relevante de las cabeceras HTTP, como el servidor y el tipo de contenido.

**Mostrar información**: Imprime la información en la consola.

**Guardar en archivo**: Pregunta si el usuario desea guardar la información en un archivo de texto y lo guarda si el usuario lo desea.

## Instrucciones:

Ejecuta el script con Python:

```
python web_scraper.py
```

Sigue las instrucciones en pantalla para introducir la URL y decidir si quieres guardar los resultados.

## Notas:

Asegúrate de que el sitio web permite el scraping revisando su archivo **robots.txt**.
