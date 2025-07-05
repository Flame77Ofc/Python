import streamlit as st

st.set_page_config(page_title="My first website using Streamlit")
st.header('Esse é o meu cabeçalho, tipo um h1.')
st.subheader('Esse é meu subcabeçalho, tipo um h2.')

st.write('E isso é um texto, tipo um parágrafo mesmo')
st.write('Outro parágrafo')

# Links
st.write('Vendo como funcionam os links')
st.write('Clique aqui para ganhar mais: [link](https://www.google.com)')

# Separando elementos:
st.write('---')

# Botão
st.button('Um botão')



# Integrando Data Science no streamlit
import pandas as pd
st.write(pd.read_csv('a.csv'))