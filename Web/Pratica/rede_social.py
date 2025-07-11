import streamlit as st

st.set_page_config(
    page_title = 'Minha rede social',
    layout = 'wide'
)

st.sidebar.title('Painel do Usuário')
st.sidebar.badge('Logado como Flame', icon='🔥', color='red')
st.sidebar.divider()

st.title('Rede Social')
st.subheader('Bem vindo à minha rede social')

st.badge(f'Username: {"Flame"}', color='blue')
col1, col2 = st.columns([1, 5]) # Só pra ficar mais ao lado

with col1:
    st.write(f'Seguidores: {3}') # Colocando chaves para simular uma variável
    st.markdown("""
- jorginho123
- pacocapow2
- jodsonscc
""")

with col2:
    st.write(f'Seguindo: {1}')
    st.markdown("""
- lucas886
""")
