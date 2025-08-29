import streamlit as st
from random import choice


def boas_vindas():
    """Função de boas-vindas com efeitos visuais"""
    st.balloons()

    notificacoes = [
        "🎉 Que bom te ver aqui! Bem-vindo!!!",
        "📖 Ebaa! Fique à vontade para a leitura dos Blogs!",
        "🤗 Mais um amigo! Yuuupiii!! Seja Bem-Vindo!",
        "🧭 Mais um explorador de leitura! Venha se aventurar!",
        "🔎 Analisando...\n Uau! Você lê muito bem! Que tal mergulhar nos nossos blogs?"
    ]
    st.toast(choice(notificacoes), icon="✨")



def arquivo_nome():
    """Verifica e coleta o nome do usuário.
    Caso não exista, pede o nome e salva num arquivo."""

    try:  # Tenta abrir o arquivo com nome
        with open("database/name.txt", "r", encoding="utf-8") as f:
            nome = f.read().strip()

        st.title(f"👋 Bem-Vindo(a), {nome}!")
    except:  # Se não existir, cria o arquivo
        with st.empty():
            nome = st.text_input("Informe o seu nome!", placeholder="Como posso te chamar?")

            if nome:
                with open("database/name.txt", "w", encoding="utf-8") as f:
                    f.write(str(nome))

                st.success("✅ Nome salvo com sucesso!")
                st.title(f"👋 Bem-Vindo(a), {nome}!")


def sobre_blog():
    # Introdução
    st.caption("✨ Aqui você encontrará dicas de **Segurança**, **Hacking Ético**, **Curiosidades sobre o Universo**, **Filosofia**, **Ciência** e muito mais. Explore esta página cheia de conhecimentos! 🚀")

    st.divider()

    # Sobre o blog
    st.subheader("📌 Sobre este Blog")
    st.info("Este é um espaço para **aprender, compartilhar e se inspirar** em diferentes áreas do conhecimento!")

    # Lista de assuntos do blog
    st.markdown("""
    ### 🔎 O que você vai encontrar aqui:
    - ✅ **Dicas do Dia-a-Dia**
    - 🛡️ **Ciber Segurança e Hacking**
        - Segurança Digital  
        - Scripts Maliciosos  
        - Resumo de Fóruns e Notícias  
        - Roadmap Completo de Hacking  
    - 🧑‍💻 **Tecnologia**
        - Programação, Automação e Inteligência Artificial  
        - Curiosidades e notícias do mundo Tech  
    - 🌌 **Ciência**
        - Astronomia, Física e descobertas recentes  
        - Filosofia e reflexões científicas  
    - 📚 **E muito mais...**
    """)

    st.divider()

    # Motivo do Blog
    st.subheader("💡 Por que este blog existe?")
    st.write("""
    Criamos este espaço com o objetivo de **compartilhar conhecimento de forma simples, prática e acessível**.  
    Aqui você encontrará **inspiração**, **conteúdos úteis** e uma comunidade de pessoas curiosas sobre o mundo da tecnologia, ciência e segurança.  
    """)

    st.divider()

    # Público do Blog
    st.subheader("👥 Para quem é este blog?")
    st.markdown("""
    - Estudantes e curiosos sobre **Segurança da Informação**  
    - Entusiastas de **Tecnologia e Programação**  
    - Amantes da **Ciência e Astronomia**  
    - Pessoas que desejam **aprender algo novo todos os dias**  
    """)

    st.divider()

    # Convite para leitura
    st.success("🚀 Explore o menu lateral para navegar pelas páginas do blog!")
    st.badge("🔖 Os blogs, configurações e outras seções estão disponíveis na **barra lateral**.", color="blue")



def main():
    boas_vindas()
    arquivo_nome()

    with st.container(border=True):
        sobre_blog()


main()
