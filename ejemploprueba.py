import requests
import html5lib
from bs4 import BeautifulSoup

# Realiza una solicitud HTTP para obtener el contenido de la página
url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    # Analiza el contenido HTML de la página
    soup = BeautifulSoup(response.text, 'html5lib')

    texto = soup.find_all('p')
    for texto in texto:
        print(texto.text)
        
else:
    print("Error al obtener la página. Código de respuesta:", response.status_code)
