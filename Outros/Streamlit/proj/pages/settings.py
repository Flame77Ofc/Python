import streamlit as st
from assets.css.no_login_centralized import set_style
import json
import requests
import os
from time import sleep


recharge = False
try:
    with open('./data/login.json', 'r') as arquivo: pass
    st.title(':material/build: Configurações')

    with st.popover(":material/info: Sobre", use_container_width=True):
        pass

    with st.popover(":material/logout: Sair", use_container_width=True):
        st.caption("Caso você deseja sair, precisará entrar novamente para acessar sua conta. Isso não irá apagar seus dados, nem deletará a sua conta.")

        if st.button("Sair", use_container_width=True):
            with st.spinner("Saindo..."):
                sleep(2)

            with open('./data/login.json', 'r') as arquivo:
                username = json.load(arquivo)
                username = username['user']['username']


            arquivos = ['./data/follow.json', './data/login.json', './data/user-birth.json', './data/user-description.json', './data/user-image.png', './data/user-lastname.json', './data/user-name.json']

            for arquivo in arquivos:
                try:
                    os.remove(arquivo)
                except:
                    pass

            recharge = True



    with st.popover(":material/no_accounts: Deletar Conta", use_container_width=True):
        st.caption("Atenção: Esta ação é irreversível e apagará todos os seus dados.")

        verify = st.text_input("Digite sua senha para confirmar a exclusão da conta", type="password")

        with open('./data/login.json', 'r') as arquivo:
            password = json.load(arquivo)
            password = password['user']['password']

        if st.button("Deletar Conta", use_container_width=True):
            if verify == password:
                with st.spinner("Deletando conta..."):
                    sleep(2)

                with open('./data/login.json', 'r') as arquivo:
                    username = json.load(arquivo)
                    username = username['user']['username']


                arquivos = ['./data/follow.json', './data/login.json', './data/user-birth.json', './data/user-description.json', './data/user-image.png', './data/user-lastname.json', './data/user-name.json', './data/welcome-data.txt']

                for arquivo in arquivos:
                    try:
                        os.remove(arquivo)
                    except:
                        pass
                            #  https://neutrumsocial1-default-rtdb.firebaseio.com/FlameOFC
                DATABASE = f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/.json"
                r = requests.delete(DATABASE)

                st.success("Conta deletada com sucesso!")
                recharge = True

            else:
                st.error("Senha incorreta.")


except:
    set_style(True, True, True)

    st.title('👀 Pronto para ver o que ninguêm vê?')
    st.caption('Vamos explorar as configurações - Uma selva de funcionalidades!')

    if st.button(':material/login: Criar conta ou Entrar'):
        st.switch_page('pages/welcome.py')

if recharge:
    st.switch_page("pages/initial.py")