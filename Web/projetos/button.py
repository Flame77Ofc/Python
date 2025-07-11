import streamlit as st

if 'click' not in st.session_state:
    st.session_state['click'] = 0

increment = st.button('Incrementar')
if increment:
    st.session_state['click'] += 1


decrement = st.button('Decrementar')
if decrement:
    st.session_state['click'] -= 1

reset = st.button('Resetar')
if reset:
    st.session_state['click'] = 0


st.divider()
st.write('## Ver as informações de chave valor')
st.write(st.session_state)


for chave in st.session_state.keys():
    st.write(chave)

for valor in st.session_state.values():
    st.write(valor)

for chave, valor in st.session_state.items():
    st.write(chave, valor)

st.write(st.session_state.click)

