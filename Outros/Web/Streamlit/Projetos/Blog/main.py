import streamlit as st
from config import settings
from assets.css import css

settings.page_config()


pages = {
    "🏠 Início": [
        st.Page("pages/welcome.py", title="Bem-Vindo", icon="🎉")
    ],

    "🪄 Criação": [
        st.Page("pages/create.py", title="Criar Post", icon="🎁")
    ],

    "🔧 Sistema": [
        st.Page("pages/config.py", title="Configurações", icon="⚙️")
    ],

    "🗒️ Blogs": [
        # code
    ]
}

for i in range(1, 10):
    try:
        pages["🗒️ Blogs"].append(st.Page(f"pages/blogs/blog00{i}.py", title=f"Blog00{i}", icon=":material/mood:"))
    except:
        pass


navigation = st.navigation(pages)
navigation.run()
