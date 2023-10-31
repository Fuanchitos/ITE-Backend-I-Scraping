from bs4 import BeautifulSoup

with open("HTML/ITE-SCRAP-P2.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

# Buscar elementos de texto
elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'li'])
for element in elements:
    text = element.text.strip()
    # Encontrar y eliminar SPAM
    if "Me gusta enFacebook" not in text and "Síguenos enTwitter" not in text and "Síguenos enYouYube" not in text and "Síguenos enInstagram" not in text and "Manda un mensaje porWhatsApp" not in text:
        print(text)

# Obtener links de imagen
image_tags = soup.find_all('img')
for img in image_tags:
    if 'src' in img.attrs:
        image_source = img['src']
        print("Link:", image_source)