import requests
from bs4 import BeautifulSoup
from ..settings import headers

def site1():
    url = 'https://www.inovacaotecnologica.com.br/noticias/assuntos.php?assunto=espaco'
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
    url = 'https://revistagalileu.globo.com/ciencia/espaco/'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('h2')
    for artigo in artigos:
        try:
            titulo = artigo.getText().strip().removeprefix(' ')
            descricao = artigo.find_next('p', attrs={'class': 'feed-post-body-resumo'}).getText().strip()

            link = artigo.find('a').get('href')
            data = artigo.find_next('span', attrs={'class': 'feed-post-datetime'}).getText().strip()

            print(f"{titulo} | Postado {data}\n{descricao}\n{link}")
            print("-----------------------------------\n")
        except:
            pass


def site3():
    url = 'https://canaltech.com.br/espaco/'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('article', attrs={'class': 'relative mx-0 mb-0 mt-4 hover:cursor-pointer tablet:my-4 [&_a]:text-[inherit] transition-colors duration-300 ease-ease [&_h3]:hover:text-mglBlue400 [&_.image-container]:hover:scale-105'})
    for artigo in artigos:
        titulo = artigo.find('h2').getText()

        tempo = artigo.find('span', attrs={'class': 'flex flex-row items-center font-medium text-black/40 [&_svg]:mr-[2px]'}).getText()

        link = artigo.find('a').get('href')

        print(f"{titulo} | Postado há: {tempo}\n{link}")
        print('---------------------\n')


def site4():
    url = 'https://www.cnnbrasil.com.br/?search=Astronomia'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    artigos = soup.find_all('div', attrs={'class': 'flex flex-col gap-4'})
    for artigo in artigos:
        titulo = artigo.find('a', attrs={'class': 'text-gray-950 hover:underline'}).getText()
        data = artigo.find_next('time', attrs={'class': 'text-base font-normal mt-6 inline-flex items-center gap-1 text-gray-400'}).getText()

        link = artigo.find('a', attrs={'class': 'text-gray-950 hover:underline'}).get('href')

        print(f"{titulo} | Postado em: {data}\n{link}")
        print('----------------------------\n')

def site5():
    paginas = int(input('Quantas páginas? (Entre 1 a 15):\n>>>'))
    while paginas not in range(1, 16):
        paginas = int(input('Digite corretamente.\nQuantas páginas? (Entre 1 a 15):\n>>>'))

    url = 'https://www.bbc.com/portuguese/topics/cr50y580rjxt'

    r = requests.Session().get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    for i in range(paginas):
        artigos = soup.find_all('li', attrs={'class': 'bbc-t44f9r'})
        for artigo in artigos:
            titulo = artigo.find('a').getText()
            data = artigo.find('time', attrs={'class': 'promo-timestamp bbc-16jlylf e1mklfmt0'}).getText()

            link = artigo.find('a').get('href')

            print(f"{titulo} | {data}\n{link}")
            print("----------------------------\n")

            url = f'https://www.bbc.com/portuguese/topics/cr50y580rjxt?page={i+2}'

            r = requests.Session().get(url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
