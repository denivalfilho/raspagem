# Farei a raspagem de notícias do site do IFSP, onde eu trabalho.

import requests
from bs4 import BeautifulSoup

url = "https://www.ifsp.edu.br/index.php/ultimas-noticias"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.37'
}

try:
    resposta = requests.get(url, headers=headers)
    sopa = BeautifulSoup(resposta.text, 'html.parser')
    noticias = sopa.find_all('h2')
