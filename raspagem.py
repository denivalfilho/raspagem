# Farei a raspagem de notícias do site do IFSP, onde eu trabalho.

import requests
from bs4 import BeautifulSoup

def conectar_ao_ifsp():
    url = "https://www.ifsp.edu.br/index.php/ultimas-noticias"