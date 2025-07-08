import requests
from bs4 import BeautifulSoup
from ..settings import headers

def pegar_livros(assunto):
    print('----------------------')
    idioma = input(f'Quer livros em português (Brasil) para a pesquisa de "{assunto}"? [S/N]:\n>>>').upper().strip()
    while idioma not in ['S', 'N']:
        idioma = input('Digite corretamente: Quer livros em português (Brasil)? [S/N]:\n>>>').upper().strip()
    if idioma == 'S':
        url = 'https://z-library.sk/s/' + assunto + '?languages%5B%5D=brazilian&languages%5B%5D=portuguese'
    else:
        url = 'https://z-library.sk/s/' + assunto
    r = requests.Session().get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')

    i = 0
    with open(f'{assunto}.pdf', 'w', encoding='utf-8') as arquivo: pass
    while True:
        boxes = soup.find_all('div', attrs={'class': 'book-item resItemBoxBooks'})
        for box in boxes:
            contador = box.find('div', attrs={'class': 'counter'}).getText().strip()

            livro = box.find('div', attrs={'slot': 'title'}).getText()
            link = box.find('z-bookcard').get('href')
            link = f'http://z-library.sk{link}'

            autor = box.find('div', attrs={'slot': 'author'}).getText()

            print(f"{contador} | {livro} (Autor: {autor}) -> {link}")
            with open(f'{assunto}.pdf', 'a', encoding='utf-8') as arquivo:
                arquivo.write(f"{contador} | {livro} (Autor: {autor}) -> {link}\n")

        if idioma == 'S':
            url = 'https://z-library.sk/s/' + assunto + f'/?languages%5B0%5D=brazilian&languages%5B1%5D=portuguese&page={i+2}'
        else:
            url = 'https://z-library.sk/s/' + assunto + f'?page={i+2}'

        r = requests.Session().get(url, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        if soup.find('div', attrs={'class': 'cBox1'}):
            break
        else:
            pass

        i += 1
    print('----------------------\n')

