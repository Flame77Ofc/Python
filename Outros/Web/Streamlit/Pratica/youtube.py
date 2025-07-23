import streamlit as st
import pandas as pd

st.set_page_config(
    page_title = 'Canal do FlameTube',
    page_icon = '📺',
    layout = 'wide'
)

st.markdown("""
<style>
    #MainMenu, header, footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html = True) # Esconder as configurações para não perder o costume e aprender

with st.sidebar:
    st.subheader('Vídeos em ALTA🔥')
    st.markdown("""
- [Vídeo 1](https://www.youtube.com)
- [Vídeo 2](https://www.youtube.com)
- [Vídeo 3](https://www.youtube.com)
""")

    st.link_button('Ir às configurações', url='#')

col1, col2 = st.columns([2, 5])

with col1:
    st.image('https://cdn.awsli.com.br/2616/2616870/favicon/perfil-1logo-redonda-site-5jcwke106n.ico', width=250, caption='Flame👑')

with col2:
    estatisticas = pd.Series({
        'Canal': 'Flame👑',
        'Usuário': 'FlameOFC',
        'Inscritos': 665743,
        'Vídeos': 56,
        'Descrição': 'Gosto de Hacking, Programação, Ciência, Astronomia, Filosofia. Apaixonado por aprender! ❤',
    })

    estatisticas['Usuário'] = f'@{estatisticas['Usuário']}' # Adicionando o @ no Usuário (Como se fosse uma coisa automatizada)
    with st.expander('Ver informações do canal'):
        st.write(estatisticas)

        st.link_button('Entrar em contanto', url='FlameOFC@mail.com')

    
    if st.button('Se inscrever'):
        st.write('Agora você é um inscrito de Flame👑')
        st.balloons()
