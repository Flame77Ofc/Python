import streamlit as st

# """
# Veremos:

# st.set_page_config()
#     - st.set_page_config(page_title="title") # Define o título do site
#     - st.set_page_config(page_icon="icon") # Define o ícone do site
#     - st.set_page_config(layout="centered/wide") # centered: Centraliza o conteúdo; wide: Ocupa a tela toda com o conteúdo

# st.sidebar()

# - Como esconder os layouts
# """


# -------------------------------------------------------------------------------------------------------------------------------


## Configurações da página -> set.page_config()
# O page_title define o nosso título do site, lá em cima na aba do navegador. É como se estivessemos nomeando nosso site com um nome especifico e adequado para o que condiz com as informações do site.
st.set_page_config(page_title="Flame")

# Já o page_icon, pelo nome, indica qual será o ícone do site, e ficará ao lado do título (page_title). Lembrando que o caminho do icon pode ser quanto pelo endereço de uma imagem quanto por caminho local. Ou até mesmo, um emoji!
st.set_page_config(page_icon="https://images.vexels.com/media/users/3/145648/isolated/lists/423beaf5a703c357b4d724a0cb692686-desenhos-animados-de-fogo.png")

# o layout é uma ferramenta muito poderosa. Por padrão, o layout vem como (layout="centered") - Isso significa que todo o conteúdo da página fica no centro. Podemos mudar esse comportamento deixando todo o conteúdo ocupar mais de 80% do espaço da tela, similar a uma tela panorâmica. Para fazer isso, utilizamos o (layout="wide"). Na minha opnião, não é necessário usar o layout="centered", até porque isso já vem como padrão. É como se você fosse a uma loja de cachorro quente e falar: Ok, para ter certeza, quero que meu cachorro-quente tenha salsicha.
st.set_page_config(layout="wide")

# Já vimos como configurar o título, o ícone e o layout do site. Mas ao invés de fazer tudo isso separadamente (digo, em linhas de códidgo separado), podemos fazer isso em apenas uma linha, e é o que deve ser feito. Então escrevemos st.set_page_config([funções]), mas para poder ser legível e fácil de ler, escrevemos cada função na sua própria linha, isso dentro do set_page_config(), deste jeito:
st.set_page_config(
    page_title = "Flame",
    page_icon = "https://images.vexels.com/media/users/3/145648/isolated/lists/423beaf5a703c357b4d724a0cb692686-desenhos-animados-de-fogo.png",
    layout = "wide"
)



## Uau! Uma segunda mini-tela? -> sidebar
# Bom, o sidebar é como nossa tela principal. Podemos fazer (quase) qualquer coisa que podemos fazer com a tela principal. Por isso é difícil cobrir tudo, então, vamos ver algumas funcionalidades que podemos fazer (Isso já está para os planos dos outros dias). Para configurar a nossa sidebar, precisamos da sintaxe:
# sidebar.função(...)
# A função pode ser um write, title, subtitle, badge, markdown, divider, slider, color_picker, etc...
st.sidebar.title('Minha sidebar!') # Definindo um título interno na sidebar
st.sidebar.divider(width="stretch") # Dividindo o conteúdo com uma barra horizontal
st.sidebar.badge('Minha página principal', icon='🚩', color='green') # Criando um texto personalizável - isto é, com cor e ícone.

# Após fazer estas pequenas mudanças, nosso site já fica com um layout mais agradável e "profissional"




# Escondendo o layout do site: Configurações no CSS
# Os três pontinhos, o Deploy, o rerun e o file change podem ser ruins para quando se for lançar um site com streamlit, pois não parece nem um pouco profissional. Por sorte, podemos ocultar isso o markdown + utilizando CSS

# Primeiro passo, escrevemos markwdown, seguido das 3 aspas duplas.
# Logo, escrevemos as tags de style, quanto a tag de abertura quando a tag de fechamento.
# Então selecionamos, dentro da tag style, a classe #MainMenu e as tags footer e header, todos separados por vírgulas
# Depois disso, apenas escrevemos (fora das 3 aspas duplas) unsafe_allow_html = True, fazendo assim com que o código css seja executado:
st.markdown("""
    <style>
    #MainMenu, footer, header {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# Uma coisa muito importante é pôr este código acima de tudo, abaixo da importação do streamlit, assim, não ha muito tempo de carregação de código, pois quando você executa o código, ainda sim é possível ver, por mais que seja muito rápido, as configurações, pois isso indica que ainda não foi carregado o comando.
