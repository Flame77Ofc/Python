import streamlit as st
import requests
from bs4 import BeautifulSoup

# Configurações gerais do site
st.set_page_config(
    page_title = "Conversor de Moeda",
    page_icon = "💵",
    layout = "wide"
)

# Sidebar
with st.sidebar:
    st.title('Conversor de Moeda')

    st.divider()

    st.badge("Guia", color = "red", icon = "🍁")
    st.caption("Este site realiza a conversão de dólares para reais e vice-versa. O método que se utiliza é: Coletar o valor do dólar em sites confiáveis e fazer uma média a partir destes valores.")

    st.divider()

    st.badge("Ferramentas", color = "green", icon = "🔰")
    st.caption("As ferramentas utilizadas aqui foram: **Python**, **streamlit**, **requests** e **BeautifulSoup**.")
    st.caption("""
- **STREAMLIT**: Biblioteca python que permite criar sites interativos
- **REQUESTS**: Biblioteca python que permite fazer requisições em sites
- **BEAUTIFUL SOUP**: Biblioteca python que permite coletar informações de uma requisição feita por requests.
""")

    st.divider()

    st.badge("Utilidades", color = "violet", icon = "🔑")
    st.caption("""
- [O que é uma biblioteca em python? - Asimov Academy](https://hub.asimov.academy/blog/bibliotecas-python/)
- [Um guia de Streamlit - Página oficial (Inglês)](https://docs.streamlit.io/)
- [Um guia de requests - Página Oficial (Inglês)](https://requests.readthedocs.io/en/latest/)
- [Um guia de BeautifulSoup - Página Oficial (Inglês)](https://beautiful-soup-4.readthedocs.io/en/latest/)""")


# Scraping de Dados
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

def pegar_media(allow: bool):
    global dolares

    with st.spinner("Aguarde... Carregando."):
        if allow:
            st.caption("O bot faz **scraping** de preços de sites confiáveis")

        media = []

        # 1
        r = requests.Session().get("https://search.brave.com/search?q=dolar+hoje&source=desktop", headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")

        dolar = float(soup.find('span', attrs={'class': 'amount t-primary svelte-14vyw89'}).getText().strip().replace(",", "."))
        media.append(dolar)
        
        if allow:
            texto = f"{dolar} | fonte: pesquisa brave"
            st.write(texto)


        # 2
        r = requests.Session().get("https://wise.com/br/currency-converter/dolar-hoje", headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")


        dolar = float(soup.find('span', attrs={'class': 'text-success'}).getText().strip().replace(",", "."))
        media.append(dolar)

        if allow:
            texto = f"{dolar} | fonte: wise"
            st.write(texto)


        # 3
        r = requests.Session().get("https://www.melhorcambio.com/dolar-hoje", headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        dolar = float(soup.find('input', attrs={'id': 'comercial'}).get('value').strip().replace(',', '.'))
        media.append(dolar)

        if allow:
            texto = f"{dolar} | fonte: melhorcambio"
            st.write(texto)


        # 4
        r = requests.Session().get("https://valor.globo.com/valor-data/", headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        dolar = float(soup.find("div", attrs={'class': 'cell auto data-cotacao__ticker_quote'}).getText().strip().replace(',', '.'))
        media.append(dolar)

        if allow:
            texto = f"{dolar} | fonte: valor.globo"
            st.write(texto)


        # 5
        r = requests.Session().get("https://dolarhoje.com/", headers=headers)
        soup = BeautifulSoup(r.content, 'html.parser')

        dolar = float(soup.find('input', attrs={'id': 'nacional'}).get("value").replace(',', '.'))
        media.append(dolar)

        if allow:
            texto = f"{dolar} | fonte: dolarhoje"
            st.write(texto)


        media = sum(media) / len(media)
        dolares = round(media, 2)

        if allow:
            st.caption(f"Valor atual do dólar: {dolares}")


# Página Principal
st.title("Conversor de Dólares <-> Reais")

col1, col2 = st.columns([1, 2])

with col1:
    escolha = st.selectbox("Escolha o tipo de conversão", options=["Reais para Dólares", "Dólares para Reais"])

    if st.button("Ver o preço do dólar"):
        pegar_media(True)

with col2:
    # Condicional para verificar qual opção o usuário escolheu
    if escolha == "Reais para Dólares":
        reais = st.number_input("Real")

        with st.empty():

            if st.button("Converter"):
                pegar_media(False)

                multiplicacao = reais * dolares
                dolares = st.number_input("Dólar", disabled=True, value=multiplicacao)

    elif escolha == "Dólares para Reais":
        dollars = st.number_input("Dólar")

        with st.empty():
            if st.button("Converter"):
                pegar_media(False)

                divisao = dollars / dolares
                reais = st.number_input("Real", disabled=True, value=divisao)
