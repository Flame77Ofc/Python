from ..settings import headers
def wikipedia(assunto: str) -> str:
    assunto = str(assunto).strip().lower()
    import requests
    from bs4 import BeautifulSoup

    while True: # while True para uso de break
        site = 'https://pt.wikipedia.org/wiki/'
        r = requests.Session().get(site + assunto, headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        # Limpa o arquivo (Para deletar o conteúdo antigo e adicionar o novo)
        with open('arquivo.pdf', 'w', encoding='utf-8') as pdf: pass

        # Verifica se existe links relacionados
        if soup.find_all('div', attrs={'class': 'mw-search-result-heading'}) or soup.find('div', attrs={'id': 'disambig'}):
            links = soup.find_all('div', attrs={'class': 'mw-search-result-heading'})
            caixa = []
            if links:
                for link in links:
                    print(link.getText())
                    caixa.append(str(link.getText().strip()))

            disambig = soup.find('div', attrs={'id': 'disambig'})
            if disambig:
                container = soup.find('div', attrs={'class': 'mw-content-ltr mw-parser-output'})

                box = container.find('ul')
                items = box.find_all('li')
                for item in items:
                    link = item.find('a')

                    print(link.getText())
                    caixa.append(str(link.getText()))

            pesquisa = input('Digite o que procura:\n>>>')
            if pesquisa in caixa:

                site = site + pesquisa
                r = requests.Session().get(site, headers=headers)
                soup = BeautifulSoup(r.content, 'html.parser')

            else:
                print('Parece que o que você procura não foi encontrado.')
                break


        # Verifica se a página não existe
        not_exist = soup.find('p', attrs={'class': 'mw-search-nonefound'})
        if not_exist or soup.find('div', attrs={'id': 'noarticletext'}):
            print('Página não encontrada.')
            break

        # Verifica se é possível redirecionar para uma página que faz mais sentindo
        redirection = soup.find('span', attrs={'class': 'mw-redirectedfrom'})
        if redirection:
            print(redirection.getText())

        # Pega o título da página
        title = soup.find('span', attrs={'class': 'mw-page-title-main'})
        if title:
            print(f"Página encontrada: {title.getText().strip()}")

        # Extrai todo o conteúdo da parte principal
        texto = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img'])
        for text in texto:
            if 'Ver também' in text or 'Bibliografia' in text or 'Referências' in text or 'Ligações externas' in text or 'Notas' in text or 'Exemplos' in text or 'Discografia' in text:
                break


            print(text.getText())

            # Abre e coloca o conteúdo da página dentro do arquivo pdf.
            with open('arquivo.pdf', 'a+', encoding='utf-8') as pdf:
                pdf.write(str(text.getText().strip()))
                pdf.write('\n')


        permissao = input('Gostaria de ver imagens? [S/N]:\n>>>').strip().upper()
        while permissao not in ['S', 'N']:
            permissao = input('Digite corretamente.\nGostaria de ver imagens? [S/N]:\n>>>').strip().upper()
        if permissao == 'S':
            imagens = soup.find_all('a', attrs={'class': 'mw-file-description'})
            for imagem in imagens:
                if 'Question_book-new' in str(imagem.find('img').get('src')):
                    pass
                else:

                    url = imagem.find('img').get('src')
                    url = 'https:' + url
                    descricao = imagem.find_next_sibling('figcaption')

                    try:
                        print(f"{descricao.getText()} -> {url}")
                        with open('arquivo.pdf', 'a+', encoding='utf-8') as pdf:
                            pdf.write(f"{descricao.getText()} -> {url}\n")
                    except:
                        pass


        elif permissao == 'N':
            pass


        break
