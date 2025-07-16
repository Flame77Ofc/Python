import streamlit as st
from assets.css.no_login_centralized import set_style
import json
import requests

try:
    with open('./data/login.json', 'r') as arquivo:
        username = json.load(arquivo)
        username = username["user"]["username"]

    r = requests.get("https://neutrumsocial1-default-rtdb.firebaseio.com/.json")
    json_data = r.json()

    for user in json_data:
        if 'users' == user or username == user: pass
        else:
            DATABASE = f"https://neutrumsocial1-default-rtdb.firebaseio.com/{user}/posts.json"
            r = requests.get(DATABASE)
            json_data = r.json()

            if json_data == ['0']: pass
            else:
                categorias = []
                for chave, valor in json_data.items():
                    with st.container(border=True):
                        st.write(user)
                        st.write(f"## **{chave}**")
                        for chave2, valor2 in valor.items():
                            if chave2 == 'data':
                                st.write(f"📆 {valor2}")
                            elif chave2 == "categoria":
                                for categoria in valor2:
                                    categorias.append(categoria)
                                st.write(f"🏷️: {", ".join(categorias)}")
                            elif chave2 == "descrição":
                                st.write(f"📃 {valor2}")
                            elif chave2 == "imagem":
                                try:
                                    st.image(valor2, width=300)
                                except:
                                    st.caption(f"[*Não foi possível carregar a imagem*]({valor2})")

                st.divider()

except:
    set_style(True, True, True)

    st.title('🚀 Quer começar a sua jornada?')
    st.caption('Para pilotar sua nave, vamos nos conectar!')

    if st.button(':material/login: Criar conta ou Entrar'):
        st.switch_page('pages/welcome.py')
