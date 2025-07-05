import streamlit as st

st.header('Calculadora')


x = st.number_input('Digite o valor de x:')
y = st.number_input('Digite o valor de y:')

botao = st.button(f'Calcular')
if botao:
    st.write(f'A soma de x e y é {x + y}')