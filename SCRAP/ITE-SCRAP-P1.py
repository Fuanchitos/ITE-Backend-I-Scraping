from bs4 import BeautifulSoup

with open("HTML/ITE-SCRAP-P1.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

elements = soup.find_all(['p', 'h1', 'h2'])
for element in elements:
    text = element.text.strip()
    # Encontrar y Eliminar SPAM
    if "Me gusta enFacebook" not in text and "Síguenos enTwitter" not in text and "Síguenos enYouYube" not in text and "Síguenos enInstagram" not in text and "Manda un mensaje porWhatsApp" not in text:
        print(text)
        