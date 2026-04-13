# Farei a raspagem de notícias do site do IFSP, onde eu trabalho.

import requests
from bs4 import BeautifulSoup

url = "https://www.ifsp.edu.br/index.php/ultimas-noticias"

resposta = requests.get(url)

sopa = BeautifulSoup(resposta.text, 'html.parser')

noticias = sopa.find_all('h2', class_='tile-headline') 
# Porque esse h2? No HTML, os textos são organizados por hierarquia de importância, indo do 1 ao 6:
#    <h1>: O título principal da página (geralmente o nome do site ou o assunto principal).
#    <h2>: Subtítulos ou títulos de seções (como os títulos de cada notícia).
#    <h3> a <h6>: Títulos menores, para subseções dentro dos temas.