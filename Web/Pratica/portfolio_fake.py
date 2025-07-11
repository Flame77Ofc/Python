import streamlit as st

st.set_page_config(
    page_title = "Portfólio Profissional",
    page_icon = '📁',
    layout = 'wide'
)

st.markdown("""
<style>
    #MainMenu, footer, header {
            visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)


with st.sidebar:
    st.title('Navegação')
    st.badge('Página Inicial', color='blue', icon='🚀')
    st.divider()

    st.write('## Tenho interesse')
    st.link_button('Converse comigo!', url='#')

st.title('Olá, Bem-vindo ao meu portfólio!')
st.write('## Linguagens que domino: ')

col1, col2 = st.columns([2, 2])

with col1:
    st.caption('Linguagens de programação')
    st.slider('Python', value = 79, width = 350, disabled = True)
    st.slider('JavaScript', value = 12, width = 350, disabled = True)

with col2:
    st.caption('Linguagem de hypertexto e de estilo')
    st.slider('HTML', value = 100, width = 350, disabled = True)
    st.slider('CSS', value = 75, width = 350, disabled = True)

st.divider()

st.write('## Projetos')

st.write("""
- Jogo da Forca
- Par ou ímpar
- Bot que reage a comandos simples
- Jogo da Velha (Jogando contra bot e 1v1)
- Projetos de scraping (Pega dados do **mercado livre**, **z-library**, **g1 notícias**, **clima do tempo**, entre outros)
- Projetos de automação (Entrar em sites como **Instagram**, **entrar em uma partida no chess.com**, **Fazer uma pesquisa no youtube e clicar no primeiro vídeo**, entre outros)
""")


st.divider()
st.write('### Precisando de automação, scraping ou programas de conversão?')
st.link_button('Entre em contato', url='#')

