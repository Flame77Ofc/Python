import streamlit as st

def main():
    st.balloons()

    try:
        with open("database/name.txt", "r", encoding="utf-8") as f:
            f.seek(0)
            nome = f.read()

        st.title(f"Bem-Vindo(a), {nome}!")
    except:
        with st.empty():
            nome = st.text_input("Informe o seu nome!", placeholder="Como posso te chamar?")

            if nome:
                with open("database/name.txt", "w", encoding="utf-8") as f:
                    f.write(str(nome))

                st.title(f"Bem-Vindo(a), {nome}!")

    # Introdução
    st.caption("Aqui você encontrará dicas de Segurança, Hacking Ético, Curiosidades sobre o Universo, Filosofia, Ciência e muito mais. Venha explorar essa página cheia de conhecimentos!")

    st.divider()

    # Sobre o blog
    st.subheader("📌 Mas do que se trata este blog?")
    st.caption("Aqui estão alguns assuntos que este blog oferece:")

    # Lista
    st.markdown("""
    - ✅ **Dicas do Dia-a-Dia**
    - 🛡️ **Ciber Segurança e Hacking**
        - Segurança Digital
        - Scripts Maliciosos
        - Resumo de Fóruns e Notícias
        - Roadmap Completo de Hacking
    - 🧑‍💻 **Tecnologia**
        - Curiosidades e notícias do mundo Tech
        - Programação, Automação e IA
    - 🌌 **Ciência**
        - Astronomia, Física e descobertas recentes
        - Filosofia e reflexões científicas
    - 📚 **Entre Outros...**
    """)

    st.divider()

    # Motivação
    st.subheader("💡 Por que criar este blog?")
    st.write("""
    Este espaço foi criado com o objetivo de **compartilhar conhecimento** de forma simples e acessível.
    Aqui você encontrará **inspiração**, **conteúdos práticos** e uma comunidade de pessoas curiosas 
    sobre segurança, ciência e tecnologia.
    """)

    st.info("🔎 O aprendizado só é verdadeiro quando é compartilhado.")

    st.divider()

    # Público alvo
    st.subheader("👥 Para quem é este blog?")
    st.markdown("""
    - Estudantes e curiosos sobre **Segurança da Informação**  
    - Entusiastas de **Tecnologia e Programação**  
    - Amantes da **Ciência e Astronomia**  
    - Qualquer pessoa que deseja **aprender algo novo todos os dias**  
    """)

    st.divider()

    # Chamado para ação
    st.success("Os blogs estão disponíveis na barra lateral 👉 Boa leitura e exploração! 🚀")

main()
