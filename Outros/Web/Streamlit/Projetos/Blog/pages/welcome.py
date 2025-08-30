import streamlit as st
from time import sleep
from random import choice

def boas_vindas():
    st.balloons()

    notificacoes = ["Hmmm... Você parece ser um bom leitor! Que tal mergulhar nos Blogs??", "Yuupii! Mais um amigo! Bora ler?", "Que tal ler os Blogs e ficar mais inteligente??", "Que bom te ver aqui! Partiu ler Blogs?", "Você sabia que a leitura é um dos melhores hábitos da atualidade?", "Quer ler? Veio ao lugar certo! Seja bem-vindo."]
    icones = ["🎗️", "☃️", "🪄", "🎈", "👑"]

    st.toast(choice(notificacoes), icon=choice(icones))


def sobre_blog():
    """Função que diz sobre o Blog"""

    st.title("Bem-Vindo!!!")

    st.caption("É muito bom te ver aqui! Nessa plataforma, você poderá ler (e criar) diversos posts de qualquer assunto que desejar. Aqui a criatividade e a imaginação andam de mãos dadas, unindo-se as duas maiores forças do ser humano. Você pode ser livre nessa plataforma e compartilhar seus aprendizados com diversas pessoas. Então, vamos começar.")

    # Motivo da Criação do Blog
    st.subheader("Por que este Blog foi criado?")
    st.caption("Fazer um blog utilizando `python` com `streamlit` é muito divertido e desafiador. Criando este blog, aplico meus conhecimentos de `streamlit` em prática, compartilho mais conhecimento e me preparo para projetos profissionais, entre outros benefícios.")

    # Assuntos do Blog
    st.subheader("Quais assuntos constituem estes Blogs?")
    st.caption("Como já disse anteriormente, neste blog haverá qualquer tipo de assunto, a única limitação é sua imaginação e criatividade, então, já sabe, né? Se prepara com algumas doses de criatividade e imaginação e vamos nos aventurar na leitura e criação destes blogs!")

    # Explicação do Blog
    st.subheader("Como começo a leitura?")
    st.caption("Você pode começar a ler este blog pela barra lateral na esquerda. Lá há algumas seções e algumas páginas, separadas de acordo com seu propósito.")

    st.title("[...]")

    st.subheader(":rainbow[Você pode começar aqui]")
    criar_blog = st.button("Criar um Blog", use_container_width=True)
    if criar_blog:
        st.switch_page("pages/create.py")

    configuracoes = st.button("Ir em Configurações", use_container_width=True)
    if configuracoes:
        st.switch_page("pages/settings.py")




def main():
    boas_vindas()
    sobre_blog()


main()
