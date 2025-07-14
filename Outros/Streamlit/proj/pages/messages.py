import streamlit as st
from assets.css.no_login_centralized import set_style


try:
    with open('./data/login.json', 'r') as arquivo: pass
    st.write('Logado!')
except:
    set_style(True, True, True)

    st.title('💬 Vamos nos comunicar e formar uma comunidade!')
    st.caption('Para conversar com pessoas, é necessário fazer login')

    if st.button(':material/login: Criar conta ou Entrar'):
        st.switch_page('pages/welcome.py')
