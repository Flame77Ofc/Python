import streamlit as st

st.header('Calculadora')

operacao = st.text_input('Qual operação deseja? (adição/subtração/multiplicação/divisão)').lower().strip()

if operacao == 'adição': # ADIÇÃO
    n1 = st.number_input('Digite o primeiro valor:')
    n2 = st.number_input('Digite o segundo valor:')

    botao = st.button(f'Calcular')
    if botao:
        st.write(f'A soma é {n1 + n2}')

elif operacao == 'subtração': # SUBTRAÇÃO
    n1 = st.number_input('Digite o primeiro valor:')
    n2 = st.number_input('Digite o segundo valor:')

    botao = st.button(f'Calcular')
    if botao:
        st.write(f'A subtração é {n1 - n2}')

elif operacao == 'multiplicação': # MULTIPLICAÇÃO
    n1 = st.number_input('Digite o primeiro valor:')
    n2 = st.number_input('Digite o segundo valor:')

    botao = st.button(f'Calcular')
    if botao:
        st.write(f'A multiplicação é {n1 * n2}')

elif operacao == 'divisão': # DIVISÃO
    n1 = st.number_input('Digite o primeiro valor:')
    n2 = st.number_input('Digite o segundo valor:')

    botao = st.button(f'Calcular')
    if botao:
        st.write(f'A divisão é {n1 / n2}')

elif len(operacao) > 0 and operacao not in ['adição', 'subtração', 'multiplicação', 'divisão']:
    st.write('Digite corretamente.')
