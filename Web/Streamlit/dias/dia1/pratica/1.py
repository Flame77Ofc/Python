# Nivel 1 (Eu usei um pouco mais do que deveria ok? Fiquei empolgado heheh
# import streamlit as st

# st.set_page_config(
#     page_title = 'Minha rede social',
#     layout = 'wide'
# )

# st.sidebar.title('Painel do Usuário')
# st.sidebar.badge('Logado como Flame', icon='🔥', color='red')
# st.sidebar.divider()

# st.title('Rede Social')
# st.subheader('Bem vindo à minha rede social')

# st.badge(f'Username: {"Flame"}', color='blue')
# col1, col2 = st.columns([1, 5]) # Só pra ficar mais ao lado

# with col1:
#     st.write(f'Seguidores: {3}') # Colocando chaves para simular uma variável
#     st.markdown("""
# - jorginho123
# - pacocapow2
# - jodsonscc
# """)

# with col2:
#     st.write(f'Seguindo: {1}')
#     st.markdown("""
# - lucas886
# """)





# Projeto 2 - Também me empolguei kkkkkkkkkk
# import streamlit as st

# st.set_page_config(
#     page_title = "Terminal Hacker",
#     page_icon = "💻",
#     layout = "centered" # Tem necessidade?
# )

# with st.sidebar:
#     st.title('Comandos disponíveis')
#     st.badge('root acess granted', color='red')

#     st.divider()

# st.title('Hacker\'s page')
# st.write("#### Acesso concedido. Bem-vindo, root.")
# if st.button('Entrar'):
#     st.write('Sua jornada começou....\nBem Vindo!')
#     st.balloons()


# 3 - import streamlit as st

# st.set_page_config(
#     page_title = "Portfólio Profissional",
#     page_icon = '📁',
#     layout = 'wide'
# )

# st.markdown("""
# <style>
#     #MainMenu, footer, header {
#             visibility: hidden;
#     }
# </style>
# """, unsafe_allow_html=True)


# with st.sidebar:
#     st.title('Navegação')
#     st.badge('Página Inicial', color='blue', icon='🚀')
#     st.divider()

#     st.write('## Tenho interesse')
#     st.link_button('Converse comigo!', url='#')

# st.title('Olá, Bem-vindo ao meu portfólio!')
# st.write('## Linguagens que domino: ')

# col1, col2 = st.columns([2, 2])

# with col1:
#     st.caption('Linguagens de programação')
#     st.slider('Python', value = 79, width = 350, disabled = True)
#     st.slider('JavaScript', value = 12, width = 350, disabled = True)

# with col2:
#     st.caption('Linguagem de hypertexto e de estilo')
#     st.slider('HTML', value = 100, width = 350, disabled = True)
#     st.slider('CSS', value = 75, width = 350, disabled = True)

# st.divider()

# st.write('## Projetos')

# st.write("""
# - Jogo da Forca
# - Par ou ímpar
# - Bot que reage a comandos simples
# - Jogo da Velha (Jogando contra bot e 1v1)
# - Projetos de scraping (Pega dados do **mercado livre**, **z-library**, **g1 notícias**, **clima do tempo**, entre outros)
# - Projetos de automação (Entrar em sites como **Instagram**, **entrar em uma partida no chess.com**, **Fazer uma pesquisa no youtube e clicar no primeiro vídeo**, entre outros)
# """)


# st.divider()
# st.write('### Precisando de automação, scraping ou programas de conversão?')
# st.link_button('Entre em contato', url='#')

# 4 - import streamlit as st

# st.markdown("""
# <style>
#     #MainMenu, footer, header {
#         visibility: hidden;
#     }
# </style>
# """, unsafe_allow_html = True)

# st.set_page_config(
#     page_title = 'Configurações do Sistema',
#     page_icon = '⚙',
# )

# with st.sidebar:
#     st.title('Painel lateral')
#     st.badge('Modo avançado ativado', color='violet')

#     st.divider()

#     secret_button = st.link_button('Ativar o MEGA', url='https://pranx.com/hacker/simulador-pt/', icon='🤫')

# st.title('Configurações Gerais')

# st.write('#### Ativar configurações de Game 🎮')
# st.divider()

# col1, col2 = st.columns([1, 1])

# with col1:

#     fps = st.selectbox('Ativar FPS', label_visibility='hidden', options=['30', '60', '90', '120'], width=450)
#     botao = st.button('Aplicar')

#     atual = st.session_state['fps'] = fps
#     st.write(f'FPS agora: {atual}')



# with col2:
#     desempenho = st.toggle('Ativar Desempenho')
#     economia = st.toggle('Ativar economia de Energia')



# import streamlit as st
# import pandas as pd


# st.set_page_config(
#     page_title = 'Loja Flame',
#     page_icon = '🛒'
# )

# with st.sidebar:
#     st.title('Categorias')
#     st.badge('Tecnologia', color='blue', icon='🔌')
#     st.divider()

# st.write('🔥Bem vindo à loja do Flame!')

# with st.expander('Ver produtos'):
#     df = pd.DataFrame({
#         'Produto': ['Notebook', 'Celular', 'Televisão'],
#         'Preço': ['R$3599,99', 'R$2699,99', 'R$1569,99'],
#         'Disponível': [3, 7, 5]
#     })

#     st.write(df)

#     st.divider()

#     st.title('😲 Amei! Quero comprar!')
#     st.link_button('Compre já!', url='https://flame77ofc.github.io/python-tutorial')


# import streamlit as st

# st.set_page_config(
#     page_title = "Nave Flame-X",
#     page_icon = '🚀',
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
#     st.title('Comando da Nave')
#     st.badge('Capitão Flame', color='orange', icon='👨🏻‍🚀')

#     st.divider()

#     with st.expander('### Informações da Nave🌀'):
#         st.slider('Inclinação', value=5, disabled=True)
#         st.write('#### Direção:')
#         st.write('Sentido Norte')
#         st.write('#### Objetivo:')
#         st.write('Ir à lua')

# st.title('👨🏻‍🚀🚀 Flame no comando!')





# import streamlit as st

# st.set_page_config(
#     page_title = 'Área Restrita',
#     page_icon = '🔒',
#     layout = 'centered' # O que faz diferença? kkkkkkkkkkk
# )

# st.markdown("""
# <style>
#     #MainMenu, footer, header {
#             visibility: hidden;
#     }
# </style>
# """, unsafe_allow_html = True)

# with st.sidebar:
#     st.title('Autenticação')
#     st.badge('Acesso necessário', color='red')

#     st.divider()


# st.title('Autenticar uma senha')

# with st.form('Autenticação'):
#     username = st.text_input('Coloque seu nome de usuário', placeholder='Username')
#     password = st.text_input('Coloque a sua senha', placeholder='Password')

#     submit = st.form_submit_button('Entrar/Cadastrar')

#     if submit:
#         if username == '' or password == '':
#             st.warning('Preencha os campos!')
#         else: # Nunca vai comseguir fazer login🤣🤣🤣🤣
#             st.warning('Usuário inexistente, senha incorreta.')





# import streamlit as st

# st.set_page_config(
#     page_title = "Sobre Flame",
#     page_icon = "🧠",
#     layout = "wide"
# )

# st.markdown("""
# <style>
#     #MainMenu, footer, header {
#     visibility: hidden;
# }
# </style>
# """, unsafe_allow_html = True)


# with st.sidebar:
#     st.title('Navegue')
#     st.badge('Início', color='grey', icon='🏠')

# st.title('Flame -> Atual Programador, Futuro Pentester, Engenheiro e Criador de Robôs e Físico')
# st.write('**Interesses**: Robótica, IA, Streamlit, Python, Física, Astronomia, Ciência')




# import streamlit as st
# import pandas as pd

# st.set_page_config(
#     page_title = 'Lanchonete do Flame',
#     page_icon = '🍟',
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
#     st.title('Título')
#     st.badge('Lanches', icon='🍔', color='orange') # Não tem a cor marrom aqui, tá

#     st.divider()


# st.title('Bem-vindo(a) à lanchonete do Flame')
# st.subheader('Cardápio do Dia')

# with st.expander('Ver o Cardápio 😋'):
#     df = pd.DataFrame({
#         'Alimento': ['X-Burguer', 'X-Salada', 'X-Bacon'],
#         'Preço': ['R$14,99', 'R$18,99', '12,00']
#     })

#     st.write(df)

#     st.image('https://www.mundoboaforma.com.br/wp-content/uploads/2020/10/Hamburguer.jpg', width=670, caption='Hambúrguer')

#     st.header('Se interessou?')
#     st.link_button('Entre em contato', url='https://flame77ofc.github.io/python-tutorial')





# import streamlit as st

# st.set_page_config(
#     page_title = 'Perfil do Aluno',
#     page_icon = '🎓',
#     layout = 'centered'
# )

# with st.sidebar:
#     st.title('Menu')
#     st.badge('Área do Estudante', color='blue', icon='👨🏻‍🎓')

#     st.divider()


# st.title('Flame - Estudante')
# aba1, aba2, aba3 = st.tabs(['🎓 Áreas de Interesse', '🌟Professores Recomendados', '🗓Uma meta para o ano'])

# with aba1:
#     st.write('Coloque aqui')

# with aba2:
#     st.write('Coloque aqui')

# with aba3:
#     st.write('Coloque aqui')






# import streamlit as st
# import pandas as pd

# st.set_page_config(
#     page_title = 'Canal do FlameTube',
#     page_icon = '📺',
#     layout = 'wide'
# )

# st.markdown("""
# <style>
#     #MainMenu, header, footer {
#         visibility: hidden;
#     }
# </style>
# """, unsafe_allow_html = True) # Esconder as configurações para não perder o costume e aprender

# with st.sidebar:
#     st.subheader('Vídeos em ALTA🔥')
#     st.markdown("""
# - [Vídeo 1](https://www.youtube.com)
# - [Vídeo 2](https://www.youtube.com)
# - [Vídeo 3](https://www.youtube.com)
# """)

#     st.link_button('Ir às configurações', url='#')

# col1, col2 = st.columns([2, 5])

# with col1:
#     st.image('https://cdn.awsli.com.br/2616/2616870/favicon/perfil-1logo-redonda-site-5jcwke106n.ico', width=250, caption='Flame👑')

# with col2:
#     estatisticas = pd.Series({
#         'Canal': 'Flame👑',
#         'Usuário': 'FlameOFC',
#         'Inscritos': 665743,
#         'Vídeos': 56,
#         'Descrição': 'Gosto de Hacking, Programação, Ciência, Astronomia, Filosofia. Apaixonado por aprender! ❤',
#     })

#     estatisticas['Usuário'] = f'@{estatisticas['Usuário']}' # Adicionando o @ no Usuário (Como se fosse uma coisa automatizada)
#     with st.expander('Ver informações do canal'):
#         st.write(estatisticas)

#         st.link_button('Entrar em contanto', url='FlameOFC@mail.com')

    
#     if st.button('Se inscrever'):
#         st.write('Agora você é um inscrito de Flame👑')
#         st.balloons()
        # Só um problema aqui, queria atualizar os inscritos, e não queria escrever estatisticas denovo, apenas substituir aquelas estatisticas e alterar os inscritos para +1, poderia me ajudar aqui??







# import streamlit as st

# st.set_page_config(
#     page_title = "Central de Estudos",
#     page_icon = "📘",
#     layout = "centered"
# )

# with st.sidebar:
#     with st.expander('Matérias'):
#         fisica, python, robotica = st.tabs(['Física', 'Python', 'Robótica'])
#         with fisica:
#             st.write("""
# A mecânica quântica (também conhecida como física quântica e teoria quântica) é a teoria física que obtém sucesso no estudo dos sistemas físicos cujas dimensões são próximas ou abaixo da escala atômica, tais como moléculas, átomos, elétrons, prótons e outras partículas subatômicas, muito embora também possa descrever fenômenos macroscópicos em diversos casos.[2]

# A mecânica quântica é um ramo fundamental da física com vasta aplicação. A teoria quântica fornece descrições precisas para muitos fenômenos previamente inexplicados tais como a radiação de corpo negro e a estabilidade dos átomos. Apesar de, na maioria dos casos, a mecânica quântica ser relevante para descrever sistemas microscópicos, os seus efeitos específicos não são somente perceptíveis em tal escala.

# Por exemplo, a explicação de fenômenos macroscópicos como a super fluidez e a supercondutividade só é possível se considerarmos que o comportamento microscópico da matéria é quântico. A quantidade característica da teoria, que determina quando ela é necessária para a descrição de um fenômeno, é a chamada constante de Planck, que tem dimensão de momento angular ou, equivalentemente, de ação.

# A mecânica quântica recebe esse nome por prever um fenômeno bastante conhecido dos físicos: a quantização. No caso dos estados ligados (por exemplo, um elétron orbitando em torno de um núcleo positivo) a Mecânica Quântica prevê que a energia (do elétron) deve ser quantizada. Este fenômeno é completamente alheio ao que prevê a teoria clássica.

# Um panorama

# O desenvolvimento da mecânica quântica foi uma necessidade gerada pelo acúmulo de resultados experimentais ao longo da virada dos séculos XIX e XX, os quais não conseguiam ser entendidos ou explicados à luz das teorias físicas existentes naquele período. As tentativas de contornar as dificuldades através da adaptação dos formalismos e ferramentas então disponíveis foram paulatinamente abandonadas, pois logo ficou claro que novas frentes conceituais e técnicas teriam que ser abertas. As propostas de uma equação de onda, que generalizava ideias acerca do caráter ondulatório das partículas, bem como de uma formulação matricial, baseada na utilização de observáveis experimentais na descrição dos sistemas atômicos, logo foram seguidas por trabalhos mais marcadamente matemáticos, que tinham por principal objetivo aparar possíveis arestas formais surgidas ao longo desse avanço conceitual.[3]

# A palavra “quântica” (do Latim quantum) quer dizer quantidade. Na mecânica quântica, esta palavra refere-se a uma unidade discreta que a teoria quântica atribui a certas quantidades físicas, como a energia de um elétron contido num átomo em repouso. A descoberta de que as ondas eletromagnéticas podem ser explicadas como uma emissão de pacotes de energia (chamados quanta) conduziu ao ramo da ciência que lida com sistemas moleculares, atômicos e subatômicos. Este ramo da ciência é atualmente conhecido como mecânica quântica.

# A mecânica quântica é a base teórica e experimental de vários campos da Física e da Química, incluindo a física da matéria condensada, física do estado sólido, física atômica, física molecular, química computacional, química quântica, física de partículas e física nuclear. Os alicerces da mecânica quântica foram estabelecidos durante a primeira metade do século XX por Albert Einstein, Werner Heisenberg, Max Planck, Louis de Broglie, Niels Bohr, Erwin Schrödinger, Max Born, John von Neumann, Paul Dirac, Wolfgang Pauli, Richard Feynman e outros. Alguns aspectos fundamentais da contribuição desses autores ainda são alvo de investigação.

# Normalmente é necessário utilizar a mecânica quântica para compreender o comportamento de sistemas em escala atômica ou molecular. Por exemplo, se a mecânica clássica governasse o funcionamento de um átomo, o modelo planetário do átomo — proposto pela primeira vez por Rutherford — seria um modelo completamente instável. Segundo a teoria eletromagnética clássica, toda carga elétrica acelerada emite radiação. Por outro lado, o processo de emissão de radiação consome a energia da partícula. Dessa forma, o elétron, enquanto caminha na sua órbita, perderia energia continuamente até colapsar contra o núcleo positivo.

# O conceito de estado na mecânica quântica
# Em física, chama-se "sistema" um fragmento concreto da realidade que foi separado para estudo. Dependendo do caso, a palavra sistema refere-se a um elétron ou um próton, um pequeno átomo de hidrogênio ou um grande átomo de urânio, uma molécula isolada ou um conjunto de moléculas interagentes formando um sólido ou um vapor. Em todos os casos, sistema é um fragmento da realidade concreta para o qual deseja-se chamar atenção.

# Dependendo da partícula pode-se inverter polarizações subsequentes de aspecto neutro.

# A especificação de um sistema físico não determina unicamente os valores que experimentos fornecem para as suas propriedades (ou as probabilidades de se medirem tais valores, em se tratando de teorias probabilísticas). Além disso, os sistemas físicos não são estáticos, eles evoluem com o tempo, de modo que o mesmo sistema, preparado da mesma forma, pode dar origem a resultados experimentais diferentes dependendo do tempo em que se realiza a medida (ou a histogramas diferentes, no caso de teorias probabilísticas). Essa ideia conduz a outro conceito-chave: o conceito de "estado". Um estado é uma quantidade matemática (que varia de acordo com a teoria) que determina completamente os valores das propriedades físicas do sistema associadas a ele num dado instante de tempo (ou as probabilidades de cada um de seus valores possíveis serem medidos, quando se trata de uma teoria probabilística). Em outras palavras, todas as informações possíveis de se conhecer em um dado sistema constituem seu estado.

# Cada sistema ocupa um estado num instante no tempo e as leis da física devem ser capazes de descrever como um dado sistema parte de um estado e chega a outro. Em outras palavras, as leis da física devem dizer como o sistema evolui (de estado em estado).

# Muitas variáveis que ficam bem determinadas na mecânica clássica são substituídas por distribuições de probabilidades na mecânica quântica, que é uma teoria intrinsecamente probabilística (isto é, dispõe-se apenas de probabilidades não por uma simplificação ou ignorância, mas porque isso é tudo que a teoria é capaz de fornecer).

# A representação do estado

# No formalismo da mecânica quântica, o estado de um sistema num dado instante de tempo pode ser representado de duas formas principais:

# Em suma, tanto as "funções de onda" quanto os "vetores de estado" (ou kets) representam os estados de um dado sistema físico de forma completa e equivalente e as leis da mecânica quântica descrevem como vetores de estado e funções de onda evoluem no tempo.

# Estes objetos matemáticos abstratos (kets e funções de onda) permitem o cálculo da probabilidade de se obter resultados específicos em um experimento concreto. Por exemplo, o formalismo da mecânica quântica permite que se calcule a probabilidade de encontrar um elétron em uma região particular em torno do núcleo.

# Quando uma função é exclusiva das coordenadas espaciais, ela é dita estacionária, ou seja, seu potencial não depende do tempo. Esta condição permite separar a função de onda em dois movimentos interdependentes. Um deles está ligado a coordenadas espaciais e o outro à coordenada temporal. Esta separação transforma a equação de Schrödinger, uma equação diferencial parcial muito usada na mecânica quântica, em duas equações diferenciais ordinárias, cada qual dependendo de apenas uma variável. O primeiro postulado da mecânica quântica refere-se, justamente, à função de onda. Esta é uma entidade complexa à qual não se atribui qualquer sentido físico especial, e o que a torna fisicamente relevante é o seu módulo quadrado (ou o produto da função de onda por seu complexo conjugado), pois este módulo quadrado representa uma probabilidade. O requisito para a aceitabilidade da função de onda é o fato de ela ser contínua, finita e apresentar um único valor para cada entidade.[5]

# Para compreender seriamente o cálculo das probabilidades a partir da informação representada nos vetores de estado e funções de onda é preciso dominar alguns fundamentos de álgebra linear.

# Formulação matemática

# Muitos fenômenos quânticos difíceis de se imaginar concretamente podem ser compreendidos com um pouco de abstração matemática. Há três conceitos fundamentais da matemática - mais especificamente da álgebra linear - que são empregados constantemente pela mecânica quântica. São estes: (1) o conceito de operador; (2) de autovetor; e (3) de autovalor.

# Vetores e espaços vetoriais

# Na álgebra linear, um espaço vetorial (ou o espaço linear) é uma coleção dos objetos abstratos (chamados vetores) que possuem algumas propriedades que não serão completamente detalhadas aqui.

# Por agora, importa saber que tais objetos (vetores) podem ser adicionados uns aos outros e multiplicados por um número escalar. O resultado dessas operações é sempre um vetor pertencente ao mesmo espaço. Os espaços vetoriais são os objetos básicos do estudo na álgebra linear, e têm várias aplicações na matemática, na ciência, e na engenharia.

# O espaço vetorial mais simples e familiar é o espaço Euclidiano bidimensional. Os vetores neste espaço são pares ordenados e são representados graficamente como "setas" dotadas de módulo, direção e sentido. No caso do espaço euclidiano bidimensional, a soma de dois vetores quaisquer pode ser realizada utilizando a regra do paralelogramo.

# Todos os vetores também podem ser multiplicados por um escalar - que no espaço Euclidiano é sempre um número real. Esta multiplicação por escalar poderá alterar o módulo do vetor e seu sentido, mas preservará sua direção. O comportamento de vetores geométricos sob estas operações fornece um bom modelo intuitivo para o comportamento dos vetores em espaços mais abstratos, que não precisam de ter a mesma interpretação geométrica. Como exemplo, é possível citar o espaço de Hilbert (onde "habitam" os vetores da mecânica quântica). Sendo ele também um espaço vetorial, é certo que possui propriedades análogas àquelas do espaço Euclidiano.

# Os operadores na mecânica quântica

# Um operador é um ente matemático que estabelece uma relação funcional entre dois espaços vetoriais. A relação funcional que um operador estabelece pode ser chamada transformação linear. Os detalhes mais formais não serão apontados aqui. Interessa, por enquanto, desenvolver uma ideia mais intuitiva do que são esses operadores.

# Por exemplo, considere o Espaço Euclidiano. Para cada vetor nesse espaço é possível executar uma rotação (de um certo ângulo) e encontrar outro vetor no mesmo espaço. Como essa rotação é uma relação funcional entre os vetores de um espaço, podemos definir um operador que realize essa transformação. Assim, dois exemplos bastante concretos de operadores são os de rotação e translação.

# Do ponto de vista teórico, a semente da ruptura entre as físicas quânticas e clássicas está no emprego dos operadores. Na mecânica clássica, é usual descrever o movimento de uma partícula com uma função escalar do tempo. Por exemplo, imagine que vemos um vaso de flor caindo de uma janela. Em cada instante de tempo podemos calcular a que altura se encontra o vaso. Em outras palavras, descrevemos a grandeza posição com um número (escalar) que varia em função do tempo.

# Uma característica distintiva na mecânica quântica é o uso de operadores para representar grandezas físicas. Ou seja, não são somente as rotações e translações que podem ser representadas por operadores. Na mecânica quântica grandezas como posição, momento linear, momento angular e energia também são representados por operadores.

# Até este ponto já é possível perceber que a mecânica quântica descreve a natureza de forma bastante abstrata. Em suma, os estados que um sistema físico pode ocupar são representados por vetores de estado (kets) ou funções de onda (que também são vetores, só que no espaço das funções). As grandezas físicas não são representadas diretamente por escalares (como 10 m, por exemplo), mas por operadores.

# Os operadores são descritos pelo segundo teorema da mecânica quântica que diz que à toda variável dinâmica, O, passível de medida direta em laboratório, associa-se um operador linear e hermitiano, correspondente. Tal operador pode ser encontrado ao relacionar termos das coordenadas de posição e componentes do momento linear.[6]

# Para compreender como essa forma abstrata de representar a natureza fornece informações sobre experimentos reais é preciso discutir um último tópico da álgebra linear: o problema de autovalor e autovetor.
# """)
#             st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Max_Planck_1933.jpg/250px-Max_Planck_1933.jpg', caption='Max Planck')

#         with python:
#             st.write("""
# Python é uma linguagem de programação de alto nível,[10] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991.[1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CPython.
# A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros.

# Python é uma linguagem de propósito geral de alto nível, multiparadigma, suporta o paradigma orientado a objetos, imperativo, funcional e procedural. Possui tipagem dinâmica e uma de suas principais características é permitir a fácil leitura do código e exigir poucas linhas de código se comparado ao mesmo programa em outras linguagens. Devido às suas características, ela é utilizada, principalmente, para processamento de textos, dados científicos e criação de CGIs para páginas dinâmicas para a web. Foi considerada pelo público a 3ª linguagem "mais amada", de acordo com uma pesquisa conduzida pelo site Stack Overflow em 2018[11] e está entre as 5 linguagens mais populares, de acordo com uma pesquisa conduzida pela RedMonk.[12]

# O nome Python teve a sua origem no grupo humorístico britânico Monty Python,[13] criador do programa Monty Python's Flying Circus, embora muitas pessoas façam associação com o réptil do mesmo nome (em português, píton ou pitão).

# História

# O Python foi concebido no final de 1989[10][13] por Guido van Rossum no Instituto de Pesquisa Nacional para Matemática e Ciência da Computação (CWI), nos Países Baixos, como um sucessor da ABC capaz de tratar exceções e prover interface com o sistema operacional Amoeba[14] através de scripts. Também da CWI, a linguagem ABC era mais produtiva que C, ainda que com o custo do desempenho em tempo de execução. Mas ela não possuía funcionalidades importantes para a interação com o sistema operacional, uma necessidade do grupo. Um dos focos primordiais de Python era aumentar a produtividade do programador.[13]

# Python foi feita com base na linguagem ABC, possui parte da sintaxe derivada do C, compreensão de listas, funções anonimas e função map de Haskell. Os iteradores são baseados na Icon, tratamentos de exceção e módulos da Modula-3, expressões regulares de Perl.

# Em 1991, Guido publicou o código (nomeado versão 0.9.0) no grupo de discussão alt.sources.[1] Nessa versão já estavam presentes classes com herança, tratamento de exceções, funções e os tipos de dado nativos list, dict, str, e assim por diante. Também estava presente nessa versão um sistema de módulos emprestado do Modula-3. O modelo de exceções também lembrava muito o do Modula-3, com a adição da opção else clause.[14] Em 1994 foi formado o principal fórum de discussão do Python, comp.lang.python, um marco para o crescimento da base de usuários da linguagem.

# A versão 1.0 foi lançada em janeiro de 1994. Novas funcionalidades incluíam ferramentas para programação funcional como lambda, map, filter e reduce. A última versão enquanto Guido estava na CWI foi o Python 1.2. Em 1995, ele continuou o trabalho no CNRI em Reston, Estados Unidos, de onde lançou diversas versões. Na versão 1.4 a linguagem ganhou parâmetros nomeados (a capacidade de passar parâmetro pelo nome e não pela posição na lista de parâmetros) e suporte nativo a números complexos, assim como uma forma de encapsulamento.[15]

# Ainda na CNRI, Guido lançou a iniciativa Computer Programming for Everybody (CP4E; literalmente, "Programação de Computadores para Todos"), que visava tornar a programação mais acessível, um projeto financiado pela DARPA.[16] Atualmente o CP4E encontra-se inativo.

# Em 2000, o time de desenvolvimento da linguagem se mudou para a BeOpen a fim de formar o time PythonLabs. A CNRI pediu que a versão 1.6 fosse lançada para marcar o fim de desenvolvimento da linguagem naquele local. O único lançamento na BeOpen foi o Python 2.0, e após o lançamento o grupo de desenvolvedores da PythonLabs agrupou-se na Digital Creations.

# Python 2.0 implementou list comprehension, uma relevante funcionalidade de linguagens funcionais como SETL e Haskell. A sintaxe da linguagem para essa construção é bastante similar a de Haskell, exceto pela preferência do Haskell por caracteres de pontuação e da preferência do python por palavras reservadas alfabéticas. Essa versão 2.0 também introduziu um sistema coletor de lixo capaz de identificar e tratar ciclos de referências.[17]

# Já o 1.6 incluiu uma licença CNRI substancialmente mais longa que a licença CWI que estavam usando nas versões anteriores. Entre outras mudanças, essa licença incluía uma cláusula atestando que a licença era governada pelas leis da Virgínia. A Free Software Foundation alegou que isso era incompatível com a GNU GPL. Tanto BeOpen quanto CNRI e FSF negociaram uma mudança na licença livre do Python que o tornaria compatível com a GPL. Python 1.6.1 é idêntico ao 1.6.0, exceto por pequenas correções de falhas e uma licença nova, compatível com a GPL.[18]

# Python 2.1 era parecido com as versões 1.6.1 e 2.0. Sua licença foi renomeada para Python Software Foundation License.[9] Todo código, documentação e especificação desde o lançamento da versão alfa da 2.1 é propriedade da Python Software Foundation (PSF), uma organização sem fins lucrativos fundada em 2001, um modelo tal qual da Apache Software Foundation.[18] O lançamento incluiu a mudança na especificação para suportar escopo aninhado, assim como outras linguagens com escopo estático.[19] Esta funcionalidade estava desativada por padrão, e somente foi requerida na versão 2.2.

# Uma grande inovação da versão 2.2 foi a unificação dos tipos Python (escritos em C) e classes (escritas em Python) em somente uma hierarquia. Isto tornou o modelo de objetos do Python consistentemente orientado a objeto.[20] Também foi adicionado generator, inspirado em Icon.[21]

# O incremento da biblioteca padrão e as escolhas sintáticas foram fortemente influenciadas por Java em alguns casos: o pacote logging[22] introduzido na versão 2.3,[23] o analisador sintático SAX, introduzido na versão 2.0 e a sintaxe de decoradores que usa @,[24] adicionadas na versão 2.4.[25]

# Em 1 de outubro de 2008 foi lançada a versão 2.6, já visando a transição para a versão 3.0 da linguagem. Entre outras modificações, foram incluídas bibliotecas para multiprocessamento, JSON e E/S, além de uma nova forma de formatação de cadeias de caracteres.[26]

# Atualmente a linguagem é usada em diversas áreas, como servidores de aplicação e computação gráfica. Está disponível como linguagem de script em aplicações como OpenOffice (Python UNO Bridge), Blender e pode ser utilizada em procedimentos armazenados no sistema gerenciador de banco de dados PostgreSQL (PL/Python).

# A terceira versão da linguagem foi lançada em dezembro de 2008,[27] chamada Python 3.0 ou Python 3000. Com noticiado desde antes de seu lançamento,[28] houve quebra de compatibilidade com a família 2.x para corrigir falhas que foram descobertas neste padrão, e para limpar os excessos das versões anteriores.[13] A primeira versão alfa foi lançada em 31 de agosto de 2007, a segunda em 7 de dezembro do mesmo ano.

# Mudanças da versão incluem a alteração da palavra reservada print, que passa a ser uma função, tornando mais fácil a utilização de uma versão alternativa da rotina. Em Python 2.6, isso já está disponível ao adicionar o código from __future__ import print_function.[29] Também, a mudança para Unicode de todas as cadeias de caracteres.[30]

# Em 2012, foi criado o Raspberry Pi, cujo nome foi baseado na linguagem Python. Uma das principais linguagens escolhidas é Python. Python influenciou várias linguagens, algumas delas foram Boo e Cobra, que usa a indentação como definição de bloco e Go, que se baseia nos princípios de desenvolvimento rápido de Python.

# Atualmente, Python é um dos componentes padrão de vários sistemas operacionais, entre eles estão a maioria das distribuições do Linux, AmigaOS 4, FreeBSD, NetBSD, OpenBSD e OS X. A linguagem se tornou a padrão no curso de ciências da computação do MIT em 2009

# Filosofia
# Parte da cultura da linguagem gira ao redor de The Zen of Python, um poema que faz parte do documento "PEP 20 (The Zen of Python)",[31] escrito pelo programador em Python de longa data Tim Peters, descrevendo sumariamente a filosofia do Python. Entre os vinte princípios do poema, estão presentes:

# Pode-se vê-lo através de um easter egg do Python pelo comando:

# Desenvolvimento
# O desenvolvimento de Python é conduzido amplamente através do processo Python Enhancement Proposal ("PEP"), em português Proposta de Melhoria do Python. Os PEPs são documentos de projeto padronizados que fornecem informações gerais relacionadas ao Python, incluindo propostas, descrições, justificativas de projeto (design rationales) e explicações para características da linguagem. PEPs pendentes são revisados e comentados por Van Rossum, o Benevolent Dictator for Life (líder arquiteto da linguagem) do projeto Python. Desenvolvedores do CPython também se comunicam através de uma lista de discussão, python-dev, que é o fórum principal para discussão sobre o desenvolvimento da linguagem. Questões específicas são discutidas no gerenciador de erros Roundup mantido em python.org. O desenvolvimento acontece no auto-hospedado https://svn.python.org/

# Python possui uma licença livre aprovada pela OSI e compatível com a GPL, porém menos restritiva. Ela prevê (entre outras coisas) que binários da linguagem sejam distribuídos sem a necessidade de fornecer o código fonte junto.[9]

# Módulos e frameworks
# Ao longo do tempo têm sido desenvolvidos pela comunidade de programadores muitas bibliotecas de funções especializadas (módulos) que permitem expandir as capacidades base da linguagem. Entre estes módulos especializados destacam-se:

# Ambientes de desenvolvimento integrado
# Existem vários ambientes de desenvolvimento integrado (IDE) disponíveis para Python:

# Sintaxe e semântica

# Construções
# Construções de Python incluem: estrutura de seleção (if, else, elif); estrutura de repetição (for, while), que itera por um container, capturando cada elemento em uma variável local dada; construção de classes (class); construção de sub-rotinas (def); construção de escopo (with), como por exemplo para adquirir um recurso.

# Tipos de dados
# A tipagem de Python é forte, pois os valores e objetos têm tipos bem definidos e não sofrem coerções como em C ou Perl. São disponibilizados diversos tipos de dados nativos:

# Python também permite a definição dos tipos de dados próprios, através de classes. Instâncias são construídas invocando a classe (FooClass()), e as classes são instância da classe type, o que permite metaprogramação e reflexão. Métodos são definidos como funções anexadas à classe, e a sintaxe instância.método(argumento) é um atalho para Classe.método(instância, argumento). Os métodos devem referenciar explicitamente a referência para o objeto incluindo o parâmetro self como o primeiro argumento do método.[34]

# Antes da versão 3.0, Python possuía dois tipos de classes: "old-style" e "new-style". Classes old-style foram eliminadas no Python 3.0, e todas são new-style. Em versões entre 2.2 e 3.0, ambos tipos de classes podiam ser usadas. A sintaxe de ambos estilos é a mesma, a diferença acaba sendo de onde objeto da classe é herdado, direta ou indiretamente (todas classes new-style herdam de object e são instancias de type). As classes new-styles nada mais são que tipos definidos pelo usuário.

# Palavras reservadas

# O Python 3 define as seguintes palavras reservadas:[35]
# A versão 3.10.0 implementou a Structural Pattern Matching (Correspondência de Padrão Estrutural), semelhante ao Switch-Case de outras linguagens, assim como definido na PEP 634.[37] Por isso as palavras match e case passarão a ser reservadas.

# Operadores
# Os operadores básicos de comparação como ==, <, >=, entre outros são usados em todos os tipos de dados, como números, cadeias de texto, listas e mapeamentos. Comparações em cadeia como a < b < c possuem o mesmo significado básico que na matemática: os termos são comparadas na ordem. É garantido que o processamento da expressão lógica irá terminar tão cedo o veredito seja claro, o princípio da avaliação mínima. Usando a expressão anterior, se a < b é falso, c não é avaliado.

# Quanto aos operadores lógicos, até Python 2.2 não havia o tipo de dado booleano. Em todas as versões da linguagem os operadores lógicos tratam "", 0, None, 0.0, [] e {} como falso, enquanto o restante é tratado como verdadeiro de modo geral. Na versão 2.2.1 as constantes True e False foram adicionadas (subclasses de 1 e 0 respectivamente). A comparação binária retorna uma das duas constantes acima.

# Os operadores booleanos and e or também seguem a avaliação mínima. Por exemplo, y == 0 or x/y > 100 nunca lançará a exceção de divisão por zero.

# Interpretador interativo
# O interpretador interativo é uma característica diferencial da linguagem, porque há a possibilidade de testar o código de um programa e receber o resultado em tempo real, antes de iniciar a compilação ou incluí-las nos programas. Por exemplo:

# Análise léxica

# No segundo capítulo do Manual de Referência da Linguagem Python é citado que a análise léxica é uma análise do interpretador em si, os programas são lidos por um analisador sintático que divide o código em tokens.

# Todo programa é dividido em linhas lógicas que são separadas pelo token NEWLINE ou NOVA LINHA, as linhas físicas são trechos de código divididos pelo caractere ENTER. Linhas lógicas não podem ultrapassar linhas físicas com exceção de junção de linhas, por exemplo:

# ou

# Para a delimitação de blocos de códigos, os delimitadores são colocados em uma pilha e diferenciados por sua indentação, iniciando a pilha com valor 0 (zero) e colocando valores maiores que os anteriores na pilha. Para cada começo de linha, o nível de indentação é comparado com o valor do topo da pilha. Se o número da linha for igual ao topo da pilha, a pilha não é alterada. Se o valor for maior, a pilha recebe o nível de indentação da linha e o nome INDENT (empilhamento). Se o nível de indentação for menor, então é desempilhado até chegar a um nível de indentação recebendo o nome DEDENT (desempilhamento). Se não encontrar nenhum valor, é gerado um erro de indentação.

# Abaixo um exemplo de permutação, retirado do capítulo 2.1 sobre Estrutura de linhas na Análise léxica do Manual de Referência da linguagem (Language Reference Manual):

# Indentação
# Python foi desenvolvido para ser uma linguagem de fácil leitura, com um visual agradável, frequentemente usando palavras e não pontuações como em outras linguagens. Para a separação de blocos de código, a linguagem usa espaços em branco e indentação ao invés de delimitadores visuais como chaves (C, Java) ou palavras (BASIC, Fortran, Pascal). Diferente de linguagens com delimitadores visuais de blocos, em Python a indentação é obrigatória. O aumento da indentação indica o início de um novo bloco, que termina da diminuição da indentação.

# Usando um editor de texto comum é muito fácil existir erros de indentação, o recomendado é configurar o editor conforme a análise léxica do Python ou utilizar uma IDE. Todas as IDE que suportam a linguagem fazem indentação automaticamente.

# Exemplo:





# O código está correto para os dois exemplos, mas o analisador léxico verificará se a indentação está coerente. O analisador reconhecerá as palavras reservadas while, def, try, except, return, print e as cadeias de caracteres entre aspas simples e a indentação, e se não houver problemas o programa executará normalmente, senão apresentará a exceção: "Seu programa está com erro no bloco de indentação".

# Na internet, há uma comparação de velocidade e de codificação entre as linguagens Python e BASIC, esta última, o dialeto BBC BASIC for Windows.

# Compilador de bytecode
# A linguagem é de altíssimo nível, como já dito, mas ela também pode compilar seus programas para que a próxima vez que o executar não precise compilar novamente o programa, reduzindo o tempo de carga na execução.

# Utilizando o interpretador interativo não é necessário a criação do arquivo de Python compilado, os comandos são executados interativamente. Porém quando um programa ou um módulo é evocado, o interpretador realiza a análise léxica e sintática, compila o código de alto nível se necessário e o executa na máquina virtual da linguagem.

# O bytecode é armazenado em arquivos com extensão .pyc ou .pyo, este último no caso de bytecode otimizado. Interessante notar que o bytecode da linguagem também é de alto nível, ou seja, é mais legível aos seres humanos que o código de byte do C, por exemplo. Para descompilar um código de byte é utilizado o módulo dis da biblioteca padrão da linguagem e existem módulos de terceiros que tornam o bytecode mais confuso, tornando a descompilação ineficaz.

# Normalmente, o Python trabalha com dois grupos de arquivos:

# Orientação a objetos
# Python suporta a maioria das técnicas da programação orientada a objeto. Qualquer objeto pode ser usado para qualquer tipo, e o código funcionará enquanto haja métodos e atributos adequados. O conceito de objeto na linguagem é bastante abrangente: classes, funções, números e módulos são todos considerados objetos. Também há suporte para metaclasses, polimorfismo, e herança (inclusive herança múltipla). Há um suporte limitado para variáveis privadas.

# Na versão 2.2 de Python foi introduzido um novo estilo de classes em que objetos e tipos foram unificados, permitindo a especialização de tipos. Já a partir da versão 2.3 foi introduzido um novo método de resolução de ambiguidades para heranças múltiplas.[39]

# Uma classe é definida com class nome:, e o código seguinte é a composição dos atributos. Todos os métodos da classe recebem uma referência a uma instância da própria classe como seu primeiro argumento, e a convenção é que se chame este argumento self. Assim os métodos são chamados objeto.método(argumento1, argumento2, ...) e são definidos iguais a uma função, como método(self, argumento1, argumento2, ...). Veja que o parâmetro self conterá uma referência para a instância da classe definida em objeto quando for efetuada esta chamada. Os atributos da classe podem ser acessados em qualquer lugar da classe, e os atributos de instância (ou variável de instância) devem ser declarados dentro dos métodos utilizando a referência à instância atual (self) (ver código contextualizado em anexo).

# Em Python não existe proteção dos membros duma classe ou instância pelo interpretador, o chamado encapsulamento. Convenciona-se que atributos com o nome começando com um _ são de uso privado da classe, mas não há um policiamento do interpretador contra acesso a estes atributos. Uma exceção são nomes começando com __, no caso em que o interpretador modifica o nome do atributo (ver código contextualizado em anexo).

# Python permite polimorfismo, que condiz com a reutilização de código. É fato que funções semelhantes em várias partes do software sejam utilizadas várias vezes, então definimos esta função como uma biblioteca e todas as outras funções que precisarem desta a chamam sem a necessidade de reescrevê-la (ver código contextualizado em anexo).

# Python não possui overloading; não é possível criar duas funções com o mesmo nome, pois elas são consideradas atributos da classe. Caso o nome da função se repita em outra assinatura, o interpretador considera esta última como override e sobrescreve a função anterior. Algumas operações entre diferentes tipos são realizadas através de coerção (ex.: 3.2 + 3).

# É possível encapsular abstrações em módulos e pacotes. Quando um arquivo é criado com a extensão .py, ele automaticamente define um módulo. Um diretório com vários módulos é chamado de pacote e deve conter um modulo chamado __init__, para defini-lo como principal. Estas diferenciações ocorrem apenas no sistema de arquivos. Os objetos criados são sempre módulos. Caso o código não defina qual dos módulos será importado, o padrão é o __init__.

# Programação funcional
# Uma das construções funcionais de Python é compreensão de listas, uma forma de construir listas. Por exemplo, pode-se usar a técnica para calcular as cinco primeiras potências de dois. O algoritmo quicksort também pode ser expressado usando a mesma técnica (ver códigos contextualizados para ambos os casos em anexo).

# Em Python, funções são objetos de primeira classe que podem ser criados e armazenados dinamicamente. O suporte a funções anônimas está na construção lambda (cálculo Lambda). Não há disponibilidade de funções anônimas de fato, pois os lambdas contêm somente expressões e não blocos de código.

# Python também suporta clausuras léxicas desde a versão 2.2 (ver códigos contextualizados para ambos os casos em anexo). Já geradores foram introduzidos na versão 2.2 e finalizados na versão 2.3, e representam o mecanismo de Python para a avaliação preguiçosa de funções (ver códigos contextualizados para ambos os casos em anexo).

# Tratamento de exceções
# Python suporta e faz uso constante de tratamento de exceções como uma forma de testar condições de erro e outros eventos inesperados no programa. É inclusive possível capturar uma exceção causada por um erro de sintaxe. O estilo da linguagem apóia o uso de exceções sempre que uma condição de erro pode aparecer. Por exemplo, ao invés de testar a disponibilidade de acesso a um recurso, a convenção é simplesmente tentar usar o recurso e capturar a exceção caso o acesso seja rejeitado (recurso inexistente, permissão de acesso insuficiente, recurso já em uso, ...).

# Exceções são usadas frequentemente como uma estrutura de seleção, substituindo blocos if-else, especialmente em situações que envolvem threads. Uma convenção de codificação é o EAFP, do inglês, "é mais fácil pedir perdão que permissão". Isso significa que em termos de desempenho é preferível capturar exceções do que testar atributos antes de os usar. Segue abaixo exemplos de código que testam atributos ("pedem permissão") e que capturam exceções ("pedem perdão"):





# Ambos os códigos produzem o mesmo efeito, mas há diferenças de desempenho. Quando spam possui o atributo eggs, o código que captura exceções é mais rápido. Caso contrário, a captura da exceção representa uma perda considerável de desempenho, e o código que testa o atributo é mais rápido. Na maioria dos casos o paradigma da captura de exceções é mais rápido, e também pode evitar problemas de concorrência.[40] Por exemplo, num ambiente multitarefa, o espaço de tempo entre o teste do atributo e seu uso de fato pode invalidar o atributo, problema que não acontece no caso da captura de exceções.

# Biblioteca padrão
# Python possui uma grande biblioteca padrão, geralmente citada como um dos maiores trunfos da linguagem,[41] fornecendo ferramentas para diversas tarefas. Por conta da grande variedade de ferramentas fornecida pela biblioteca padrão, combinada com a habilidade de usar linguagens de nível mais baixo como C e C++, Python pode ser poderosa para conectar componentes diversos de software.

# A biblioteca padrão conta com facilidades para escrever aplicações para a Internet, contando com diversos formatos e protocolos como MIME e HTTP. Também há módulos para criar interfaces gráficas, conectar em bancos de dados relacionais e manipular expressões regulares.

# Algumas partes da biblioteca são cobertas por especificações (por exemplo, a implementação WSGI da wsgiref segue o PEP 333[42]), mas a maioria dos módulos não segue.

# Interoperabilidade
# Um outro ponto forte da linguagem é sua capacidade de interoperar com várias outras linguagens, principalmente código nativo. A documentação da linguagem inclui exemplos de como usar a Python C-API para escrever funções em C que podem ser chamadas diretamente de código Python - mas atualmente esse sequer é o modo mais indicado de interoperação, havendo alternativas tais como Cython, Swig ou cffi. A biblioteca Boost do C++ inclui uma biblioteca para permitir a interoperabilidade entre as duas linguagens, e pacotes científicos fazem uso de bibliotecas de alta performance numérica escritos em Fortran e mantidos há décadas.

# Comentários
# Python fornece duas alternativas para documentar o código. A primeira é o uso de comentários para indicar o que certo código faz. Comentários começam com # e são terminados pela quebra da linha. Não há suporte para comentários que se estendem por mais de uma linha; cada linha consecutiva de comentário deve indicar #. A segunda alternativa é o uso de cadeias de caractere, literais de texto inseridos no código sem atribuição. Cadeias de caracteres em Python são delimitadas por " ou ' para única linha e por \""" ou ''' para múltiplas linhas. Entretanto, é convenção usar o métodos de múltiplas linhas em ambos os casos.

# Diferente de comentários, a cadeias de caracteres usadas como documentação são objetos Python e fazem parte do código interpretado. Isso significa que um programa pode acessar sua própria documentação e manipular a informação. Há ferramentas que extraem automaticamente essa documentação para a geração da documentação de API a partir do código. Documentação através de cadeias de caracteres também pode ser acessada a partir do interpretador através da função help().
# """)
#             st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/He_invented_Python.jpg/250px-He_invented_Python.jpg', caption='Guido van Rossum')
        
#         with robotica:
#             st.write("""
# Robótica é um ramo educacional e tecnológico que trata de sistemas compostos por partes mecânicas automáticas em conjunto com circuitos integrados, tornando sistemas mecânicos motorizados controlados por circuitos elétricos e inteligência computacional. A robótica é objeto de estudo de diversas áreas: computação, aeroespacial, mecânica, automação, elétrica, etc. 

# Cada vez mais as pessoas utilizam os robôs para suas tarefas, como por exemplo o robô aspirador, e robôs para cirurgias médicas.[1] Esta tecnologia, hoje adaptada por muitas fábricas e indústrias, tem obtido, de modo geral, êxito em questões como redução de custos, aumento de produtividade e redução de problemas trabalhistas.[2] Contudo, apesar das vantagens, os robôs acabam trazendo outros problemas específicos, como a demissão de vários funcionários humanos.[3]

# Etimologia e história do termo
# O termo robô foi usado pela primeira vez pelo checo Karel Capek (1890-1938) na peça de teatro intitulada R.U.R. (Rossum's Universal Robots, cujo livro foi lançado no Brasil pela editora Hedra com o título A Fábrica de Robôs),[4] estreada em janeiro de 1921 em Praga.[5] Inicialmente Capek estava decidido a chamar as criaturas automatas da sua peça de labori, em clara referência ao latin labor, "trabalho", mas acatou a sugestão de seu irmão, Josef Čapek (1887-1945) o verdadeiro criador da palavra (ver: Irmãos Čapek)[6] e os chamou de roboti (plural). A palavra robô, derivada de robot/roboti (singular/plural) tem como raiz a palavra checa robota,[7] a qual significa "trabalho forçado, servidão" [8] e tem como uma de suas derivações a palavra rabu, que significa "escravo".[9] Os "robôs" de R.U.R. eram fabricados com matéria orgânica sintética[10] sendo, portanto, mais próximos dos replicantes e dos clones humanos [11] enquanto que na concepção atual, "robô" é definido como sendo composto por partes totalmente mecânicas.

# O termo robótica foi criado e popularizado pelo escritor de ficção cientifica Isaac Asimov, no seu livro " I, Robot" de 1950. Neste livro, Asimov criou as Leis da robótica, que, segundo ele, regeriam os robôs no futuro:[12] Crítico de R.U.R., Asimov desenvolveu as Leis para evitar rebeliões de máquinas como as vistas na peça.[13]

# A ideia de se construir robôs começou a tomar força no início do século XX[15] com a necessidade de aumentar a produtividade e melhorar a qualidade dos produtos. É nesta época que o robô industrial encontrou suas primeiras aplicações, o pai da robótica industrial foi George Devol (1912-2011). Devol criou o primeiro robô industrial, denominado Unimate,[16] o qual foi instalado na fábrica da Ford Motor Company de Trenton (Nova Jérsei) em 1961.[17] Devido aos inúmeros recursos que os sistemas de microcomputadores nos oferece, a robótica atravessa uma época de contínuo crescimento que permitirá, em um curto espaço de tempo, o desenvolvimento de robôs inteligentes fazendo assim a ficção do homem antigo se tornar a realidade do homem moderno.

# Robótica coletiva
# A robótica de enxame trabalha com robôs grandes e pequenos e simples onde o objetivo é a otimização da realização de tarefas coletivas complexas.[18][19][20][21]

# O fenômeno da robotização

# Robotização é o nome dado ao processo que envolve a implementação de ferramentas tecnológicas que possibilitem a substituição de tarefas outrora executadas por humanos, de forma que tais atividades passem a ser executadas por meio de robôs.[22].

# A tecnologia envolvendo a robotização é altamente sofisticada e requer elevado grau de conhecimento, e altos níveis de desenvolvimento técnico-científico.[23] Dentre as áreas mais comumente robotizadas, temos o setor computacional, setor aeroespacial, automação industrial (indústria automobilística, têxtil, etc.), setor militar e as atividades médico-hospitalares.[24]

# Aplicações da robótica
# À medida que mais e mais robôs são projetados para tarefas específicas, este método de classificação torna-se mais relevante. Por exemplo, muitos robôs são projetados para trabalhos de montagem, o que pode não ser facilmente adaptável para outras aplicações. Eles são chamados de “robôs de montagem”. Para soldagem por costura, alguns fornecedores fornecem sistemas de soldagem completos com o robô, ou seja, o equipamento de soldagem junto com outras instalações de manuseio de materiais, como mesas giratórias, etc. como uma unidade integrada. Tal sistema robótico integrado é chamado de “robô de soldagem”, embora sua unidade manipuladora discreta possa ser adaptada a uma variedade de tarefas. Alguns robôs são projetados especificamente para manipulação de cargas pesadas e são rotulados como "robôs para serviços pesados".[25]

# As aplicações atuais e potenciais incluem:

# Aspectos básicos dos robôs
# Existem muitos tipos de robôs; eles são usados ​​em muitos ambientes diferentes e para muitos usos diferentes. Embora diversos em aplicação e forma, todos eles compartilham três aspectos básicos quando se trata de seu projeto e construção:[32]

# Projetos robóticos
# O projeto de um robô é necessariamente interdisciplinar e envolve a utilização de conhecimentos de várias áreas clássicas como:

# • Engenharia mecânica: a qual fornece metodologias para o estudo de estruturas e mecanismos em situações estáticas e dinâmicas;     • Engenharias elétrica e eletrônica: fornecem técnicas para o projeto e integração de sensores, interfaces, atuadores e controladores; 

# • Teoria de controle: formula e avalia algoritmos ou critérios de inteligência artificial que realizam os movimentos desejados e controlam as interações entre robô e o ambiente;

# • Ciência da computação: propicia ferramentas para a programação de robôs, capacitando-os à realização das tarefas especificadas. Neste tipo de projeto deve-se ainda considerar entre outros aspectos: 

# • dimensionamento de atuadores, mecanismos, circuitos eletrônicos (hardware), unidades de controle e potência; • cálculos estruturais; 

# • fabricação e montagem de peças de precisão;

# • seleção de materiais; 

# • planificação dos movimentos; 

# • simulação e modelagem; 

# • desenvolvimento de técnicas de programação para o sistema de controle, sistema operacional, diagnose de sistemas/componentes e comunicação ao operador; e 

# • testes de desempenho. 

# Os robôs são máquinas de programação flexível projetadas para operar em diversas situações, logo, as especificações de operação fornecidas pelo fabricante são de caráter geral e relacionam-se a: volume de trabalho, capacidade de carga, velocidade máxima, precisão e repetibilidade. 

# Com a implementação de um sistema robótico em uma fábrica, devem ainda ser analisados aspectos relacionados às áreas econômica e social, como: análise de custos e benefícios, mudanças organizacionais na estrutura da empresa e investimentos diretos e indiretos na produção, redução do número de empregados e remanejamentos.[34]

# Inteligência artificial na robótica[35]
# Nos últimos anos, presenciamos um crescente avanço na área de tecnologia, mais precisamente na robótica e na inteligência artificial. Tal avanço não se dá de forma isolada, pelo contrário, é na sinergia entre estes dois campos que observamos uma verdadeira revolução tecnológica. A combinação de inteligência artificial (IA) com robótica representa um marco na história da inovação, trazendo desenvolvimentos significativos em diversas áreas de atuação.

# A inteligência artificial, por sua vez, vem impulsionando a robótica e revolucionando a forma como os robôs são programados e operados. A capacidade de compreender e aprender com os dados tem sido um dos principais avanços na inteligência artificial.

# A seguir entenderemos as áreas de aplicação

# SAÚDE E MEDICINA
# A robótica e a inteligência artificial têm revolucionado a área da saúde, oferecendo soluções inovadoras e melhorando a qualidade de vida dos pacientes. Por exemplo, robôs cirúrgicos assistidos por inteligência artificial estão sendo utilizados em procedimentos complexos, proporcionando maior precisão e reduzindo os riscos de erro humano. 

# Dessa forma, a combinação de robôs e IA permite a realização de diagnósticos mais precisos e rápidos, auxiliando médicos e pesquisadores no desenvolvimento de tratamentos mais eficazes.

# AGRICULTURA
# A sinergia entre robótica e inteligência artificial tem desempenhado um papel fundamental na modernização da agricultura. Robôs agrícolas autônomos, equipados com sensores avançados e sistemas de IA, podem detectar pragas e doenças nas plantações, permitindo uma intervenção rápida e precisa. Esses robôs são capazes de realizar tarefas como a colheita, o que aumenta a eficiência e reduz a dependência de mão de obra humana.

# INDÚSTRIA
# Na indústria, a sinergia entre robótica e inteligência artificial está transformando a forma como as fábricas operam. Os robôs colaborativos, por exemplo, são capazes de trabalhar em conjunto com os humanos de forma segura e eficiente, aumentando a produtividade e melhorando a segurança no ambiente de trabalho. 

# A IA pode ser usada para otimizar a cadeia de produção, identificando padrões e realizando análises em tempo real, o que resulta em processos mais eficientes e redução de custos.

# TRANSPORTE E LOGÍSTICA
# A sinergia entre robótica e inteligência artificial também está presente no setor de transporte e logística. Carros autônomos, por exemplo, são equipados com sistemas de IA avançados que os permitem dirigir de forma autônoma e segura, reduzindo a ocorrência de acidentes. 

# Além disso, a IA também é utilizada para otimizar rotas de entrega, reduzir congestionamentos e melhorar a eficiência dos processos logísticos.

# EDUCAÇÃO
# A sinergia entre robótica e inteligência artificial tem sido explorada no campo educacional, proporcionando novas formas de aprendizado e interação. Robôs educacionais equipados com sistemas de IA são capazes de auxiliar no ensino, permitindo uma personalização do processo de aprendizagem de acordo com as necessidades e habilidades individuais dos alunos. A robótica educacional também estimula o desenvolvimento de habilidades cognitivas e criativas nas crianças.[35]
# """)
#             st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/Curiosity_-_Robot_Geologist_and_Chemist_in_One%21.jpg/250px-Curiosity_-_Robot_Geologist_and_Chemist_in_One%21.jpg', caption='Curiosity')



# st.title("Central de Estudos - Flame")
# st.caption("Domine uma matéria por vez.")
# resumo = st.text_area('Resumo de hoje', placeholder='Escreva o resumo (Lembre-se de clicar ctrl + enter)')

# download = st.download_button('Fazer o download do resumo', data=resumo, file_name='resumo.txt')




# import streamlit as st

# st.set_page_config(
#     page_title = "Editor de Artigos",
#     page_icon = "📄",
#     layout = "wide"
# )

# with st.sidebar:
#     st.title("Menu")
#     st.write("Novo artigo")
#     st.write("Artigos Salvos")


# st.title("Escreva seu artigo 📄")

# with st.form('Article'):
#     title = st.text_input("Digite o título")
#     data = st.text_area("Artigo", placeholder="Escreva o artigo")

#     submit = st.form_submit_button('Enviar')
#     if submit:
#         st.session_state[title] = data



# for chave, valor in st.session_state.items():
#     if 'FormSubmitter' in chave:
#         pass
#     else:
#         with st.expander(chave):
#             st.write(valor)






# import streamlit as st

# st.set_page_config(
#     page_title = "Flame | Página Oficial",
#     page_icon = "🧠",
#     layout = "wide"
# )

# with st.sidebar:
#     st.badge('Navegação')

#     st.markdown("""
# ### Sobre mim
# - Meu nome é Flame, gosto de ciência, matemática, programação, astronomia e robótica

# ### Projetos
# - Um bot que busca os produtos, os preços e os links de um produto especificado
# - Um bot que aceita um assunto, este assunto é pesquisado na wikipédia e retornado como texto
# - Um bot que pega os dados de climas de uma cidade especifica 

# ### Contato""")

#     st.link_button('Contato pelo Whatsapp', url="#")
#     st.link_button('Contato pelo Email', url="#")


# st.title('🌠 Flame')
# st.subheader('As 3 Regras Fundamentais')
# st.caption('1 - Não disperdisse tempo')
# st.caption('2 - Tenha constância, não pressa e imediatismo')




# O que eu aprendi: É possível usar "with st.sidebar:" e que é possível colocar emojis no ícone da página
