import streamlit as st
from assets.css.no_login_centralized import set_style

set_style(True, False, False)

st.title('Bem vindo!')

try:
    with open('data/welcome-data.txt', 'r', encoding='utf-8') as file:
        with open('data/welcome-data.txt', 'w', encoding='utf-8') as file:
            file.write('Usuário já acessou a página\n')
except:
    with open('data/welcome-data.txt', 'w', encoding='utf-8') as file:
        file.write('Primeira vez que o usuário acessa a página!\n')
    st.balloons()
    st.toast("+1 Membro!", icon="🤗")


st.subheader('O que é o NeutrumSocial?')
st.caption('NeutrumSocial é um projeto grande de uma simulação de Rede Social. Aqui você pode ser livre para criar contas, testar, fazer postagens e tudo mais!')

st.subheader('Onde começar?')
st.caption('O primeiro passo para entrar no NeutrumSocial é criar um nome de usuário e uma senha. Você pode fazer isso clicando no botão abaixo')

if st.button(':material/login: Criar conta ou fazer meu cadastro'):
    st.switch_page('pages/login.py')
