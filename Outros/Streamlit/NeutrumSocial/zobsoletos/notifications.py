import streamlit as st
from assets.css.no_login_centralized import set_style


try:
    with open('./data/login.json', 'r') as arquivo: pass
    st.write('Logado!')
except:
    set_style(True, True, True)

    st.title('🔔 O que estão falando sobre mim?')
    st.caption('Descubra novidades, veja as notificações de um post ou de uma atualização.')

    if st.button(':material/login: Criar conta ou Entrar'):
        st.switch_page('pages/welcome.py')
