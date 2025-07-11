import streamlit as st
from datetime import datetime
import requests

st.set_page_config(
    page_title = 'Registrador de Humor',
    page_icon = '😃',
    layout = 'wide'
)

st.markdown("""
<style>
    #MainMenu, footer, header {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html = True)

with st.sidebar:
    st.title('Bem-vindo ao Registrador de Humor')
    st.divider()


    st.badge('Guia', color='blue', icon='🌀')
    st.caption('Escreva como foi seu dia em geral e principalmente o seu humor. Selecione a cor correspondente, que indica seu nível de humor')

    st.badge('Registros', color='red', icon='🍁')
    st.caption('Para acessar seus registros de humor, todos eles são armazenados no banco de dados do MockAPI. Você pode acessar todos eles clicando neste botão abaixo')
    st.link_button('Ver meus registros de Humor', url='https://mockapi.io/projects/6855ff071789e182b37cd43e#')


with st.form('Formulário de Humor'):
    col1, col2 = st.columns([1, 1])

    with col1:
        conteudo = st.text_area('Como foi seu dia e seu humor?')
        if conteudo == '':
            st.warning('Preencha todos os campos', icon='❌')

    with col2:
        with st.expander('Selecionar o seu Humor'):
            humor = st.selectbox('Selecione a cor com seu humor correspondente', options=['Azul - INCRÍVEL', 'Verde - Muito bom', 'Amarelo - Legal', 'Laranja - Ruim', 'Vermelho - HORRÍVEL'])


    horario = datetime.now().strftime('%d/%m/%Y às %H:%M:%S')

    data = {
        'horario': horario,
        'conteudo': conteudo,
        'humor': humor
    }


    submit = st.form_submit_button('Enviar')
    if submit:
        send_data = requests.post('https://6855ff071789e182b37cd43d.mockapi.io/api/Humor', json=data)
        if send_data.ok:
            st.badge('Dados Enviados com sucesso', color='green', icon='✅')
        else:
            st.warning('Oops! algum erro. Tente novamente mais tarde.')
            st.badge(f'Código de resposta: {send_data}', color='red', icon='💫')


ids = requests.get('https://6855ff071789e182b37cd43d.mockapi.io/api/Humor').json()
if len(ids) > 0 and submit:

    horario_list = []
    conteudo_list = []
    humor_list = []

    for id in ids:
        for chave, item in id.items():
            if 'horario' in chave:
                horario_list.append(item)
            elif 'conteudo' in chave:
                conteudo_list.append(item)
            elif 'humor' in chave:
                humor_list.append(item)



    lista = st.tabs(horario_list, width=570)

    for item in lista:
        with item:
            index = lista.index(item)
            st.write(conteudo_list[index])
            st.write(humor_list[index])
