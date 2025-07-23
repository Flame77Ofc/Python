import streamlit as st
import requests
from bs4 import BeautifulSoup


st.set_page_config(
    page_title = 'Página dos Estudantes',
    page_icon = '👨🏻‍🎓',
    layout = 'wide',
)

st.markdown("""<style>
    #MainMenu, footer {
        visibility: hidden;
    }

</style>""", unsafe_allow_html = True)


with st.sidebar:
    st.title('Dashboard')
    st.divider()

    st.badge('Boas-Vindas', color='blue', icon='🐾')
    st.caption('Seja bem-vindo(a) à página do guia do estudante! Aqui você encontrará dicas de estudo, melhores professores, e um bot integrado que busca conteúdos de graça')

    st.divider()

    st.badge('Bot - Busca assuntos', color='violet', icon='🤖')
    st.caption('Você pode facilmente pesquisar aqui um assunto que deseja.')






# ---------------------------------------------------
    assunto = st.text_input('Digite o assunto', placeholder='Assunto')

    if st.button('Enviar') and assunto != '':
        with st.spinner('Carregando...'):
            def wikipedia(assunto: str) -> str:
                headers = {
                    "User-Agent": (
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/125.0.6422.113 Safari/537.36 "
                        "Edg/125.0.2535.67"
                    ),
                    "Accept": (
                        "text/html,application/xhtml+xml,application/xml;"
                        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                        "application/signed-exchange;v=b3;q=0.7"
                    ),
                    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
                    "Connection": "keep-alive",
                    "Upgrade-Insecure-Requests": "1",
                    "Sec-Fetch-Dest": "document",
                    "Sec-Fetch-Mode": "navigate",
                    "Sec-Fetch-Site": "none",
                    "Sec-Fetch-User": "?1",
                    "Sec-Ch-Ua": (
                        '"Chromium";v="125", "Microsoft Edge";v="125", '
                        '"Not.A/Brand";v="24"'
                    ),
                    "Sec-Ch-Ua-Mobile": "?0",
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "DNT": "1",
                    "TE": "trailers"
                }

                assunto = str(assunto).strip().lower()
                while True: # while True para uso de break
                    site = 'https://pt.wikipedia.org/wiki/'
                    r = requests.Session().get(site + assunto, headers=headers)
                    soup = BeautifulSoup(r.content, 'html.parser')

                    # Verifica se existe links relacionados
                    if soup.find_all('div', attrs={'class': 'mw-search-result-heading'}) or soup.find('div', attrs={'id': 'disambig'}):
                        links = soup.find_all('div', attrs={'class': 'mw-search-result-heading'})
                        caixa = []

                        st.info('Possíveis resultados que você esteja procurando (Caso tenha o resultado que esteja procurando, escreva novamente incluindo **TODOS** os caracteres da pesquisa.)')
                        if links:
                            for link in links:
                                st.write(link.getText())
                                caixa.append(str(link.getText().strip()))

                        disambig = soup.find('div', attrs={'id': 'disambig'})
                        if disambig:
                            container = soup.find('div', attrs={'class': 'mw-content-ltr mw-parser-output'})

                            box = container.find('ul')
                            items = box.find_all('li')
                            for item in items:
                                link = item.find('a')

                                st.write(link.getText())
                                caixa.append(str(link.getText()))
                        else:
                            st.write('Parece que o que você procura não foi encontrado.')
                            break


                    # Verifica se a página não existe
                    not_exist = soup.find('p', attrs={'class': 'mw-search-nonefound'})
                    if not_exist or soup.find('div', attrs={'id': 'noarticletext'}):
                        st.write('Página não encontrada.')
                        st.warning('Verifique se esse assunto realmente existe.')
                        break

                    # Verifica se é possível redirecionar para uma página que faz mais sentindo
                    redirection = soup.find('span', attrs={'class': 'mw-redirectedfrom'})
                    if redirection:
                        st.write(redirection.getText())

                    # Pega o título da página
                    title = soup.find('span', attrs={'class': 'mw-page-title-main'})
                    if title:
                        st.write(f"Página encontrada: {title.getText().strip()}")


                    # Extrai todo o conteúdo da parte principal
                    conteudo = ''
                    texto = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'img'])

                    st.toast('Algo encontrado!', icon='⛄')
                    for text in texto:
                        if 'Ver também' in text or 'Bibliografia' in text or 'Referências' in text or 'Ligações externas' in text or 'Notas' in text or 'Exemplos' in text or 'Discografia' in text:
                            break

                        conteudo += text.getText()
                        st.write(text.getText())

                    st.download_button('Deseja baixar?', str(conteudo), f'{assunto}.txt')
                    break

            wikipedia(assunto)


st.title('Página dos Estudantes')


st.divider()
st.badge('Área de estudos', color = 'red', icon = '🍁')

st.markdown('#### Como estudar melhor e mais efetivamente? ')

st.write('<p style="color: lightgray;">Estudar efetivamente pode ser um desafio para muitos. Se não aplicar as técnicas certas, podem causar muitas frustações. Separamos algumas dicas para render um estudo melhor</p>', unsafe_allow_html = True)

st.write("""<p style="color: lightgray;">Existem diversas técnicas adequadas de estudo para garantir que a forma de aprendizado é eficaz. Vamos conferir:</p>
<h4 style="color: grey;">👨🏻‍🚀 Técnica Feynman</h4>
<p style="color: lightgray">Essa técnica foi criada pelo físico teórico <strong>Richard Feynman</strong>, que recebeu um prêmio Nobel de física. Ele foi responsável por criar uma técnica chamada <strong>Técnica Feynman</strong>. <br> Essa técnica consiste em: <strong>Escolher algum assunto</strong>; <strong>Aplicar na prática</strong>; <strong>Ensinar para alguém</strong>; <strong>Revisar tudo aprendido</strong> <br> Vista com uma técnica poderosa, pode se encaixar perfeitamente em uma nova forma de aprendizado.</p>""", unsafe_allow_html = True)

st.image("https://imgs.search.brave.com/9rKdG51Mfa9QpOhjCfU1uzbZtCRzoJg-q1_6hWUM6p8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi8xLzFhL1Jp/Y2hhcmRGZXlubWFu/LVBhaW5lTWFuc2lv/bldvb2RzMTk4NF9j/b3B5cmlnaHRUYW1p/a29UaGllbF9idy5q/cGcvNTEycHgtUmlj/aGFyZEZleW5tYW4t/UGFpbmVNYW5zaW9u/V29vZHMxOTg0X2Nv/cHlyaWdodFRhbWlr/b1RoaWVsX2J3Lmpw/Zw", caption = "Richard Feynman - Físico Teórico | Criador da Técnica Feynman", width=350)

st.write("""<h4 style="color: grey;">🍅 Técnica Pomodoro</h4>
<p style="color: lightgray">A técnica do pomodoro é muito lembrado por um <strong>tomate</strong>. Essa técnica é incrivelmente boa, muitos estudantes usam isso para aprimorar seus estudos como um machado afiado!🪓 <br> <br> Esta técnica consiste em: <strong>Ficar 25 a 40 minutos de foco total</strong> e <strong>5 a 10 minutos de descanso</strong>, repetindo isso umas 4 ou 5 vezes, dependendo do tempo disponível de pessoa para pessoa. Os valores podem aumentar ou diminuir, e cada estudante pode adaptar para o horário que se sentir melhor, porém o que o pomodoro mais se concentra é em: Foco total e descanso para "fluir melhor o cérebro"</p>""", unsafe_allow_html = True)

st.image("https://www.pontotel.com.br/local/wp-content/uploads/2024/11/tecnica-pomodoro-como-funciona-a-tecnica-pomodoro-funciona-1024x945.webp", caption="Técnica Pomodoro", width=350)



st.write("""<h4 style="color: grey">🃏 FlashCards</h4>""", unsafe_allow_html = True)
st.write("""<p style="color: lightgray;">Considerado uma das melhores técnicas de estudo, os Flashcards são <strong>cartas que apresentam dois lados: Um lado é uma pergunta, e do outro lado (virando a carta) está o significado ou conceito</strong>.Flashcards são algo parecido com a imagem abaixo</p>""", unsafe_allow_html = True)

st.image("https://oaprendizemsaude.wordpress.com/wp-content/uploads/2017/07/sem-tc3adtulo.png?w=660", caption="Esquema de um flashcard", width=350)

st.write("""<p>Os flashcards funcionam por meio de um estudo feito por <strong>Hermann Ebbinghaus</strong>. O estudo de Ebbinghaus mostrou que precisamos relembrar o assunto que estudamos em dias especificos. Por exemplo, se estudei na segunda-feira um assunto, os flashcards são feitos para serem estudados: <strong>No mesmo dia do estudo, após 1 dia, após 3 dias, após 1 semana</strong>, etc... <br> Porém, essa regra só serve para aqueles flashcards que você <strong>já dominou</strong>. Se você tem um flashcard, e não soube responder a pergunta antes de virar a carta, então esse flashcard deve ser estudado denovo num tempo mais curto que aquela ordem.""", unsafe_allow_html = True)

st.image("https://upload.wikimedia.org/wikipedia/commons/9/92/Ebbinghaus2.jpg", caption="Hermann Ebbinghaus", width=350)
