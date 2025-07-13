import streamlit as st
from assets.css.no_login_centralized import set_style

set_style(True, True, True)

try:
    with open('./data/login.json', 'r') as arquivo: pass
    st.write('Logado!')
except:
    st.title('🌟 Vamos criar conteúdo e ganhar fama!')
    st.caption('Crie conteúdos únicos e com criativdade!')

    if st.button(':material/login: Criar conta ou fazer meu cadastro'):
        st.switch_page('pages/login.py')
