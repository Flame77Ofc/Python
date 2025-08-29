import streamlit as st

### 1. Configuração da Página
st.set_page_config(page_title="Título") # Define o título da aba do navegador
st.sidebar # Acessa a barra lateral (sidebar)


### 2. Títulos, Textos e Marcação
st.title("Texto") # Título principal
st.write("Texto" ) # Escreve qualquer conteúdo (texto, número, lista, etc.)
st.markdown("**Negrito**") # Formatação com Markdown
st.text_area("Label") # Caixa de texto grande (várias linhas)
st.caption("Texto") # Escreve um texto pequeno


### 3. Inputs e Interações
st.text_input("Label") # Entrada de texto
st.number_input("Label") # Entrada de número
st.slider("Label") # Barra deslizante
st.date_input("Label") # Seleciona uma data
st.time_input("Label") # Seleciona um horário
st.checkbox("Opção") # Caixa de seleção
st.radio("Pergunta", options=[...]) # Uma escolha entre várias
st.selectbox("Pergunta", options=[...]) # Menu suspenso com uma opção
st.multiselect("Pergunta", options=[...]) # Menu suspenso com múltiplas opções
st.button("Texto")# Botão comum
st.link_button("Texto", url="link") # Botão com link embutido
st.pills('Selecione uma das opções', options=['opção 1', 'opção 2', 'opção 3'])
with st.popover("Mais informações"):
    st.write("Texto")




### 4. Feedback e Mensagens ao Usuário
st.success("Texto") # Mensagem de sucesso (verde)
st.warning("Texto") # Alerta (amarelo)
st.error("Texto") # Erro (vermelho)
st.info("Texto") # Informação (azul)
st.toast("Texto") # Notificação discreta
st.spinner("Mensagem") # Mensagem de carregamento com animação 


### 5. Imagens, Mídias e Arquivos
# st.image("imagem.png") # Mostra imagem
# st.logo("logo.png")# Mostra logotipo
# st.video("video.mp4")# Mostra um vídeo
# st.audio("audio.mp3")# Reproduz um áudio 


### 6. Layout e Organização
st.columns([1, 1])# Divide a página em colunas
st.expander("Texto")# Área expansível
st.divider()# Linha divisória
st.tabs(["Tab1", "Tab2"])# Abas de navegação
st.badge("Texto", icon='✅')# Badge/etiqueta com ícone e cor
st.progress(text="Texto", value=50)# Barra de progresso alternativa para o slider
with st.container(border=True):
    st.write("Contâiner")



# Efeitos
st.snow()# Efeito de neve caindo 
st.balloons() # Solta balões na tela


# Páginas
pages = st.navigation([
    st.Page("pagina.py", title="Página Principal", icon="⛄"),
    st.Page("second.py", title="Página Secundária", icon="🚩")
])
