# Farei a raspagem de notícias do site do IFSP, onde eu trabalho.

import requests
from bs4 import BeautifulSoup

url = "https://www.ifsp.edu.br/ultimas-noticias"
headers = {'User-Agent': 'Mozilla/5.0'}

resposta = requests.get(url, headers=headers)

sopa = BeautifulSoup(resposta.text, 'html.parser')

noticias = sopa.find_all('h2', class_='tileHeadline') # Em vez de pegar todos os h2, pegamos apenas h2 que estão dentro da classe 'tileHeadline'

print(f"--- Foram encontradas {len(noticias)} notícias ---")

for n in noticias:
    print(n.get_text())