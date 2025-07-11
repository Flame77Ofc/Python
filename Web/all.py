import streamlit as st

# Definindo as configurações da página
st.set_page_config (
    page_title = "Título da Página",
    page_icon = "Emoji Icon",
    # layout = "wide/centered"
)


# Sidebar: Barra Lateral
with st.sidebar:
    # Comandos
    pass


# Comandos de escrita
st.title("Título")
st.write("Escrita 1"); st.markdown("Escrita 2"); st.caption("Escrita 3")
st.badge("Texto Personalizável", color="red", icon="🍁")


# Interatividade
st.text_input("Input de Texto"); st.text_area("Input de Texto Multilinha")
st.number_input("Input de Número"); st.date_input("Input de Data"); st.time_input("Input de horário")
st.checkbox("Checkbox"); st.radio("Radio", options=["Op1", "Op2"])
st.selectbox("Seleção", options=['Op1', 'Op2']); st.multiselect("Seleção", options=['Op1', 'Op2'])
st.button("Botão"); st.link_button("Link", url="link"); st.download_button("Download", data="arquivo", file_name="teste.txt")


# Mensagens
st.success("Sucesso"); st.warning("Atenção"); st.error("Erro"); st.info("Informação")
st.toast("Notificação")
with st.spinner("Carregando"):
    # Comando de carregamento
    pass


# Layout e Estrutura
col1, col2 = st.columns([1, 1])
with col1: pass # comandos da primeira coluna
with col2: pass # comandos da segunda coluna

with st.expander("Expandidor"):
    # comandos dentro do expandidor
    pass

st.divider()

tab1, tab2 = st.tabs(['Perguntas', 'Respostas'])
with tab1: pass # Comandos do primeiro tab
with tab2: pass # Comandos do segundo tab


# Efeitos
st.balloons(); st.snow()
