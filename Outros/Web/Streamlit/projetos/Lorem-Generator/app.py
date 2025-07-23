import streamlit as st
from random import choice

st.set_page_config(
    page_title = "Lorem Generator",
    page_icon = "🔠",
    layout = "wide"
)

with st.sidebar:
    st.title("Lorem Generator")
    st.divider()

    st.badge("O que é", color='violet', icon="🍇")
    st.caption("O Lorem Generator serve para gerar textos randômicos (aleatórios). Estes textos são úteis para desenvolvedores que necessitam de uma grande quantidade de texto. Ao usar o Lorem Generator, o desenvolvedor/usuário consegue rapidamente obter uma grande quantidade de texto, ao ínves de escrever tudo.")

    st.badge("Utilização - Exemplo", color="green", icon="🌵")
    st.caption("Um desenvolvedor de sites (conhecido como desenvolvedor Front-End) está criando um blog. Como em html e css os elementos podem transbordar (isso é, quebrar a configuração original de uma caixa/contâiner) por causa de muito texto, é muito recomendado usar o Lorem para garantir que muito texto seja suportado dentro da caixa e não quebre.")

    st.badge("Guia", color="red", icon="🍁")
    st.caption("Como usar: Preencha a quantidade necessária de textos que precisam ser gerados, e o programa automaticamente entregará ao usuário todo o texto, permitindo também fazer a instalação do texto. No campo de quantidade, a quantidade mínima de lorem gerados deve ser maior que 0, já o limite é de lorem gerados é 50.")


quantity = int(st.number_input("Quantidade", value=1))

lorem = ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Eum ut corporis eligendi inventore a repellendus voluptates placeat doloremque ullam aperiam eaque vero provident consectetur atque perferendis iste, beatae incidunt ratione?",

"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Sint obcaecati laudantium in ipsum iusto illum id quas odio error. Natus aperiam dolorum ratione magni, deserunt doloremque eius velit delectus tempore?",

"Lorem ipsum dolor sit amet consectetur adipisicing elit. Est atque optio doloremque quod nihil consectetur officia tempore sed debitis, hic, unde sequi amet voluptatem similique? Nisi voluptatum perferendis voluptates accusantium!",

"Lorem, ipsum dolor sit amet consectetur adipisicing elit. Enim repellat ullam, natus assumenda necessitatibus modi minima quasi consectetur. Magni perferendis omnis eius nihil consectetur temporibus qui fuga itaque aut autem.",

"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Perspiciatis perferendis consequatur aspernatur sit beatae, iusto dolorum dolorem alias illum, maxime non a distinctio ipsum, rem labore sapiente quis minus fugit!",

"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Pariatur facilis excepturi mollitia quas qui perferendis officiis autem, corporis reiciendis nemo eligendi maiores odio harum quae molestiae culpa accusamus. Vero, quis!",

"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non ut laudantium vero aliquid omnis unde, perspiciatis possimus accusantium harum voluptatem ratione culpa aperiam suscipit eligendi dignissimos itaque qui? Doloremque, reprehenderit?",

"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Veritatis ratione repellendus ut magnam id recusandae veniam eius dolores saepe tenetur porro vitae itaque eligendi, blanditiis consectetur placeat, et quaerat. Quibusdam.",

"Lorem ipsum dolor sit amet consectetur adipisicing elit. Saepe est quos magni iure corrupti consequuntur animi adipisci quia sequi atque nulla rerum reprehenderit hic, enim beatae iste ipsam suscipit vel.",

"Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusantium voluptatibus dolore quos quae, qui inventore. Voluptas dolor quisquam quae harum ea eveniet soluta ut, at, porro numquam sed exercitationem animi?",

"Lorem ipsum, dolor sit amet consectetur adipisicing elit. Ad omnis ratione voluptates numquam expedita culpa eos nostrum optio est. Quasi dolore quaerat dolores? Ratione doloribus corrupti itaque id fuga dignissimos?",

"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Neque facere nemo veniam velit, doloremque molestiae similique. Laborum reiciendis numquam, esse, qui earum ducimus debitis perspiciatis dolorum est, exercitationem fuga! Voluptatem.",

"Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis eum ut non inventore, accusamus sit optio dicta quibusdam! Velit fugit natus sint assumenda porro veritatis culpa quod facere commodi molestiae.",

"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Repellat a facere inventore dolorum accusantium placeat maiores ut corporis, illum fugiat et, sit quis voluptas est! Numquam culpa officiis perferendis aut?",

"Lorem ipsum dolor sit, amet consectetur adipisicing elit. Libero, optio. Magni sit totam, incidunt velit harum, ut esse ducimus dolorem eius explicabo quae dolore fugit nisi rem quisquam obcaecati reiciendis!",

"Lorem ipsum dolor sit amet, consectetur adipisicing elit. Officia a maxime blanditiis aliquid voluptatem nemo, facilis iste voluptas quae saepe ratione, esse quibusdam eaque nisi porro ab cumque dolorum adipisci?",

"Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo ducimus itaque quam blanditiis quod amet tenetur sequi est facere temporibus, ipsam dolorem, similique dolores labore iusto architecto nobis distinctio. Ut.",

"Lorem ipsum dolor sit amet consectetur, adipisicing elit. Explicabo mollitia, dignissimos, sint quis iure tenetur odit vitae qui maxime totam aspernatur ipsum blanditiis? Voluptates quisquam assumenda placeat adipisci, fuga incidunt!",

"Lorem ipsum dolor sit amet consectetur adipisicing elit. Earum quisquam excepturi libero minima incidunt quod hic ipsum, deleniti ducimus perferendis aspernatur assumenda doloremque odit similique velit rerum quia sed dicta!",
]

submit = st.button("Gerar")
if submit:
    if quantity <= 0:
        st.warning("A quantidade deve ser maior que 0.")
    elif quantity > 50:
        st.warning("O limite de quantidade é 50. Por favor, diminua o campo de quantidade.")
    else:

        teste = []
        for _ in range(quantity):
            choicen = choice(lorem)
            st.write(f"{choicen}")

            teste.append(choicen)


        st.session_state['botao'] = True
        if st.session_state['botao']:
            texto = ""
            for palavra in teste:
                texto += f"{palavra}\n\n"
            st.download_button("Fazer download do texto", data=texto, file_name="lorem.txt")
