from bs4 import BeautifulSoup

with open("HTML/scrap-prueba-1.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, 'html.parser')

elements = soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'table'])
for element in elements:
    if element.name == 'table':
        for row in element.find_all('tr'):
            row_data = [cell.text for cell in row.find_all('td')]
            print("\t".join(row_data))  
        print()  
    else:
        print(element.text.strip())  


