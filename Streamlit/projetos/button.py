import streamlit as st

# """if 'button' not in st.session_state:
#     st.session_state['button'] = 0

# if st.button("Click"):
#     st.session_state['button'] += 1

# st.write(st.session_state['button'])
# """



try: # Verifica se já existe o arquivo

    # Lê o número dentro do arquivo como um inteiro (str daria erro)
    with open("data.txt", "r") as arquivo:
        numero = int(arquivo.read())

    # Escreve o número que já leu anteriormente
    with open("data.txt", "w") as arquivo:
        arquivo.write(str(numero))


except: # Verifica se ainda não existe o arquivo

    # Cria o arquivo e define o contador como 0
    with open("data.txt", "w") as arquivo:
        arquivo.write(str(0))

    # Lê o número dentro do arquivo como um inteiro (str daria erro)
    with open("data.txt", "r") as arquivo:
        numero = int(arquivo.read())

# Cria 3 colunas
col1, col2, col3 = st.columns([1, 1, 3])

with col1:
    # Se for clicado, incrementará +1 ao contador
    if st.button("Incrementar"):
        with open("data.txt", "w") as arquivo:
            numero += 1
            arquivo.write(str(numero))

with col2:
    if st.button("Decrementar"):
        with open("data.txt", "w") as arquivo:
            numero -= 1
            arquivo.write(str(numero))

with col3:
    if st.button("Resetar"):
        with open("data.txt", "w") as arquivo:
            numero = 0
            arquivo.write(str(numero))


st.divider()

st.write(f"Contador: {numero}")
