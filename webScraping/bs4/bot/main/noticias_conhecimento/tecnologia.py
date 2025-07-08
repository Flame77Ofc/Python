import requests
from bs4 import BeautifulSoup
from ..settings import headers


def site1():
    url = 'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=informatica'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    artigos = soup.find_all('div', attrs={'class': 'manchete'})
    for artigo in artigos:
        try:
            titulo = artigo.find('a').getText()
            link = url + artigo.find('a').get('href')

            descricao = artigo.find('p').getText().replace('Leia mais...', '')
            data = artigo.find('div', attrs={'class': 'data'}).getText()

            print(f"{titulo} | Postado em: {data}\n{descricao}\n{link}")
            print("-----------------------------------\n")
        except:
            pass


def site2():
    url = 'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=robotica'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('div', attrs={'class': 'pure-u-sm-6-8 manchete assuntos-todas'})
    for artigo in artigos:
        try:
            titulo = artigo.find('a').getText()
            link = url + artigo.find('a').get('href')

            descricao = artigo.find('p').getText().replace('Leia mais...', '')
            data = artigo.find('div', attrs={'class': 'data'}).get_text()

            print(f"{titulo} | Postado em: {data}\n{descricao}\n{link}")
            print("-----------------------------------\n")
        except:
            pass


def site3():
    url = 'https://oglobo.globo.com/economia/tecnologia/'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('div', attrs={'class': 'feed-post-body'})
    for artigo in artigos:
        titulo = artigo.find('a', attrs={'class': 'feed-post-link'}).getText()
        data = artigo.find('span', attrs={'class': 'feed-post-datetime'}).getText()

        descricao = artigo.find_next('p', attrs={'class': 'feed-post-body-resumo'}).getText()
        link = artigo.find('a', attrs={'class': 'feed-post-link'}).get('href')

        print(f"{titulo} | Postado há: {data}\n{descricao}\n{link}")
        print("-----------------------------------\n")
