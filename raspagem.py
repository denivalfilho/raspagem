# Farei a raspagem de notícias do site do IFSP, onde eu trabalho.

import requests
from bs4 import BeautifulSoup

url = "https://www.ifsp.edu.br/ultimas-noticias"
headers = {'User-Agent': 'Mozilla/5.0'}

resposta = requests.get(url, headers=headers)

sopa = BeautifulSoup(resposta.text, 'html.parser')

noticias = sopa.find_all('h2')

for n in noticias[7:]: #pular as 7 primeiras que são menus
    print(n.get_text().strip())