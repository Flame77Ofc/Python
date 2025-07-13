# Organizador de tarefas (To-Do list)

"""
Não utilizarei session_state. Ao invés disso, optarei por arquivos: Garantindo que mesmo após o usuário sair, seus dados permanecerem
"""

import streamlit as st

st.set_page_config(
    page_title = "To-do List",
    page_icon = "✔",
    layout = "wide"
)

with st.sidebar:
    st.title("To-do List")

    st.divider()

    st.caption('Navegação')
    st.badge("Início", icon='🏠')


    st.divider()

    st.badge("Guia", color="red", icon="🍁")
    st.caption("...")

