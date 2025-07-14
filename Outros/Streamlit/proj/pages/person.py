import streamlit as st
import json
from assets.css.no_login_centralized import set_style

st.markdown('''
<style>
    h4#nome-de-usuario, h4#senha, h4#nome, h4#sobrenome {
        margin: 0;
        padding: 0;
    }

    button[data-testid="stPopoverButton"] {
        margin: 10px 0}
</style>
''', unsafe_allow_html=True)

try:
    set_style(False, False, True)
    with open('./data/login.json', 'r') as arquivo:
        pass

except:
    set_style(True, True, True)

    st.title('🌞 Vamos deixar nosso perfil bonito!')
    st.caption('Que tal decorar o perfil com descrição e informações pessoais?')

    if st.button(':material/login: Criar conta ou Entrar'):
        st.switch_page('pages/welcome.py')

with st.container(border=True):
    st.title('Meu Perfil')

    col1, col2 = st.columns([1, 1])

    with col1:
        st.write('#### Nome de usuário')
        with open('./data/login.json', 'r') as arquivo:
            username = json.load(arquivo)
            username = username["user"][0]
        st.caption(username)

        st.write('#### Senha')
        with open('./data/login.json', 'r') as arquivo:
            password = json.load(arquivo)
            password = password["user"][1]
        with st.popover("Revelar", icon='👀'):
            st.caption(password)

        st.write("#### Nome")
        try: 
            with open('./data/user-name.json', 'r', encoding='utf-8') as arquivo: 
                name = json.load(arquivo)
            st.caption(name["nome"])
        except:
            with st.empty():
                name = st.text_input("Coloque seu nome")

                if name:
                    data = {
                        "nome": name
                    }
                    with open('./data/user-name.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(data, arquivo, indent=4)
                    st.caption(name)

        st.write("#### Sobrenome")
        try:
            with open('./data/user-username.json', 'r', encoding='utf-8') as arquivo: 
                username = json.load(arquivo)
            st.caption(username["nome"])
        except:
            with st.empty():
                username = st.text_input("Coloque seu sobrenome")

                if username:
                    data = {
                        "nome": username
                    }
                    with open('./data/user-username.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(data, arquivo, indent=4)
                    st.caption(username)


    with col2:
        try:
            if open(f'./data/user-image.png'):
                st.image(f'./data/user-image.png', width=200, caption="Foto de Perfil")
        except:
            with st.empty():
                image = st.file_uploader("Imagem", type=["png"], accept_multiple_files=False)

                if image:
                    st.image(image, width=200, caption="Foto de Perfil")

                    try: open(f"./data/user-image.png", "x").close()
                    except: pass

                    with open("./data/user-image.png", 'wb') as f:
                        f.write(image.read())

