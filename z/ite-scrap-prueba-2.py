import requests
from bs4 import BeautifulSoup

# Realiza una solicitud HTTP para obtener el contenido de la página
url = "https://www.ensenada.tecnm.mx/ingenieria-en-innovacion-agricola-sustentable/"

try:
    response = requests.get(url)
    if response.status_code == 200:
        # Guarda el contenido HTML en un archivo local
        with open("pagina.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        
        # Analiza el contenido HTML del archivo
        with open("pagina.html", "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, 'html.parser')
        
        # Encuentra y muestra todos los párrafos en el archivo HTML
        paragraphs = soup.find_all('p')
        for paragraph in paragraphs:
            print(paragraph.text)
    else:
        print("Error al obtener la página. Código de respuesta:", response.status_code)
except Exception as e:
    print("Ocurrió un error al descargar la página:", str(e))
