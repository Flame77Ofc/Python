import requests
from bs4 import BeautifulSoup
import pandas as pd
from ..settings import headers

def produtos(nome):
    url = f'https://lista.mercadolivre.com.br/{nome}'
    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.content, 'html.parser')
    produtos = soup.find_all('li', attrs={'class': 'ui-search-layout__item'})

    lista_produtos = []
    lista_links = []
    lista_precos = []

    for produto in produtos:
        img_tag = produto.find('img')
        a_tag = produto.find('a')
        preco_tag = produto.find('span', attrs={'class': 'andes-money-amount__fraction'})

        if img_tag and a_tag and preco_tag:
            titulo = img_tag.get('title', 'Sem título')
            link = a_tag.get('href', 'Sem link')
            preco_texto = preco_tag.getText().replace('.', '')

            try:
                preco = int(preco_texto)
            except ValueError:
                preco = 0

            print(f"{titulo} - {preco}\n{link}\n")

            lista_produtos.append(titulo)
            lista_links.append(link)
            lista_precos.append(preco)

    df = pd.DataFrame({
        'Produto': lista_produtos,
        'Link': lista_links,
        'Preço': lista_precos
    })

    df = df.sort_values(by='Preço', ascending=True, ignore_index=True)
    df.to_excel('produtos.xlsx', index=False)

    df = df.sort_values(by='Preço', ascending=True, ignore_index=True)
    print(df)
