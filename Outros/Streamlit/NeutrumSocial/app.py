import streamlit as st
import requests
import json


st.set_page_config(
    page_title="NeutrumSocial",
    page_icon="assets/image/icon.png",
    layout="wide"
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
    "🏠 Principal": [
        st.Page("pages/initial.py", title="Início", icon=":material/home:"),
        st.Page("pages/search.py", title="Pesquisar", icon=":material/search:"),
        st.Page("pages/create.py", title="Post", icon=":material/publish:")
    ],

    "💬 Chat": [

    ],

    "🌵 Outros": [
        st.Page("pages/person.py", title="Perfil", icon=":material/account_circle:"),
        st.Page("pages/settings.py", title="Configurações", icon=":material/settings:")
    ],
}

try:
    with open('./data/login.json', 'r') as arquivo: 
        pass
except:
    pages["🥏 Primeiros Passos"] = st.Page("pages/welcome.py", title="Bem-vindo", icon=":material/emoji_people:"),

### Chat
try:
    with open("./data/login.json", 'r', encoding="utf-8") as arquivo:
        username = json.load(arquivo)["user"]["username"]

    # Coletando os seguindo e os seguidores
    seguindo = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/status/lista_seguindo/.json").json()

    seguidores = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/{username}/status/lista_seguidores/.json").json()
    lista = set()

    # Adicionando cada na lista (set)
    for seguindo in seguindo:
        lista.add(seguindo)

    for seguidor in seguidores:
        lista.add(seguidor)

    lista.remove("None")
    lista = list(lista)

    if len(lista) == 0:
        pass
    else:
        # Criando os arquivos para cada seguindo/seguidor da lista.
        for user in lista:
            try:
                with open(f"pages/friends/{user}.py", "r") as arquivo: pass
            except:
                with open(f"pages/friends/{user}.py", "w", encoding='utf-8') as arquivo:
                    arquivo.write(f'''import streamlit as st
import requests
import json

me = "{username}"
friend = "{user}"

letra = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$me!/chat/$friend!/letra/.json").json()
main = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$me!/chat/$friend!/main/.json").json()
sec = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$me!/chat/$friend!/sec/.json").json()

with open("./data/login.json", "r") as arquivo:
    username = json.load(arquivo)["user"]["username"]

mensagens = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$me!/chat/$friend!/.json").json()
for i, mensagem in mensagens.items():
    if mensagem == "None" or (i == "letra" and mensagem == "a") or (i == "letra" and mensagem == "b") or (i == "main" and mensagem == me) or (i == "main" and mensagem == friend):
        pass
    else:

        if i[0] == "a":
            if me == main:
                with st.chat_message("user", avatar=":material/mood:"):
                    st.caption(f":green[$main!]")
                    st.write(mensagem)
            else:
                with st.chat_message("user", avatar=":material/account_circle:"):
                    st.caption(f":blue[Eu $sec!]")
                    st.write(mensagem)
        else:
            if me == main:
                with st.chat_message("user", avatar=":material/account_circle:"):
                    st.caption(f":blue[Eu $me!]")
                    st.write(mensagem)
            else:
                with st.chat_message("user", avatar=":material/mood:"):
                    st.caption(f":green[Amigo $friend!]")
                    st.write(mensagem)


enviar_mensagem = st.chat_input("Digite sua mensagem")

if enviar_mensagem:
    with st.spinner("Enviado Mensagem, aguarde..."):
        # Enviando a mensagem para o banco de dados
        r = requests.get(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$me!/chat/$friend!/.json").json()

        pessoa_a = f"a$[sum(pessoa[0].count('a') for pessoa, _ in r.items() if pessoa[0] == 'a')][0] + 1!"
        pessoa_b = f"b$[sum(pessoa[0].count('b') for pessoa, _ in r.items() if pessoa[0] == 'b')][0] + 1!"

        if letra == "a":
            data = $
                pessoa_a: enviar_mensagem
            !
        else:
            data = $
                pessoa_b: enviar_mensagem
            !

        r = requests.patch(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$me!/chat/$friend!/.json", json=data)
        r = requests.patch(f"https://neutrumsocial1-default-rtdb.firebaseio.com/$friend!/chat/$me!/.json", json=data)

        st.rerun()
'''.replace("$", "{").replace("!", "}"))

            pages["💬 Chat"].append(st.Page(f"pages/friends/{user}.py", title=user, icon=":material/mood:"))

except:
    pass


pg = st.navigation(pages)
pg.run()
