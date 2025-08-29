import streamlit as st
from database.pages import verifica_paginas
from config import settings

settings.page_config()


pages = {
    "🏠 Início": [
        st.Page("pages/welcome.py", title="Bem-Vindo", icon="🎉")
    ],

    "🪄 Criação": [
        st.Page("pages/create.py", title="Criar Post", icon="✨"),
    ],

    "🔧 Sistema": [
        st.Page("pages/config.py", title="Configurações", icon="⚙️")
    ],

    "🗒️ Blogs": [
        # code
    ]
}


try:
    for pagina in verifica_paginas():
        numero_pagina = pagina[-6:-3]
        pages["🗒️ Blogs"].append(st.Page(f"{pagina}", title=f"Blog{numero_pagina}", icon="📃"))
except:
    pass


navigation = st.navigation(pages)
navigation.run()
