# import streamlit as st
# from datetime import datetime
# import requests

# st.set_page_config(
#     page_title = 'Registrador de Humor',
#     page_icon = '😃',
#     layout = 'wide'
# )

# st.markdown("""
# <style>
#     #MainMenu, footer, header {
#         visibility: hidden;
#     }
# </style>
# """, unsafe_allow_html = True)

# with st.sidebar:
#     st.title('Bem-vindo ao Registrador de Humor')
#     st.divider()


#     st.badge('Guia', color='blue', icon='🌀')
#     st.caption('Escreva como foi seu dia em geral e principalmente o seu humor. Selecione a cor correspondente, que indica seu nível de humor')

#     st.badge('Registros', color='red', icon='🍁')
#     st.caption('Para acessar seus registros de humor, todos eles são armazenados no banco de dados do MockAPI. Você pode acessar todos eles clicando neste botão abaixo')
#     st.link_button('Ver meus registros de Humor', url='https://mockapi.io/projects/6855ff071789e182b37cd43e#')


# with st.form('Formulário de Humor'):
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         conteudo = st.text_area('Como foi seu dia e seu humor?')
#         if conteudo == '':
#             st.warning('Preencha todos os campos', icon='❌')

#     with col2:
#         with st.expander('Selecionar o seu Humor'):
#             humor = st.selectbox('Selecione a cor com seu humor correspondente', options=['Azul - INCRÍVEL', 'Verde - Muito bom', 'Amarelo - Legal', 'Laranja - Ruim', 'Vermelho - HORRÍVEL'])


#     horario = datetime.now().strftime('%d/%m/%Y às %H:%M:%S')

#     data = {
#         'horario': horario,
#         'conteudo': conteudo,
#         'humor': humor
#     }


#     submit = st.form_submit_button('Enviar')
#     if submit:
#         send_data = requests.post('https://6855ff071789e182b37cd43d.mockapi.io/api/Humor', json=data)
#         if send_data.ok:
#             st.badge('Dados Enviados com sucesso', color='green', icon='✅')
#         else:
#             st.warning('Oops! algum erro. Tente novamente mais tarde.')
#             st.badge(f'Código de resposta: {send_data}', color='red', icon='💫')


# ids = requests.get('https://6855ff071789e182b37cd43d.mockapi.io/api/Humor').json()
# if len(ids) > 0 and submit:

#     horario_list = []
#     conteudo_list = []
#     humor_list = []
#     for id in ids:
#         for chave, item in id.items():
#             if 'horario' in chave:
#                 horario_list.append(item)
#             elif 'conteudo' in chave:
#                 conteudo_list.append(item)
#             elif 'humor' in chave:
#                 humor_list.append(item)



#     item = st.tabs(horario_list, width=570)

#     for v in item:
#         with v:
#             index = item.index(v)
#             st.write(conteudo_list[index])
#             st.write(humor_list[index])




import streamlit as st

st.set_page_config(
    page_title = 'Minha Página',
    page_icon = '🌠',
    layout = 'wide',
)

st.markdown("""<style>
    #MainMenu, footer {
        visibility: hidden;
    }
            
    .hideScrollbar.st-emotion-cache-jx6q2s.e1quxfqw2 {
            # background-color: white;}
            
</style>""", unsafe_allow_html = True)


with st.sidebar:
    st.title('Dashboard')
    st.divider()

    st.badge('Boas-Vindas', color='blue', icon='🐾')
    st.caption('Seja bem-vindo(a) à página do guia do estudante! Aqui você encontrará dicas de estudo, melhores professores, e um bot integrado que busca conteúdos de graça')

    st.divider()

    st.badge('Bot - Busca assuntos', color='violet', icon='🤖')
    st.caption('Você pode facilmente pesquisar aqui um assunto que deseja.')

    assunto = st.text_input('Digite o assunto', placeholder='Assunto')
    if assunto == '':
        st.warning('Preeencha o Campo!')


st.title('Página dos Estudantes')


st.divider()
st.badge('Área de estudos', color = 'red', icon = '🍁')

st.markdown('#### Como estudar melhor e mais efetivamente? ')

st.write('<p style="color: lightgray;">Estudar efetivamente pode ser um desafio para muitos. Se não aplicar as técnicas certas, podem causar muitas frustações. Separamos algumas dicas para render um estudo melhor</p>', unsafe_allow_html = True)

st.write("""<p style="color: lightgray;">Existem diversas técnicas adequadas de estudo para garantir que a forma de aprendizado é eficaz. Vamos conferir:</p>
<h4 style="color: grey;">👨🏻‍🚀 Técnica Feynman</h4>
<p style="color: lightgray">Essa técnica foi criada pelo físico teórico <strong>Richard Feynman</strong>, que recebeu um prêmio Nobel de física. Ele foi responsável por criar uma técnica chamada <strong>Técnica Feynman</strong>. <br> Essa técnica consiste em: <strong>Escolher algum assunto</strong>; <strong>Aplicar na prática</strong>; <strong>Ensinar para alguém</strong>; <strong>Revisar tudo aprendido</strong> <br> Vista com uma técnica poderosa, pode se encaixar perfeitamente em uma nova forma de aprendizado.</p>""", unsafe_allow_html = True)

st.image("https://imgs.search.brave.com/9rKdG51Mfa9QpOhjCfU1uzbZtCRzoJg-q1_6hWUM6p8/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy90/aHVtYi8xLzFhL1Jp/Y2hhcmRGZXlubWFu/LVBhaW5lTWFuc2lv/bldvb2RzMTk4NF9j/b3B5cmlnaHRUYW1p/a29UaGllbF9idy5q/cGcvNTEycHgtUmlj/aGFyZEZleW5tYW4t/UGFpbmVNYW5zaW9u/V29vZHMxOTg0X2Nv/cHlyaWdodFRhbWlr/b1RoaWVsX2J3Lmpw/Zw", caption = "Richard Feynman - Físico Teórico | Criador da Técnica Feynman", width=350)

st.write("""<h4 style="color: grey;">🍅 Técnica Pomodoro</h4>
<p style="color: lightgray">A técnica do pomodoro é muito lembrado por um <strong>tomate</strong>. Essa técnica é incrivelmente boa, muitos estudantes usam isso para aprimorar seus estudos como um machado afiado!🪓 <br> <br> Esta técnica consiste em: <strong>Ficar 25 a 40 minutos de foco total</strong> e <strong>5 a 10 minutos de descanço</strong>, repetindo isso umas 4 ou 5 vezes, dependendo do tempo disponível de pessoa para pessoa. Os valores podem aumentar ou diminuir, e cada estudante pode adaptar para o horário que se sentir melhor, porém o que o pomodoro mais se concentra é em: Foco total e descanço para "fluir melhor o cérebro"</p>""", unsafe_allow_html = True)

st.image("https://www.pontotel.com.br/local/wp-content/uploads/2024/11/tecnica-pomodoro-como-funciona-a-tecnica-pomodoro-funciona-1024x945.webp", caption="Técnica Pomodoro", width=350)



st.write("""<h4 style="color: grey">🃏 FlashCards</h4>""", unsafe_allow_html = True)
st.write("""<p style="color: lightgray;">Considerado uma das melhores técnicas de estudo, os Flashcards são <strong>cartas que apresentam dois lados: Um lado é uma pergunta, e do outro lado (virando a carta) está o significado ou conceito</strong>.Flashcards são algo parecido com a imagem abaixo</p>""", unsafe_allow_html = True)

st.image("https://oaprendizemsaude.wordpress.com/wp-content/uploads/2017/07/sem-tc3adtulo.png?w=660", caption="Esquema de um flashcard", width=350)

st.write("""<p>Os flashcards funcionam por meio de um estudo feito por <strong>Hermann Ebbinghaus</strong>. O estudo de Ebbinghaus mostrou que precisamos relembrar o assunto que estudamos em dias especificos. Por exemplo, se estudei na Segunda-Feira um assunto, os flashcards são feitos para serem estudados: <strong>No mesmo dia do estudo, após 1 dia, após 3 dias, após 1 semana</strong>, etc... <br> Porém, essa regra só serve para aqueles flashcards que você <strong>já dominou</strong>. Se você tem um flashcard, e não soube responder a pergunta antes de virar a carta, então esse flashcard deve ser estudado denovo num tempo mais curto que aquela ordem.""", unsafe_allow_html = True)

st.image("https://upload.wikimedia.org/wikipedia/commons/9/92/Ebbinghaus2.jpg", caption="Hermann Ebbinghaus", width=350)