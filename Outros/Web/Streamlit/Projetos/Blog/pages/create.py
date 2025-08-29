import streamlit as st
from database.pages import retorna_nova_pagina
from time import sleep


def criacao_blog():
    st.title("Criação de Posts")

    with st.form("Blog Post"):
        # Campo de título
        titulo = st.text_input("Digite o título do Blog", placeholder="Título")
        if titulo == "":
            st.warning("Por favor, preencha o campo de título.")

        # Campo de conteúdo
        conteudo = st.text_area("Digite o conteúdo do Blog", placeholder="Conteúdo")
        if conteudo == "":
            st.warning("Por favor, preencha o campo de conteúdo.")

        # Verificação
        enviar = st.form_submit_button("Enviar dados")
        if enviar and titulo != "" and conteudo != "":
            # Envio de dados
            nova_pagina = retorna_nova_pagina()
            with open(f"{nova_pagina}", "w", encoding="utf-8") as f:
                f.write(f"""import streamlit as st

with st.container(border=True):
    st.title("{titulo}")

    st.divider()

    st.caption("{conteudo}")
""")

            st.success("Dados Enviados com Sucesso!")
            with st.spinner("Carregando..."):
                st.toast("Página criada com sucesso!", icon="✅")
                st.toast("Recarregando a página!", icon="🔁")
                sleep(5)

                st.rerun()


def main():
    criacao_blog()


main()
