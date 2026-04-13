# Farei a raspagem de notícias do site do IFSP, onde eu trabalho.

import requests
from bs4 import BeautifulSoup

url = "https://www.ifsp.edu.br/index.php/ultimas-noticias"

resposta = requests.get(url)

sopa = BeautifulSoup(resposta.text, 'html.parser')