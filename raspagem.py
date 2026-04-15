import requests
from bs4 import BeautifulSoup

url = "https://www.ifsp.edu.br/ultimas-noticias"
headers = {'User-Agent': 'Mozilla/5.0'}

resposta = requests.get(url, headers=headers)

sopa = BeautifulSoup(resposta.text, 'html.parser')

noticias = sopa.find_all('h2', class_='tileHeadline')
for n in noticias:
    titulo = n.get_text().strip()
    link_tag = n.find('a')
    
    if link_tag:
        link_completo = "https://www.ifsp.edu.br" + link_tag['href']
        print(f"Título: {titulo}")
        print(f"Link: {link_completo}\n")