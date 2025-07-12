import requests
from bs4 import BeautifulSoup
from ..settings import headers

def globo():
    r = requests.get('https://g1.globo.com/', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    print(soup.title)

    noticias = soup.find_all('div', attrs={'class': 'bastian-feed-item'})
    for noticia in noticias:
        titulo = noticia.find('h2').getText()
        link = noticia.find('a').get('href')

        print(f"{titulo} -> {link}")

def bbc():
    r = requests.Session().get('https://www.bbc.com/portuguese', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    noticias = soup.find('ul', attrs={'class': 'bbc-1rrncb9'})
    lista = noticias.find_all('li')
    for item in lista:
        titulo = item.find('a').getText()
        link = item.find('a').get('href')

        print(f"{titulo} -> {link}")

def r7():
    r = requests.Session().get('https://www.r7.com/', headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    caixas = soup.find_all('article', attrs={'class': 'card-@container card-flex card-flex-col'})
    for caixa in caixas:
        titulo = caixa.find('h3').getText()
        link = caixa.find('a').get('href')

        print(f"{titulo} -> {link}")
