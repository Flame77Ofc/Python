import streamlit as st

st.set_page_config(
    page_title = "NeutrumSocial",
    page_icon = "assets/image/planet_5566471.png",
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

</style>
</head>''', unsafe_allow_html=True)



pages = {
    "🥏 Primeiros Passos": [
        st.Page("pages/welcome.py", title=f"Bem-vindo", icon=":material/emoji_people:"),
    ],

    "🏠 Principal": [
        st.Page("pages/initial.py", title=f"Início", icon=":material/home:"),
        st.Page("pages/search.py", title=f"Pesquisar", icon=":material/search:"),
        st.Page("pages/create.py", title=f"Post", icon=":material/publish:")
    ],

    "🌾 Secundário": [
        st.Page("pages/login.py", title=f"Login/Cadastrar", icon=":material/login:"),
        st.Page("pages/messages.py", title=f"Mensagens", icon=":material/message:"),
        st.Page("pages/notifications.py", title=f"Notificações", icon=":material/notifications:")
    ],

    "🌵 Outros": [
        st.Page("pages/person.py", title=f"Perfil", icon=":material/account_circle:"),
        st.Page("pages/settings.py", title=f"Configurações", icon=":material/settings:")
    ]
}

pg = st.navigation(pages)
pg.run()
