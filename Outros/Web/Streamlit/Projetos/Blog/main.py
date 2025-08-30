import streamlit as st
from config import configset

configset.main()


def set_pages():
    """Configura as páginas do Blog"""

    pages = {
    "🏠 Início": [
        st.Page("pages/welcome.py", title="Bem-vindo", icon="☃️")
    ],

    "🪄 Criação e Remoção": [
        st.Page("pages/create.py", title="Criar Blog", icon="✨"),
        st.Page("pages/remove.py", title="Remover Blog", icon="🗑️")
    ],

    "📱 Sistema": [
        st.Page("pages/settings.py", title="Configurações", icon="⚙️"),
        st.Page("pages/about.py", title="Sobre", icon="🗨️")
    ],

    # "🗒️ Blogs": [
    #     # code...
    # ]
    }


    # pages["🗒️ Blogs"].append(st.Page("pages/teste.py", title="asasasdadasdasd", icon="⚙️"))


    pg = st.navigation(pages=pages)
    pg.run()


def main():
    set_pages()


main()
