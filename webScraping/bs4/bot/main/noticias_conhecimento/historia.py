import requests
from bs4 import BeautifulSoup
from ..settings import headers

def site1():
    url = 'https://veja.abril.com.br/noticias-sobre/historia'
    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('h2', attrs={'class': 'title'})
    for artigo in artigos:
        titulo = artigo.getText()
        link = artigo.find_parent('a').get('href')

        data = artigo.find_next('span').find_next('time')
        if data:
            data = data.getText()
        else:
            data = f"| {artigo.find_next('span', attrs={'class': 'author'}).find('span', attrs={'class': 'date-post'}).getText().strip()}"

        print(f"{titulo} {data}\n{link}")
        print("-----------------------------\n")


def site2():
    url = 'https://www1.folha.uol.com.br/folha-topicos/historia-do-brasil/?utm_source=chatgpt.com'
    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('a', attrs={'class': 'c-headline__url'})
    for artigo in artigos:
        try:
            titulo = artigo.find('h2').getText().strip()
            link = artigo.get('href')

            descricao = artigo.find('p', attrs={'class': 'c-headline__standfirst'}).getText().strip()
            data = artigo.find('time', attrs={'class': 'c-headline__dateline'}).getText().strip()
            print(f"{titulo} | Publicado em {data}\n{descricao}\n{link}")
            print('----------------------------------\n')
        except:
            pass


def site3():
    url = 'https://super.abril.com.br/historia/'
    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('div', attrs={'class':'col-s-12 col-l-9'})
    for artigo in artigos:
        titulo = artigo.find('h2', attrs={'class': 'title'})
        data = artigo.find_next('span', attrs={'class': 'date-post'}).getText().strip()

        link = titulo.find_parent('a').get('href')

        print(f"{titulo.getText()} | Postado em {data}\n{link}")
        print("-----------------------------\n")

