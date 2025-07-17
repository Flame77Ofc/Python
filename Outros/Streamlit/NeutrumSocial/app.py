import streamlit as st
import requests
import json


st.set_page_config(
    page_title = "NeutrumSocial",
    page_icon = "assets/image/icon.png",
    layout = "wide"
)

st.markdown('''<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300..700&display=swap" rel="stylesheet">
<style>
    #MainMenu, footer, .st-emotion-cache-1gwi02i {
        visibility: hidden;
    }

    * {
        font-family: "Space Grotesk", sans-serif;
    }

    .st-emotion-cache-1pru02b {
        font-size: 0.9em;
        font-weight: 900;
        color: grey;
    }

    .e16b601d6 {
        font-weight: 700;
        color: #d6d6d6;
    }

    .rc-overflow-item {
        padding: 5px;
    }

    span[data-testid="stIconMaterial"] {
        color: #add1ff;
    }
</style>
</head>''', unsafe_allow_html=True)


pages = {
    # "🥏 Primeiros Passos": [
    #     st.Page("pages/welcome.py", title=f"Bem-vindo", icon=":material/emoji_people:"),
    # ],

    "🏠 Principal": [
        st.Page("pages/initial.py", title=f"Início", icon=":material/home:"),
        st.Page("pages/search.py", title=f"Pesquisar", icon=":material/search:"),
        st.Page("pages/create.py", title=f"Post", icon=":material/publish:")
    ],

    "💬 Chat": [
        # st.Page("pages/messages.py", title=f"Chat e Amigos", icon=':material/message:'),
        # st.Page("pages/notifications.py", title=f"Notificações", icon=":material/notifications:")
    ],

    "🌵 Outros": [
        st.Page("pages/person.py", title=f"Perfil", icon=":material/account_circle:"),
        st.Page("pages/settings.py", title=f"Configurações", icon=":material/settings:")
    ],
}

try:
    with open('./data/login.json', 'r') as arquivo: pass
except:
    pages["🥏 Primeiros Passos"] = st.Page("pages/welcome.py", title=f"Bem-vindo", icon=":material/emoji_people:"),


























try:
    with open('./data/login.json', 'r') as arquivo:
        username = json.load(arquivo)['user']['username']

    # Cria a conexão com o banco de dados
    DATABASE = f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/status/.json"
    r = requests.get(DATABASE)
    json_data = r.json()

    # Coleta o usuários que você segue e os que te seguem
    seguidores = json_data['lista_seguidores']
    seguindo = json_data['lista_seguindo']

    # Cria um set com os seguidores e os seguindo, evitando que não tenha repetições de usuários
    lista = set()
    for seguidor in seguidores:
        lista.add(seguidor)

    for seguindo in seguindo:
        lista.add(seguindo)

    lista.remove("None") # Remove o None que é padrão para não dar erros
    lista = list(lista) # Transforma em lista


    DATABASE = "https://neutrumsocial1-default-rtdb.firebaseio.com/.json"
    r = requests.get(DATABASE)

    for user in lista:
        try:
            with open(f"pages/friends/{user}.py", "r", encoding='utf-8') as f: pass
        except:
            with open(f"pages/friends/{user}.py", "w", encoding='utf-8') as f:
                f.write(f'import streamlit as st\n\nfriend = "{user}"')
        pages["💬 Chat"].append(st.Page(f"pages/friends/{user}.py", title=user))

except:
    pass

pg = st.navigation(pages)
pg.run()