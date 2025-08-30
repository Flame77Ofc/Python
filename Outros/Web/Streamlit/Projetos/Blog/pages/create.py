import streamlit as st
from config import pages
from random import choice


def efeitos_visuais():
    notificacoes = ["Obaa! Bora criar Blogs!", "Um apaixonado pela leitura e conhecimento!", "Olha só! Você é um especialista em leitura??", "Uau! Aposto que você consegue criar Blogs sensacionais!", "Arrasa na criação de Blogs, e compartilhe com seus amgios!", "Seu sobrenome é Blogueiro? Deve ser um expert em criação de Blogs... Crie o seu!"]
    icones = ["🎈", "🎖️", "🎯", "🥏"]

    st.toast(choice(notificacoes), icon=choice(icones))

def criacao_blog():
    st.title("Criação de Blogs")
    st.subheader("[...]")

    with st.container(border=True):
        titulo = st.text_input("Digite o título do Blog", placeholder="Título")
        if titulo == "":
            st.warning("Preencha o campo de título!")

        conteudo = st.text_input("Digite o conteúdo do Blog", placeholder="Conteúdo")
        if conteudo == "":
            st.warning("Preencha o campo de conteúdo!")

        icone = st.text_input("ícone", width=50)
        if len(icone) != 1 and icone.isalnum():
            st.warning("Preencha o campo com apenas um ícone!")

        submit = st.button("Enviar dados")
        if submit:
            if titulo != "" and conteudo != "" and len(icone) == 1 and not icone.isalnum():
                proximo_blog = pages.salvar_proximo_blog()
                with open(f"pages/blogs/{proximo_blog}.py", "w", encoding="utf-8") as f:
                    f.write("""


""")


def main():
    efeitos_visuais()
    criacao_blog()

main()
